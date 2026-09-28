from contextlib import contextmanager

# 1. 基于 contextmanager 装饰器的上下文管理器
@contextmanager
def open_file(path, mode):
    f = open(path, mode, encoding="utf-8")
    try:
        yield f
    finally:
        f.close()

with open_file("test_ctx.txt", "w") as f:
    f.write("hello context manager\n")

with open_file("test_ctx.txt", "r") as f:
    print("文件内容:", f.read().strip())

# 2. 基于类的上下文管理器：计时器
import time

class Timer:
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.elapsed = time.time() - self.start
        print(f"耗时: {self.elapsed:.4f}s")
        return False  # 不吞异常

with Timer():
    time.sleep(1)

# 3. 练习：一个自动回滚的"事务"上下文管理器
class Transaction:
    def __init__(self):
        self.data = []

    def __enter__(self):
        print("开始事务")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            print(f"出错回滚: {exc_val}")
            self.data.clear()
        else:
            print("提交事务")
        return False

with Transaction() as t:
    t.data.append("操作1")
    t.data.append("操作2")
    print("事务内数据:", t.data)

print("事务后数据:", t.data)