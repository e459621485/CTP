class Test:
    def __init__(self, **kwargs) -> None:
        """
        
        @param id: 任务id
        """
        self.values = kwargs
    
    def get_values(self):
        print(self.values)
        
        
values = {
    'key': 'value',
    'key2': 'value2',
}

test = Test(**values)
test.get_values()