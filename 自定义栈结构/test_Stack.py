import Stack

s = Stack.Stack()
print(s.isEmpty())
print(s.isFull())
s.push(5)
s.push(7)
s.push('a')
s.show()
print(s.pop(),s.pop())
s.push('f')
s.push('a\ee')
s.push('a\e12e')
s.push('a\ee44')
s.show()
s.showRemainderSpace()
s.setSize(3) # 只保留前3个 后面的删除
s.show()