import subprocess

def run(host="google.com"):
    try:
        result = subprocess.run(
            ["ping", "-c", "3", host],
            capture_output=True,
            text=True
        )
        return {"status": "success", "output": result.stdout}
    except Exception as e:
        return {"status": "failed", "error": str(e)}