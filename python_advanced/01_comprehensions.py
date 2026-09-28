# 列表推导式
squares = [x * x for x in range(10) if x % 2 == 0]
print("偶数平方:", squares)

# 字典推导式
square_dict = {x: x * x for x in range(5)}
print("字典:", square_dict)

# 集合推导式
unique_lengths = {len(w) for w in ["ai", "edge", "battery", "llm"]}
print("长度集合:", unique_lengths)

# 嵌套推导式
matrix = [[i * j for j in range(3)] for i in range(3)]
print("矩阵:", matrix)

# 练习：把下面这段改成推导式
# result = []
# for x in range(20):
#     if x % 3 == 0:
#         result.append(x * 2)
result = [x * 2 for x in range(20) if x % 3 == 0]
print("练习结果:", result)
