from flask import Flask, jsonify, send_file, make_response
import subprocess
import sys
import json
import traceback
import os
import re
from pathlib import Path

from automation_services.pdf_report_generator import generate_pdf


app = Flask(__name__)

PROJECT_ROOT = Path(__file__).parent.parent

REPORT_DIR = PROJECT_ROOT / "reports"

RESULT_FILE = REPORT_DIR / "result.json"

PDF_FILE = REPORT_DIR / "QA_Execution_Report.pdf"


@app.route("/run-tests", methods=["GET"])
def run_tests():

    try:

        REPORT_DIR.mkdir(exist_ok=True)

        print("Starting pytest execution...")

        result = subprocess.run(
            [
                sys.executable,
                "-m",
                "pytest",
                "-v",
                "--json-report",
                f"--json-report-file={RESULT_FILE}",
                "--html=reports/test_report.html",
                "--self-contained-html",
            ],
            cwd=PROJECT_ROOT,
            capture_output=True,
            text=True,
        )

        print("Pytest completed")
        print("Exit code:", result.returncode)

        if not RESULT_FILE.exists():
            raise Exception("result.json was not generated")

        with open(RESULT_FILE, "r", encoding="utf-8") as file:
            pytest_data = json.load(file)

        raw_summary = pytest_data.get("summary", {})

        summary = {
            "total": raw_summary.get("total", 0),
            "passed": raw_summary.get("passed", 0),
            "failed": raw_summary.get("failed", 0),
            "duration": round(pytest_data.get("duration", 0), 2),
        }

        failed_tests = []
        all_tests = []

        for item in pytest_data.get("tests", []):

            node_id = item.get("nodeid", "")
            test_fn = node_id.split("::")[-1]

            name = (
                test_fn
                .replace("test_", "")
                .replace("_", " ")
                .capitalize()
            )

            outcome = item.get("outcome", "unknown").upper()

            screenshot_path = f"screenshots/{test_fn}.png"
            screenshot_exists = (PROJECT_ROOT / screenshot_path).exists()

            test_entry = {
                "name": name,
                "status": outcome,
                "screenshot": screenshot_path if screenshot_exists else None,
            }

            all_tests.append(test_entry)

            if outcome == "FAILED":
                call = item.get("call", {})
                longrepr = str(call.get("longrepr", ""))
                crash = call.get("crash", {})

                # Extract clean assertion message from crash
                crash_message = crash.get("message", "").strip()

                # Extract the failing BDD step from longrepr
                failing_step = None
                match = re.search(
                    r'@(given|when|then)\s*\(\s*["\'](.+?)["\']\s*\)',
                    longrepr,
                    re.IGNORECASE,
                )
                if match:
                    keyword = match.group(1).capitalize()
                    step_text = match.group(2)
                    failing_step = f"{keyword}: {step_text}"

                # Extract execution log (completed actions)
                execution_log = [
                    entry.get("msg", "")
                    for entry in call.get("log", [])
                    if entry.get("msg")
                ]

                failed_tests.append(
                    {
                        "name": name,
                        "failing_step": failing_step,
                        "crash_message": crash_message,
                        "execution_log": execution_log,
                        "screenshot": screenshot_path if screenshot_exists else None,
                    }
                )

        response_data = {
            "execution_status": (
                "PASSED" if result.returncode == 0 else "FAILED"
            ),
            "summary": summary,
            "failed_tests": failed_tests,
            "all_tests": all_tests,
            "html_report": "reports/test_report.html",
        }

        print("Generating PDF report...")

        try:
            pdf_abs_path = PROJECT_ROOT / "reports" / "QA_Execution_Report.pdf"
            generate_pdf(response_data, pdf_abs_path)
            response_data["pdf_report"] = "reports/QA_Execution_Report.pdf"
        except Exception as pdf_error:
            print("PDF generation failed:", pdf_error)
            response_data["pdf_report"] = None

        print("Execution completed successfully")

        return jsonify(response_data)

    except Exception as e:

        tb = traceback.format_exc()
        print(tb)

        return make_response(
            jsonify(
                {
                    "error": str(e),
                    "traceback": tb,
                }
            ),
            500
        )


@app.route("/download-report")
def download_report():

    if not PDF_FILE.exists():

        return jsonify(
            {
                "error": "PDF report not available yet"
            }
        ), 404

    return send_file(
        PDF_FILE,
        as_attachment=True,
        download_name="QA_Execution_Report.pdf",
    )


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False,
        use_reloader=False,
    )
