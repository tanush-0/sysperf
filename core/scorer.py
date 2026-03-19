def calculate(results):
    score = 0

    if results["cpu"]:
        score += max(0, 100 - results["cpu"]["duration"])

    if results["disk"]:
        score += results["disk"]["write_speed"] / 2

    if results["memory"]:
        score += 20 if results["memory"]["status"] == "success" else 0

    return round(score, 2)