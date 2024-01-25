'''
内嗅皮层
'''

from typing import Callable, Any

from memory.memory import Memory


class EntorhinalCortex:
    def __init__(self, criteria_func: Callable[[Memory], bool], filter_postprocess_func: [[Memory], Memory] = None):
        """
        初始化内嗅皮层类
        :param criteria_func: 用于判断记忆是否符合给定的标准的函数
        eg：

        ```python
        def meets_criteria(memory) -> bool:
            '''
            判断记忆是否符合给定的标准
            :param memory: 待检查的记忆
            :return: 符合标准为True，不符合为False
            这里的逻辑需要根据实际的过滤标准来实现
            例如，可以检查记忆的时间、重要性等
            '''
            return True
        ```

        :param filter_postprocess_func: 一个可选的函数，用于对过滤通过的记忆进行后处理 返回memory
        eg：
        ```python
        def filter_postprocess_func(memory)-> Memory:
            '''
            对过滤通过的记忆进行后处理
            :param memory: 过滤通过的记忆
            :return: 处理后的记忆
            这里的逻辑需要根据实际的需求来实现
            例如，可以对记忆进行加工、修改等操作
            '''
            return memory
        ```

        """

        self.meets_criteria = criteria_func
        self.filter_postprocess_func = filter_postprocess_func

    def filter_memory(self, memory):
        """
        过滤记忆
        :param memory: 记忆实例
        :return: 过滤后的记忆实例
        如果记忆不符合过滤标准，返回None
        """
        # 根据给定的过滤标准过滤记忆
        if not self.meets_criteria(memory):
            return None
        # 记忆过滤通过：后处理逻辑
        if self.filter_postprocess_func:
            memory = self.filter_postprocess_func(memory)
        return memory
