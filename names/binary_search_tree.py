class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    
    def insert(self, value):
        
        if self.value == None:
            self.value = value
            return
        elif value >= self.value:
            if self.right == None:
                new_node = BinarySearchTree(value)
                self.right = new_node
                return
            else:
                self.right.insert(value)
        elif value < self.value:
            if self.left == None:
                new_node = BinarySearchTree(value)
                self.left = new_node
                return
            else: 
                self.left.insert(value)  

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self == None:
            return False
        elif self.value == target:
            return True
        elif target > self.value:
                if self.right == None: 
                    return False
                else:
                    return self.right.contains(target)
        else: ##remaining case target < self.value
            if self.left == None: 
                return False
            else:
                return self.left.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right == None:
            return self.value
        else:
            return self.right.get_max()

    def for_each(self, cb):
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)  
