# backend/vpn.py
import subprocess
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent.parent / "scripts" / "vpn.sh"

def _run(*args):
    result = subprocess.run([SCRIPT, *args],
                            text=True, capture_output=True)
    return {"code": result.returncode,
            "stdout": result.stdout, "stderr": result.stderr}

def init_pki():
    return _run("init-pki")

def build_server():
    return _run("build-server")

def build_client(name: str):
    return _run("build-client", name)

def start():
    return _run("start")

def stop():
    return _run("stop")

def status():
    return _run("status")
