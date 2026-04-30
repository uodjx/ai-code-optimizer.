# 优化后的代码
def calculate_operations(a: float, b: float) -> tuple:
    """
    计算两个数的加、减、乘结果。
    返回: (和, 差, 积)
    """
    return a + b, a - b, a * b


def get_user_list(max_count: int = 100) -> list:
    """
    生成用户ID列表。
    参数: max_count - 最大数量
    返回: ID列表
    """
    return list(range(max_count))
