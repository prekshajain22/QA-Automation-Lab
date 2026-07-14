from flask import Flask, jsonify
import subprocess
import json
from pathlib import Path

app = Flask(__name__)

PROJECT_ROOT = Path(__file__).parent.parent
REPORT_FILE = PROJECT_ROOT / "reports" / "result.json"


@app.route("/run-tests", methods=["GET"])
def run_tests():
    result = subprocess.run(
        [
            "pytest",
            "-v",
            "--json-report",
            f"--json-report-file={REPORT_FILE}",
        ],
        cwd=PROJECT_ROOT,
        capture_output=True,
        text=True,
    )

    with open(REPORT_FILE, "r") as file:
        test_results = json.load(file)

    summary = {
        "execution_status": "PASSED" if result.returncode == 0 else "FAILED",
        "total_tests": test_results["summary"].get("total", 0),
        "passed": test_results["summary"].get("passed", 0),
        "failed": test_results["summary"].get("failed", 0),
        "duration_seconds": round(test_results.get("duration", 0), 2),
        "report": "reports/test_report.html",
    }

    return jsonify(summary)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)