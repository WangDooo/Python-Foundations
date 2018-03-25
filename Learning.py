#======字符串==========================================================
# spilt() rsplit() 设置最大分割次数
#----------------------------------------------------------------
# s = 'hello world my 那 is OK 好的'
# ans1 = s.split(None,3)
# ans2 = s.rsplit(None,2)
# print(ans1,ans2)
#----------------------------------------------------------------


#======字符串==========================================================
# startswith() endswith() 在限定范围内检查字符
#----------------------------------------------------------------
# import os
# s = 'hello world my 那 is OK 好的'
# print(s.startswith('hell',0,7))

# count = 0
# for filename in os.listdir('C:\\Users\\Wang\\Desktop\\Img'):
# 	if filename.endswith(('jpg','JPG')):
# 		count += 1
# print(count)
#----------------------------------------------------------------


#=======复杂数据结构--堆=========================================================
# 堆 是一个二叉树 每个父节点的值都小于或等于子节点的值 最小元素位于二叉树的根节点
# heap[k]<=heap[2*k+1] heap[k]<=heap[2*k+2]
# python heapq模块
#----------------------------------------------------------------
# import heapq
# import random

# data = list(range(10))
# random.shuffle(data)
# heap = [] # 建堆
# for n in data:
# 	heapq.heappush(heap,n)
# heapq.heappush(heap,0.5) # heappush() 新数据入堆
# heapq.heappop(heap) # heappop() 弹出最小元素 堆会自动重建
# print(data,'\n',heap)
# myheap = [1,2,3,5,7,8,9,4,10,333,666]
# print(myheap)
# heapq.heapify(myheap) # heapify() 将列表转化为堆
# print(myheap)
# heapq.heapreplace(myheap,6) # heapqreplace() 替换堆中的元素值，自动重新构建堆
# print(myheap)
# print(heapq.nlargest(3,myheap)) # nlargest() 返回前3个最大的元素
# print(heapq.nsmallest(2,myheap)) # nsmallest() 返回前2个最小的元素
#----------------------------------------------------------------


#=======复杂数据结构--队列=========================================================
# 队列 FIFO(First In First Out),LILO(Last In Last Out)
# queue collections.deque 模块
#----------------------------------------------------------------
# import queue

# q = queue.Queue() # Queue()
# q.put(0)		  # 元素入队 添加到队伍尾部
# q.put(1)
# q.put(2)
# print(q.queue)
# print(q.get())	  # 队列头元素出队
# print(q.queue)
# print(q.get())
# print(q.queue)

# # 后进先出序列
# LiFoQueue = queue.LifoQueue(5)
# LiFoQueue.put(1)
# LiFoQueue.put(2)
# LiFoQueue.put(3)
# print(LiFoQueue.get(),LiFoQueue.get(),LiFoQueue.get())

# # 优先级队列
# PriQueue = queue.PriorityQueue(5) # by order
# PriQueue.put(3)
# PriQueue.put(5)
# PriQueue.put(1)
# PriQueue.put(8)
# print(PriQueue.queue)
# print(PriQueue.get(),PriQueue.get(),PriQueue.get(),PriQueue.get())
#----------------------------------------------------------------


#=======复杂数据结构--栈=========================================================
# 栈 后进先出(Last In First Out) 或 先进后出(First In Last Out)
# pop() 弹出并返回列表的最后一个元素 但若列表为空 pop() 出栈 会报错，另外也无法限制栈的大小
#----------------------------------------------------------------
# myStack = []
# myStack.append(3)
# myStack.append(5)
# myStack.append(7)
# print(myStack)
# print(myStack.pop(),myStack.pop(),myStack.pop())
# myStack.pop() # IndexError: pop from empty list
#----------------------------------------------------------------


#=======复杂数据结构--链表=========================================================
# python用列表进行 链表的创建 节点的插入和删除
# 存在问题 链表为空或删除的元素不存在时 会抛出异常
#----------------------------------------------------------------
# linkTable = []
# linkTable.append(3) # 在尾部追加节点
# linkTable.append(8)
# print(linkTable)
# linkTable.insert(1,99)
# print(linkTable)
# linkTable.remove(3)
# linkTable.remove(linkTable[1])
# print(linkTable)
#----------------------------------------------------------------


#=======复杂数据结构--二叉树=========================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------


#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------


#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------


#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------