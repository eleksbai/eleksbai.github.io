jupyter 环境搭建
```bash
pip install jupyter
cd study_days/jupyter
jupyter notebook
```
jupyter 文档查看
函数名?
help(函数名)

# numpy
多维数组容器, numpy.array

numpy.array和list的区别?
数据类型统一,
```python
import numpy as np
na = np.array([i for i in range(5)])
``` 


### 数据类型 np.dtype
查看数据类型`na.dtype`
类型在初始化时确定
如果为int64位, 对数组某个位置赋值一个浮点数, 则会截位

### np.zeros, np.ones, np.full 特殊的创建方法
shape=(3,5) 3行5列
dtype=int default

np.full((3,5), fill_value=666.0)



### np.arange
np.arange(0,10,0.5), 步长为0.5
np.linspace(0,20,10), 包含0, 20, 获取一个等差数组
X = np.arange(15).reshape(3,5) 对一维数组重新排列成多维数组

### 随机数
np.random.randint(0, 10) 获取一个数
np.random.randint(0,10, size=10) 获取10随机数数组
np.random.randint(0,10, size=(3,5)) 随机获取3行5列的数组

随机种子
np.random.seed(666) 每次生成随机数前调用,可使生成的随机数一样
np.random.random() 获取随机浮点数
np.random.normal() 符合正态分布的浮点数(默认, 均值为0,方差为1)


## 属性
ndim 维度
shape 每个维度下的元素个数(几行几列)
size 所有维度的总数量

## 操作方式
```python
import numpy as np
na= np.random.randint(0,10, size=(3,5))
f=na[0][4] # 无法操作多维切片
f1=na[(0,4)] # 数组的操作方式
f2=na[0,4] # 数组的操作方式, 推荐
```
### 子矩阵
x[::2] 步长为2
X[:2, :3] 前两行,前三列 
X[:,0] 取所有行, 取第一列
python切边创建新对象, numpy默认不会创建新对象.
元素,矩阵和子矩阵共用
subX=X[:2, :3].copy()  创建新对象


##  reshape 移动元素位置, 改变数据维度, 返回一个新的对象
x = np.arange(10)
cx = x.reshape(2, 5) # 必须 2 * 5 = 10                                      
ax = x.reshape(2, -1) # -1表示自动计算 
ay = x.reshape(-1, 5) # -1表示自动计算

##　合并操作
x=np.array([1,2,3])
y=np.array([6,5,4])
c = np.concatenate([x,y]) # 将多个一维数组合并成一个含所有元素的一维数组

xx = np.array([[1,2,3],[4,5,6]])
cc = np.concatenate([xx,xx]) =[[1,2,3],[4,5,6],[1,2,3],[4,5,6]]#将多个二维数组中合并成一个二维数组,其中含有所有的一维数据元素

#　二维数据
第一维度行
第二维度列
一行表示一个样本
一列表示一个特征
[1,2,3] 表示1*3矩阵　表示一行三列　表示一个样本有三个特征


np.concatenate([xx,xx], axis=1) # axis默认为0, 0表示行拼接(打散成行数据在进行组合),1表示列拼接(打散成列数据再进行组合)
= [[]]
