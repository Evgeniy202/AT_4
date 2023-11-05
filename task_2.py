class task_2:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(root):
    result = []
    
    def inorder(node):
        if node:
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)
    
    inorder(root)
    return result

root = task_2(1)
root.right = task_2(2)
root.right.left = task_2(3)
print(inorderTraversal(root))

print(inorderTraversal(None))

root = task_2(1)
print(inorderTraversal(root)) 
