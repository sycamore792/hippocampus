

class Memory:
    def __init__(self, memory_data, memory_create_time):
        self.memory_create_time = memory_create_time
        self.memory_cate = None
        self.memory_data = memory_data

    def classification(self, memory_cate):
        self.memory_cate = memory_cate

    def to_string(self):
        return str(self.memory_data)+f"记忆类型为：{self.memory_cate}"
