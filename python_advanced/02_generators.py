# 生成器函数：用 yield 逐个产出值
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print("斐波那契前10项:")
for num in fib(10):
    print(num, end=" ")
print()

# 生成器表达式
gen = (x * x for x in range(5))
print("生成器表达式:")
print(next(gen))
print(next(gen))
print(list(gen))  # 剩下的

# 练习：逐行读取大文件的生成器
def read_lines(path):
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            yield line.strip()

# 先造一个测试文件
with open("test_lines.txt", "w", encoding="utf-8") as f:
    f.write("line1\nline2\nline3\n")

print("逐行读取:")
for line in read_lines("test_lines.txt"):
    print(line)

# 对比：列表 vs 生成器的内存差异
import sys
list_comp = [x for x in range(10000)]
gen_comp = (x for x in range(10000))
print("列表占用:", sys.getsizeof(list_comp), "字节")
print("生成器占用:", sys.getsizeof(gen_comp), "字节")
