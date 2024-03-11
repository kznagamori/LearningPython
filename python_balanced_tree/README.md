# 平衡二分木構造

平衡二分木（AVL木など）の実装は、通常の二分木に比べて複雑です。各ノードにバランスファクターを保持し、挿入や削除のたびに木のバランスを維持するための回転処理が必要になります。ここでは、PythonでのAVL木（自己平衡二分探索木）の簡単な実装例を紹介します。この例では、挿入処理と木のバランスを保つための回転処理を含みます。

## サンプルプログラム
```python
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
```

このプログラムでは、AVL木の基本的な構造と、挿入時のバランス調整ロジック（右回転、左回転）が実装されています。ノードには高さ情報が含まれ、挿入操作のたびにノードの高さが更新され、木のバランスが調整されます。これにより、木が常にバランス状態を維持することができます。

`main` 関数では、いくつかの値を木に挿入し、その後、先行順巡回（ `Pre-order Traversal` ）を使って木の内容を表示しています。AVL木は挿入、削除、検索の

