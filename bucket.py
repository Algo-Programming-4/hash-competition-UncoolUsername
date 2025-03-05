class Bucket:
    def __init__(self):
        self.array = []
        self.size = 0


    def push(self, newdata = None):
        if not newdata:
            print("WARNING: self.push() missing required argument (newdata), this call has been ignored.")
            return -1 
        
        self.size += 1
        self.array.append(newdata)


    def remove(self, data_to_remove):
        for list_item in self.array:
            if list_item == data_to_remove:
                self.array.remove(list_item)
                return list_item
        return -1

    def pop(self, index = 0):
        if self.size > 0:
            self.size -= 1
            self.array.pop(index)
        else:
            print("WARNING: self.pop() attempted to remove item at index which does not exist. This call has been ignored.")


    def get(self, data_to_find = None):
        if data_to_find == None:
            print("WARNING self.get() missing required argument (data_to_find), this call has been ignored.")

        # TODO: Consider replacing this with a binary search in the future
        # O(n) time complexity is not too severe in this use case.
        for list_item in self.array:
            if list_item == data_to_find:
                return list_item
            
        return None


    def __str__(self):
        return f"<{str(self.array)}>"
    

    def __repr__(self):
        return "Bucket"