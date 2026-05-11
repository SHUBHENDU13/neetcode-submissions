class TreeNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class TreeMap:
    
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        newNode = TreeNode(key, val)
        if not self.root:
            self.root = newNode
            return 
        current = self.root
        while True:
            if key < current.key:
                if current.left == None:
                    current.left = newNode
                current = current.left
            elif key > current.key:
                if current.right == None:
                    current.right = newNode
                current = current.right
            else:
                current.val = val
                return 

    def get(self, key: int) -> int:
        current = self.root
        while current:
            if key < current.key:
                current = current.left
            elif key > current.key:
                current = current.right
            else:
                return current.val
        return -1

    def getMin(self) -> int:
        if not self.root:
            return -1
        current = self.root
        while current and current.left:
            current = current.left
        return current.val

    def getMax(self) -> int:
        if not self.root:
            return -1
        current = self.root
        while current and current.right:
            current = current.right
        return current.val

    def remove(self, key: int) -> None:
        self.root = self.removeHelper(self.root, key)
                

    def getInorderKeys(self) -> List[int]:
        res = []
        return self.inorderHelper(self.root, res)

    def findMin(self, root):
        curr = root
        while curr and curr.left:
            curr = root.left
        return curr

    def removeHelper(self, root, key):
        if not root:
            return None

        if key < root.key:
            root.left = self.removeHelper(root.left, key)
        elif key > root.key:
            root.right = self.removeHelper(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                minNode = self.findMin(root.right)
                root.key = minNode.key
                root.val = minNode.val
                root.right = self.removeHelper(root.right, minNode.key)
        return root
    
    def inorderHelper(self, root, res):
        if root:
            self.inorderHelper(root.left, res)
            res.append(root.key)
            self.inorderHelper(root.right, res)
        return res

