class DynamicArray:
    def __init__(self, capacity: int):
        self.length = 0
        self.capacity = capacity
        self.arr = [0] * capacity # linear time   

    def get(self, i: int) -> int:
        return self.arr[i] # constant time
    
    def set(self, i: int, n: int):
        self.arr[i] = n # constant time

    def pushback(self, n: int): 
        if self.length == self.capacity:
            self.resize()
        self.arr[self.length] = n
        self.length += 1 # linear time, ammortized = constant

    def popback(self) -> int:
        self.length -= 1
        res = self.arr[self.length]
        self.arr[self.length] = 0
        return res # constant

    def resize(self):
        self.capacity = 2 * self.capacity
        new_arr = [0] * self.capacity

        for i in range(self.length):
            new_arr[i] = self.arr[i] 
        self.arr = new_arr # linear time
        
    def getSize(self) -> int:
        return self.length # constant

    def getCapacity(self) -> int:
        return self.capacity # constant