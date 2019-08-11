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

def main():
	pass

if __name__ == '__main__':
	main()