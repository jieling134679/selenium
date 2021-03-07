PYTHON笔记
当有多个参数需要接收，但是不知道参数有多少个的时候，有两种方式可以：

1、将不知道有多少的参数（可变参数）放入list处理，定义可变参数n接收这些参数，这些参入将会被封装为一个tuple保存在n中，一般写法是*args            （可变参数）

可以定义可变参数接受多个变量，比如
def sum_n(*n):
    sum = 0;
    for i in n:
        print(i)
        sum = sum + int(i)*int(i);
    print(sum);
sum_n(1, 3, 5, 7);
python会自动将1,3,5,7组装为一个tuple(1, 3, 5, 7)

如果函数用可变参数接收数据，且调用函数时想要传入list或tuple时：
def sum_n(*n):
    sum = 0;
    for i in n:
        print(i)
        sum = sum + int(i)*int(i);
    print(sum);
sum_n(*[1, 3, 5, 7]);
可以在实参前面加*，表示传进去的是list里的参数


2、将不知道有多少的参数（可变参数）放入dict处理，定义可变参数kw接收这些参数，这些参数会被封装进dict，等号前面为key，等号后面为value，一般写法是**kw（关键字参数）
def person(name,age,**kw):
    print('name :', name);
    print('age :', age);
    print('other paramters :', kw);
    
person('Bob', 5, city='chengdu', height='175')

输出：
name : Bob
age : 5
other paramters : {'city': 'chengdu', 'height': '175'}

3、当输入的参数必须指定key的时候，使用命名关键字参数；*作为分割符，*后面的是命名关键字参数       （命名关键字参数）
def person(name,age,*,city,job):
    print('name :', name);
    print('age :', age);
    print('city :', city);
    print('job :', job);
person('Bob', 5, city='chengdu', job='worker')

当参数中间有可变参数时，后面的默认为命名关键字参数
def person(name,age,*arg,city,job):
    print('name :', name);
    print('age :', age);
    print('arg :', arg)
    print('city :', city);
    print('job :', job);
    
person('Bob', 5, 'aaa','bbb','ccc' ,city='chengdu', job='worker')

输出：
name : Bob
age : 5
arg : ('aaa', 'bbb', 'ccc')
city : chengdu
job : worker

类与对象：
type()可以查看对象类型
定义对象：
class Car:
brand = ‘Benz’             #类的属性
country = ‘Germany’
def pressHorn():              #类的方法
    print(‘didi’)

实例属性通常在类的初始化方法__init__中定义，类在初始化时，解释器会去执行

def __init__(self):
self.color = “red”
self.engine = “612485”
@ 当调用初始化方法实例化对象时，解释器首先会在内存中创建一个类的实例对象，解释器就把这个对象本身作为参数传递进变量self中
@ 在实例化对象时，解释器会自动执行__init__(self)方法

实例可以访问类的属性，类不能访问实例的属性

实例的属性通常是作为参数传递进__init__()方法，例如：
class Car：
brand = 'Benz'

def __init__(self, color, engineSN):
    self.color = color
	self.engineSN = engineSN
	
# 第一个参数self由解释器默认传进去	
car1 = Car('white', 'SN58372')
car2 = Car('black', 'SN84268')

# 注意！！！实例方法的第一个参数始终是self

实例方法定义时，第一个参数必为self
def read(self, book):

在实例调用自己的实例方法时，调用方法的实例本身就作为第一参数传递了进去：
xiaoming.read('mathbook') #xiaoming作为实参传给了self，'mathbook作为实参传给了book'

类的静态方法不能访问实例属性

#----------------------------------------------类的继承
class Car:
    XXX
    XXX
    def __init__(self):
       XXX

#定义BenzCar继承Car
class BenzCar2018(BenzCar):
    price = '880000'
    model = 'Benz2018'

    def __init__(self, color, engineSN, weight, oilweight):
        # 子类的初始化方法需要先调用父类的初始化方法
        # 个人理解：
        # 这里BenzCar2018的对象也是BenzCar的对象，所以可以调用父类Benz的__init__方法，由于还传入两个其他的参数，所以还需要进行两次赋值
        BenzCar.__init__(self, color, engineSN)
        # 或者用这种方法进行初始化，推荐用super()
        super().__init__(color,engineSN)
        self.weight= weight # 车的重量
        self.oilweight = 0  # 油的重量

    # 加油
    def fuel(self, oilweight):
        self.oilweight += oilAdded
        self.weight    += oilAdded

# 这里__init__的第一个参数self其实就是car1
car1 = BenzCar2018('black', 'SN134679', '2t', '500kg')

类的组合关系，即一个类的实例属性里包含另一个类实例
类的属性可以为其他的对象；对象的属性可以是其他的对象

#---------------------------------------打印异常信息
Traceback(most recent call last)
******错误信息按照时间顺序从前到后打印出来，先打印的是最先调用的地方，一直打印到最后报错的那行******

#--------------------------------------Python调用外部应用程序
python擅长调用其他程序

常见的两种方式：
1.os库的system函数
2.subprocess库

