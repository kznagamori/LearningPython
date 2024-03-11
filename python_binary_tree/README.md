# 二分木構造

二分木構造をPythonで実装するには、まずノードクラスを定義し、次にこのノードを使用して木を構築します。ノードクラスには、データを格納する値と、左右の子ノードへの参照を持たせます。この基本的な構造を使用して、挿入、検索、およびトラバーサル（木の走査）の操作を行うメソッドを実装します。

以下に、基本的な二分木構造のサンプルプログラムを示します。このプログラムでは、ノードの挿入と、中順走査（ `In-order Traversal` ）での要素の表示を行います。

## サンプルプログラム
```python
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

```

このプログラムでは、まず空の二分木を作成し、`insert` メソッドを使用して複数の値を木に挿入しています。挿入処理は再帰的に行われ、値が現在のノードの値より小さい場合は左の子に、大きい場合は右の子に挿入されます。

中順走査（ `In-order Traversal` ）は、左の子ノード、現在のノード、右の子ノードの順に走査する方法で、このプログラムでは `inorder_traversal` メソッドを通じて実行されます。これにより、挿入された要素が昇順で表示されます。

`main` 関数では、具体的な挿入操作と走査結果の表示が行われています。このプログラムを実行することで、Pythonで二分木構造を実装し、基本的な操作を行う方法を理解することができます。

