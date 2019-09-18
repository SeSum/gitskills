#!usr/bin/env python
# _*_ coding:UTF-8 _*_
# @Time : 2019/8/9 15:01
# @Author : SeSum
# @FileName : algorithm0809.py
# @Software : Sublime

#一些简单算法

#判断闰年

def isLeapYear(year):
	return  ((not year % 4) and (year % 100)) or (not year % 400)

#找零钱
#给定数额的钱，换成相应的零钱

def mod(money):
	money=int(money*100)
	allMoney=[50,20,10,5,1]
	moneyDict={}
	for i in range(len(allMoney)):
		moneyDict[allMoney[i]],money=divmod(money,allMoney[i])
	return moneyDict

#最大公约数，辗转相除法

def maxCommonDivisor(m,n):
	while n != 0:
		m, n = n, m % n
	return m

#最小公倍数
#两数之积等于最大公约数与最小公倍数之积

def maxCommonMultiple(m,n):
	return m * n / maxCommonDivisor(m,n)

#判断素数

def isprime(n):
	flag=True
	for i in range(int(n/2), 1, -1):
		if n % i == 0:
			flag=False
			break
	return flag

#获取所有因子

def getFactors(n):
	factorsList=[n]
	for i in range(1,int(n/2)+1):
		if n % i == 0:
			factorsList.append(i)
	return factorsList

#素因子分解

def decompose(n):
	factorsList=sorted(getFactors(n))
	decomposeList=[]
	factorsList.remove(1)
	factorsList.remove(n)
	print(factorsList)
	for i in range(len(factorsList)):
		print(factorsList[i])
		while n % factorsList[i] == 0:
			decomposeList.append(factorsList[i])
			n = n / factorsList[i]
			print(decomposeList)
	return decomposeList

#获取前N个斐波那契数列

def fibonacci(n):
	fibonacciList=[]
	for i in range(n):
		if i == 0 or i ==1:
			fibonacciList.append(1)
		else:
			fibonacciList.append(fibonacciList[i-1]+fibonacciList[i-2])
	return fibonacciList


#倒三角打印字符串

def triangleDisplay(mystr):
	mystrLen=len(mystr)
	for i in range(mystrLen):
		for y in range(mystrLen-i):
			print(mystr[y+i],end='')
		print()

#两个N位二进制数相加

def biAdd(m,n):
	#不能不同位相加
    addList=[]
    m.reverse()
    n.reverse()
    a,b=0,0
    for i in range(len(m)):
        a,b=divmod(m[i]+n[i]+a,2)
        addList.insert(i,b)
    addList.insert(len(m),a)
    addList.reverse()
    return addList

#不同位数二进制数相加
'''
#verson 1.0
def biAdd2(m,n):
    if len(m) > len(n):
        maxLen=len(m)
        minLen=len(n)
    else:
        maxLen=len(n)
        minLen=len(m)
    addList=[0]*maxLen
    m.reverse()
    n.reverse()
    for i in range(minLen):
        addList[i]=m[i]+n[i]
    if addList[len(addList)-1]>=2:
        addList.append(0)
    for i in range(len(addList)):
        if addList[i]>=2:
            addList[i]-=2
            addList[i+1]+=1
    addList.reverse()
    return addList
'''

#version 2.0
def biAdd3(m,n):
    maxLen=max(len(n),len(m))
    minLen=min(len(n),len(m))
    addList=[0]*maxLen
    m.reverse()
    n.reverse()
    a=0
    for i in range(minLen):
        a,addList[i]=divmod(m[i]+n[i]+a,2)
    if a != 0:
        addList.append(a)
    addList.reverse()
    return addList

"""
Topic: 从1到9，组成3个三位数，要求每个数字只用一次，
要求结果第二个数是第一个数的两倍，第三个数是第一个数的三倍。求所有的组合
算法思想：
使用三层循环先计算第一个数each1，要求三个位不一样
然后先计算符合倍数关系的第二个数each2=2*each1，第三个数each3=3*each1，
然后判断each1、each2和each3这三个数是否每个位都各不相同，
这个将它们拆成单个字符然后放入集合中，如果集合个数=9就符合条件
"""

#version 1.0
def nineNumber():

    #生成3倍小于1000的数
    l=[]
    for i in range(100,999):
        if 3* i < 1000:
            i=str(i)
            if i[0]!=i[1] and i[1]!=i[2] and i[0]!=i[2]:
                if '0' not in i:
                    i=int(i)
                    l.append(i)
    print(l)
    l2=[2*x for x in l]
    l3=[3*x for x in l]
    l4=[]

    for i in range(len(l)):
        l4.append(str(l[i])+str(l2[i])+str(l3[i]))
    finallyStr=[]
    #筛选3个3位数中无重复的数
    '''
    #使用字符串计数，筛选无重复数字
    for i in l4:
        y=list(i)
        for num in range(9):
            flag=False
            if i.count(y[num]) != 1:
                flag=False
                break
            else:
                flag=True
        #排除其中可能诞生的0
        if flag and '0' not in i:
            finallyStr.append(i)
    '''
    #使用集合进行筛选
    for i in l4:
        y=list(i)
        y=set(y)
        if len(y)==9 and '0' not in y:
            finallyStr.append(i)

    return finallyStr

#多项式求和(Horner求值)
#参考链接：https://blog.csdn.net/qq_18738333/article/details/51769204

def hornerPoly(coefficientArr, x):
    res = 0
    for i in range(len(coefficientArr))[-1::-1]:
        res = coefficientArr[i] + x * res
    return res


#简单排序
def select_sort(args):
    args_len=len(args)
    for i in range(args_len-1):
        minindex = i
        for j in range(i+1, args_len):
            if args[minindex] > args[j]:
                args[minindex], args[j] = args[j], args[minindex]
    return args

#冒泡排序
def bubble_sort(args):
    args_len = len(args)
    for i in range(args_len-1):
        for j in range(args_len-1-i):
            if args[j] > args[j+1]:
                args[j], args[j+1] = args[j+1], args[j]
        print(args[args_len-1-i])
    return args

#归并排序（分治法）
#eg:merge_sort([1,2,4,5,3,78,34,22,12])
#对数据进行排序
def merge(args_a, args_b):
    args=[]
    while args_a and args_b:
        if args_a[0] < args_b[0]:
            temp = args_a[0]
            args_a.pop(0)
        else:
            temp = args_b[0]
            args_b.pop(0)
        args.append(temp)
    if args_a:
        for i in range(len(args_a)):
            args.append(args_a[i])
    else:
        for i in range(len(args_b)):
            args.append(args_b[i])
    return args

#对数据进行拆分
def merge_sort(args):

    if len(args) == 1:
        return args
    
    mid_num = len(args) // 2
    left_args = args[:mid_num]
    right_args = args[mid_num:]
    left = merge_sort(left_args)
    right = merge_sort(right_args)
    return merge(left, right)


#顺序查找
def seq_search(args,key):
    for i in range(len(args)):
        if key == args[i]:
            return i
    return -1


#折半查找
def bin_search(args,key):
    #默认已经排好序
    start, end =0, len(args)-1
    
    while start != end:
        mid = (start + end) // 2
        if args[mid] == key:
            return mid
        elif args[mid] > key:
            end = mid - 1
        elif args[mid] < key:
            start = mid + 1
    return -1


def main():
	pass

if __name__ == '__main__':
	main()