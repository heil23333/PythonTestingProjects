import math

def quadratic(a, b, c):
    b2 = b * b
    ac4 = 4 * a * c

    b4ac = math.sqrt(b2 - ac4)

    return ((-b + b4ac)/(2 * a), (-b - b4ac)/(2 * a))


# 测试:
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')
