import time

def run(size_mb=4096):
    start = time.time()

    try:
        data = bytearray(size_mb * 1024 * 1024)
        duration = time.time() - start

        return {
            "allocated_mb": size_mb,
            "time": round(duration, 3),
            "status": "success"
        }
    except MemoryError:
        return {
            "allocated_mb": size_mb,
            "status": "failed"
        }