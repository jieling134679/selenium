每个进程至少包含一个线程

应用程序通过操作系统提供的系统调用接口，请求操作系统分配一个新的线程

from threading import Thread
from time import sleep 

#定义一个函数，作为新线程执行的入口函数
def threadFunc(arg1, arg2):
    print('子线程开始')
	print(f'线程函数的参数为: {arg1}, {arg2}')
	sleep(3)
	print('子线程结束')

#创建Thread类的示例对象，并且指定新线程的入口函数
thread = Thread(target=threadFunc, args=('参数1', '参数2') )

#执行start()方法，就会创建新线程
#并且新线程会去执行入口函数里面的代码
#这时候，这个线程就有包含主线程在内的两个线程了
thread.start()

#主线程的代码执行子线程对对象的join方法，就会等待子线程结束，才继续执行下面的代码
thread.join()
print('主线程结束')

#--------------------------------------------------------------
多个线程里面的代码需要访问同一个公共的数据对象，程序需要防止线程的代码同时操作公共的数据对象，否则则可能导致数据的访问互相冲突影响
可以使用threading库里面的Lock对象去保护
其他线程想去操作获取加锁的数据时，需要排队等待

from threading import  Lock
bankLock = Lock()

#操作共享数据前，申请获取锁
bankLock.acquire()


#数据操作步骤，省略

#操作完共享数据后，申请释放锁
bankLock.release()