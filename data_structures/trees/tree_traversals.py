def inorder(node):
    if node:
        yield from inorder(node.left)
        yield node
        yield from inorder(node.right)


def preorder(node):
    if node:
        yield node
        yield from preorder(node.left)
        yield from preorder(node.right)


def postorder(node):
    if node:
        yield from postorder(node.left)
        yield from postorder(node.right)
        yield node