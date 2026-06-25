class MinStack:

    def __init__(self):
        self._data = []
        self._min = []     

    def push(self, val: int) -> None:
        if not self._min or val<=self._min[-1]:
            self._min.append(val)

        self._data.append(val)
        
    def pop(self) -> None:
        val = self._data.pop()
        if val == self._min[-1]:
            self._min.pop()

    def top(self) -> int:
        return self._data[-1]
        

    def getMin(self) -> int:
        return self._min[-1]

        
