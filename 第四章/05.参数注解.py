# 参数注解
def calc_data(scores: list[int]) -> tuple[int, int, float]:
    return max(scores), min(scores), max(scores) / min(scores)

print(calc_data([10, 20, 33, 555]))