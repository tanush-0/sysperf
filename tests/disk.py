import time
import os

def run(size_mb=500):
    filename = "temp_test_file.bin"
    data = os.urandom(size_mb * 1024 * 1024)

    # Write test
    start = time.time()
    with open(filename, "wb") as f:
        f.write(data)
    write_time = time.time() - start

    # Read test
    start = time.time()
    with open(filename, "rb") as f:
        f.read()
    read_time = time.time() - start

    os.remove(filename)

    return {
        "write_speed": round(size_mb / write_time, 2),
        "read_speed": round(size_mb / read_time, 2)
    }