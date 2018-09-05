def get_height(root):
    if root is None: 
        return 0
    return 1 + max(get_height(root.left), get_height(root.right))

def is_balanced(root):
    # a None tree is balanced
    if root is None: 
        return True
    return is_balanced(root.right) and is_balanced(root.left) and abs(get_height(root.left) - get_height(root.right)) <= 1