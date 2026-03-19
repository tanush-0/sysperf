import threading
from tests import cpu, memory, disk, network
from config import TEST_CONFIG

results = {
    "cpu": None,
    "memory": None,
    "disk": None,
    "network": None,
    "status": "idle"
}

def run_all():
    global results
    results["status"] = "running"

    results["cpu"] = cpu.run(TEST_CONFIG["cpu_limit"])
    results["memory"] = memory.run(TEST_CONFIG["memory_size_mb"])
    results["disk"] = disk.run(TEST_CONFIG["disk_test_size_mb"])
    results["network"] = network.run(TEST_CONFIG["network_host"])

    results["status"] = "completed"

def start():
    thread = threading.Thread(target=run_all)
    thread.start()