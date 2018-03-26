import BinaryTree

root = BinaryTree.BinaryTree('root')
a = root.insertLeftChild('A')
b = root.insertRightChild('B')
c = a.insertLeftChild('3')
d = c.insertRightChild('D')
e = b.insertRightChild('E')
f = e.insertLeftChild('F')

root.inOrder()

a.preOrder()
print('\n')
root.preOrder()