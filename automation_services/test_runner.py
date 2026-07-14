from flask import Flask, jsonify
import subprocess

app = Flask(__name__)


@app.route("/run-tests", methods=["GET"])
def run_tests():
    result = subprocess.run(
        ["pytest", "-v"],
        capture_output=True,
        text=True
    )

    return jsonify(
        {
            "return_code": result.returncode,
            "status": "passed" if result.returncode == 0 else "failed",
            "output": result.stdout,
            "errors": result.stderr,
        }
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)