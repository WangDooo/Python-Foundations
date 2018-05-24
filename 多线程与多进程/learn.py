#================================================================
# 
#----------------------------------------------------------------
'''
并不是使用的线程数量越多越好，如果线程太多，线程调度带来的开销可能会比线程实际执行的开销还要大
'''
#----------------------------------------------------------------


#=======threading模块=========================================================
# threading.active_count() 返回处于alive状态的Thread对象数量
# threading.current_thread() 返回当前Thread对象
# threading.get_ident() 返回当前线程的线程标识符
# threading.enumerate() 返回处于alive状态的所有Thread对象列表
# threading.main_thread() 返回主线程对象
# threading.stack_size([size]) 返回创建线程是的栈的大小
#----------------------------------------------------------------
# import threading

# print(threading.stack_size())
# print(threading.active_count())
# print(threading.current_thread())
# print(threading.enumerate())
#----------------------------------------------------------------


#=======Thread对象========================================================
# Thread类支持使用两种方法来创建线程
# 1. 为构造函数传递一个可调用对象
# 2. 继承Thread类并在派生类中重写__init__() 和 run()方法
# 创建线程对象以后，使用start()启动，该方法会自动调用该类对象的run()方法，此时线程出入alive状态，直至run()方法运行结束
#----------------------------------------------------------------

# start() 自动调用run()方法，启动线程，执行线程代码
# run() 线程代码
# __init__(self,group=None,target=None,name=None,args=(),kwargs=None,verbose=None) 构造函数
# name 读取或设置线程名字
# ident 线程标识
# is_alive() isAlive()
# daemon 布尔值，表示线程是否为守护线程
# join(timeout=None) 等待线程结束或超时返回

#----------------------------------------------------------------


#=========join([timeout])=======================================================
# 阻塞当前线程，等待被调线程结束或超时后再继续执行当前线程的后续代码，timeout指定最长等待时间，单位为秒
#----------------------------------------------------------------
# import threading
# import time

# def func1(x, y):
# 	for i in range(x, y):
# 		print(i, end='')
# 	time.sleep(10)

# t1 = threading.Thread(target=func1, args=(15,20))
# t1.start()
# t1.join(10) # 相当于给t1自己单独的10秒钟时间
# t2 = threading.Thread(target=func1, args=(5,10))
# t2.start()

#----------------------------------------------------------------


#=========isAlive()=======================================================
# 
#----------------------------------------------------------------
# import threading
# import time

# def func1(x, y):
# 	for i in range(x, y):
# 		print(i, end='')
# 	time.sleep(10)

# t1 = threading.Thread(target=func1, args=(15,20))
# t1.start()
# t1.join(10) # 相当于给t1自己单独的10秒钟时间
# t2 = threading.Thread(target=func1, args=(5,10))
# t2.start()
# t2.join()
# print('t1:', t1.isAlive())
# print('t2:', t2.isAlive())
#----------------------------------------------------------------


#=========Thread对象中deamon属性=======================================================
# 一个主线程，在主线程中创建了一个子线程，当主线程结束时根据子线程的daemon属性值不同：
# 1. daemon为False 主线程等子线程结束再结束
# 2. daemon为True 子线程随主线程一起结束，无论是否运行完成
# daemon属性默认值为False 如需修改，则必须在调用start()方法启动线程之前修改
#----------------------------------------------------------------
# import threading
# import time

# # 派生自Thread类的自定义线程类也是一个普通类，拥有线程类特有的run()\start()\join()一系列方法
# class mythread(threading.Thread):
# 	def __init__(self, num, threadname):
# 		threading.Thread.__init__(self, name=threadname)
# 		self.num = num
# 		# self.deamon = True
# 	def run(self):
# 		time.sleep(self.num)
# 		print(self.num)

# t1 = mythread(1, 't1')
# t2 = mythread(5, 't2')
# t2.daemon = True
# print(t1.daemon)
# print(t2.daemon)
# t1.start()
# t2.start()
#----------------------------------------------------------------


#========调用线程对象的普通方法========================================================
# 
#----------------------------------------------------------------
# import threading
# import time

# class myThread(threading.Thread):
# 	def __init__(self, threadName):
# 		threading.Thread.__init__(self)
# 		self.name = threadName

# 	def run(self):
# 		time.sleep(1)
# 		print("In run:", self.name)

# 	def output(self):
# 		print("In output:", self.name)

# t = myThread('test')
# t.start()
# # time.sleep(2)
# t.output()
# time.sleep(5)
# print('OK')

#----------------------------------------------------------------


#=========线程同步技术=Lock/RLocK对象======================================================
# Lock是比较低级的同步原语，当被锁定以后不属于特定的线程
# acquire() unlocked-->locked
# release() locked-->unlocked

# 可重入锁RLocK对象也是一种常用的线程同步原语，可被同一个线程acquire()多次
# RLocK对象的acquire()/release()调用对可以嵌套，仅当最后一个或者最外层的release()执行结束后，锁才会被设置为unlocked状态
#----------------------------------------------------------------
# import threading
# import time

# class mythread(threading.Thread):
# 	def __init__(self):
# 		threading.Thread.__init__(self)

# 	def run(self):
# 		global x
# 		lock.acquire()
# 		for i in range(3):
# 			x = x + i
# 		time.sleep(2)
# 		print(x)
# 		lock.release()

# lock = threading.RLock()
# tl = []
# for i in range(10):
# 	t = mythread()
# 	tl.append(t)
# x = 0
# for i in tl:
# 	i.start()
#----------------------------------------------------------------


#=========Condition 对象=======================================================
# Condition对象可以在某些事情触发后才处理数据，可以用于不同线程之间的通讯，以实现更高级别的同步。
# Condition对象 acquire() release() wait() notify()
#----------------------------------------------------------------
# import threading

# # 生产者线程类
# class Producer(threading.Thread):
# 	def __init__(self, threadname):
# 		threading.Thread.__init__(self, name=threadname)

# 	def run(self):
# 		global x
# 		con.acquire()
# 		if x == 20:
# 			con.wait()
# 		else:
# 			print('\nProducer:', end='')
# 			for i in range(20):
# 				print(x, end='')
# 				x += 1
# 			print(x)
# 			con.notify()
# 		con.release()

# # 消费者线程类
# class Consumer(threading.Thread):
# 	def __init__(self, threadname):
# 		threading.Thread.__init__(self, name=threadname)

# 	def run(self):
# 		global x
# 		con.acquire()
# 		if x == 0:
# 			con.wait()
# 		else:
# 			print('\nConsumer:', end='')
# 			for i in range(20):
# 				print(x, end='')
# 				x -= 1
# 			print(x)
# 			con.notify()
# 		con.release()

# con = threading.Condition()
# x = 0
# p = Producer('Producer')
# c = Consumer('Consumer')
# p.start()
# c.start()
# p.join()
# c.join()

#----------------------------------------------------------------


#=========queue 对象=======================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------


#=========Event 对象=======================================================
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


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------