import os
command = r'd:\tools\wget http://mirrors.sohu.com/nginx/nginx-1.13.9.zip'
os.system(command)

os.system会默认启动一个命令行cmd程序： Python -> 打开CMD ->CMD中执行指令
但是os.system没法获取输出到CMD的内容
#-------------
如果要对输出到屏幕上的内容进行分析，就要使用subprocess模块
from subprocess import PIPE, Popen

# 第一个参数是要执行的命令；
# stdout=PIPE：重定向输出，输出不再输出到终端，而是输出到管道中
# shell=True打开一个CMD，让CMD去执行命令
proc = Popen('fsutil volume diskfree c:', stdin=None, stdout=PIPE, stderr=None, shell=True)

# communicate 方法返回输出到 标准输出stdout和标准错误stderr 的字节串内容
# 标准输出设备和标准错误设备都是本终端设备
outinfo, errinfo = proc.communicate()
	

#---------------------异常捕获：
try:
    ….
except XXXError:
….


当出现多种except类型时，
try:
    ….
except ZeroDivisionError:
….
except IndexError:
….

捕获所有类型的异常：
import traceback:
try:
100/0
except Exception as e:
print(“未知异常”,e)
print(traceback.format_exc())
#----------------------------------------------字符串编码
在解释器运行过程中，字符在内存中UTF-16存储
'你好'.encode("utf-8") #将内存中的UTF-16的'你好'转为UTF-8对应的字节码:E4 BD A0   E5 A5 BD, UTF-8三个字节表示一个中文，一个字节8位可以表示成两个16进制数



#----------------------------------------------------------------
socket编程：
应用程序A->Socket编程接口->操作系统->通讯硬件           Socket编程接口是由操作系统提供的，编程语言都是去调用的Socket编程接口

TCP分为服务端和客户端，

下面是tcp 服务端程序 server.py

#  === TCP 服务端程序 server.py ===

# 导入socket 库
from socket import *

# 主机地址为空字符串，表示绑定本机所有网络接口ip地址
# 等待客户端来连接
IP = ''
# 端口号
PORT = 50000
# 定义一次从socket缓冲区最多读入512个字节数据
BUFLEN = 512

# 实例化一个socket对象
# 参数 AF_INET 表示该socket网络层使用IP协议
# 参数 SOCK_STREAM 表示该socket传输层使用tcp协议
listenSocket = socket(AF_INET, SOCK_STREAM)

# socket绑定地址和端口
listenSocket.bind((IP, PORT))


# 使socket处于监听状态，等待客户端的连接请求
# 参数 8 表示 最多接受多少个等待连接的客户端
listenSocket.listen(8)
print(f'服务端启动成功，在{PORT}端口等待客户端连接...')

dataSocket, addr = listenSocket.accept()
print('接受一个客户端连接:', addr)

while True:
    # 尝试读取对方发送的消息
    # BUFLEN 指定从接收缓冲里最多读取多少字节
    recved = dataSocket.recv(BUFLEN)

    # 如果返回空bytes，表示对方关闭了连接
    # 退出循环，结束消息收发
    if not recved:
        break

    # 读取的字节数据是bytes类型，需要解码为字符串
    info = recved.decode()
    print(f'收到对方信息： {info}')

    # 发送的数据类型必须是bytes，所以要编码
    dataSocket.send(f'服务端接收到了信息 {info}'.encode())

# 服务端也调用close()关闭socket
dataSocket.close()
listenSocket.close()



下面是tcp 客户端程序 client.py

#  === TCP 客户端程序 client.py ===

from socket import *

IP = '127.0.0.1'
SERVER_PORT = 50000
BUFLEN = 1024

# 实例化一个socket对象，指明协议
dataSocket = socket(AF_INET, SOCK_STREAM)

# 连接服务端socket
dataSocket.connect((IP, SERVER_PORT))

while True:
    # 从终端读入用户输入的字符串
    toSend = input('>>> ')
    if  toSend =='exit':
        break
    # 发送消息，也要编码为 bytes
    dataSocket.send(toSend.encode())

    # 等待接收服务端的消息
    recved = dataSocket.recv(BUFLEN)
    # 如果返回空bytes，表示对方关闭了连接
    if not recved:
        break
    # 打印读取的信息
    print(recved.decode())

dataSocket.close()


#----------------------------------------------
文件和目录操作
#创建目录：os.makedirs可以递归的创建目录结构
import os
os.makedirs('tmp/python/fileop', exist_ok=True)  #exist_ok=True表示如果创建的某个目录已经存在，也不报错


#-----------
import os 

#目标目录
targetDir = r'h:\arch\content'
files = []
dirs = []

#下面三个变量dirpath, dirnames, filenames
#dirpath 代表当前遍历到的目录名
#dirnames 是列表对象，存放当前dirpath中的所有子目录名
#filenames 是列表对象，存放当前dirpath中所有文件名
for (dirpath, dirnames, filenames) in os.walk(targetDir):
    files += filenames
	dirs += dirnames
	
print(files)
print(dirs)

#---------------------字符集
字符集就是数字和字符的映射集合


