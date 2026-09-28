from typing import List, Dict, Optional, Callable

# 1. 闭包
def make_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

times3 = make_multiplier(3)
times5 = make_multiplier(5)
print("3 * 10 =", times3(10))
print("5 * 10 =", times5(10))

# 2. *args 和 **kwargs
def greet(*args, **kwargs):
    print("位置参数:", args)
    print("关键字参数:", kwargs)

greet("AI", "Edge", name="Alice", age=25)

# 3. 默认参数 + 关键字参数
def train_model(lr=0.001, epochs=10, batch_size=32):
    return f"lr={lr}, epochs={epochs}, batch_size={batch_size}"

print(train_model())
print(train_model(epochs=50))
print(train_model(0.01, 20, 64))

# 4. 类型注解
def process_scores(scores: List[int]) -> Dict[str, float]:
    return {
        "max": float(max(scores)),
        "min": float(min(scores)),
        "avg": sum(scores) / len(scores),
    }

result = process_scores([90, 80, 100, 70])
print("成绩统计:", result)

# 5. Optional 和 Callable
def apply_func(x: int, func: Optional[Callable[[int], int]] = None) -> int:
    if func is None:
        return x
    return func(x)

print(apply_func(5))
print(apply_func(5, lambda n: n * n))

# 6. 综合练习：带类型注解的缓存装饰器
def cache(func: Callable) -> Callable:
    memo: Dict = {}
    def wrapper(*args):
        if args not in memo:
            memo[args] = func(*args)
        return memo[args]
    return wrapper

@cache
def slow_square(n: int) -> int:
    print(f"计算 {n} 的平方")
    return n * n

print(slow_square(4))
print(slow_square(4))
print(slow_square(5))
print(slow_square(5))