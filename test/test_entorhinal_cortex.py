"""
内嗅皮层 测试脚本
"""

from entorhinal_cortex.entorhinal_cortex import EntorhinalCortex
from memory.memory import Memory

memory = Memory("那天我很开心，与凯西交谈了人生的意义。")


def meets_criteria(memory) -> bool:
    # 判断记忆是否符合给定的标准
    # :param
    # memory: 待检查的记忆
    # :return: 符合标准为True，不符合为False
    # 这里的逻辑需要根据实际的过滤标准来实现
    # 例如，可以检查记忆的时间、重要性等
    return True


def filter_postprocess_func(memory) -> Memory:
    '''
    对过滤通过的记忆进行后处理
    :param memory: 过滤通过的记忆
    :return: 处理后的记忆
    这里的逻辑需要根据实际的需求来实现
    例如，可以对记忆进行加工、修改等操作
    '''
    memory.classification("情感类")
    return memory

entorhinal_cortex = EntorhinalCortex(meets_criteria,filter_postprocess_func)
memory_filtered = entorhinal_cortex.filter_memory(memory)
if not memory_filtered:
    print(f"记忆:{memory}已被过滤")
else:
    print(f"内嗅皮层后的记忆为：{memory_filtered.to_string()}")