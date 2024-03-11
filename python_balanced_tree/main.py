class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None
        self.height = 1  # ノードの高さ（バランスの取り方の基準）

class AVLTree:
    def get_height(self, root):
        if not root:
            return 0
        return root.height

    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def right_rotate(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1
        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1
        return x

    def left_rotate(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1
        return y

    def insert(self, root, key):
        if not root:
            return TreeNode(key)
        elif key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance = self.get_balance(root)

        # 左左ケース
        if balance > 1 and key < root.left.val:
            return self.right_rotate(root)
        # 右右ケース
        if balance < -1 and key > root.right.val:
            return self.left_rotate(root)
        # 左右ケース
        if balance > 1 and key > root.left.val:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        # 右左ケース
        if balance < -1 and key < root.right.val:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def preorder_traversal(self, root):
        if root:
            print(root.val, end=' ')
            self.preorder_traversal(root.left)
            self.preorder_traversal(root.right)

def main():
    tree = AVLTree()
    root = None

    # 木にデータを挿入
    for key in [10, 20, 30, 40, 50, 25]:
        root = tree.insert(root, key)

    # 先行順巡回で木を表示
    print("Preorder traversal of the constructed AVL tree is:")
    tree.preorder_traversal(root)
    print()

if __name__ == "__main__":
    main()
