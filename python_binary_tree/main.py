class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, current_node, key):
        if key < current_node.val:
            if current_node.left is None:
                current_node.left = TreeNode(key)
            else:
                self._insert_recursive(current_node.left, key)
        else:
            if current_node.right is None:
                current_node.right = TreeNode(key)
            else:
                self._insert_recursive(current_node.right, key)

    def inorder_traversal(self):
        self._inorder_recursive(self.root)
        print()  # 改行用

    def _inorder_recursive(self, node):
        if node:
            self._inorder_recursive(node.left)
            print(node.val, end=' ')
            self._inorder_recursive(node.right)

def main():
    bt = BinaryTree()
    # 二分木にデータを挿入
    bt.insert(50)
    bt.insert(30)
    bt.insert(20)
    bt.insert(40)
    bt.insert(70)
    bt.insert(60)
    bt.insert(80)
    # 中順走査での要素の表示
    print("Inorder traversal of the binary tree is:")
    bt.inorder_traversal()

if __name__ == "__main__":
    main()
