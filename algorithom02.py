#!usr/bin/env python
# _*_ coding:UTF-8 _*_
# @Time : 2019/9/18 17:26
# @Author : SeSum
# @FileName : algorithom02.py
# @Software : Sublime

#一些简单算法

#穷举法

# 公鸡5元一只 母鸡3元一只 小鸡1元三只
# 用100元买100只鸡 问公鸡/母鸡/小鸡各多少只

def exhaustive_method_eg1():
	for x in range(20):
		for y in range(33):
			z = 100 - x - y
			if 5 * x + 3 * y + z // 3 == 100 and z % 3 == 0:
				print(x,y,z)


# A、B、C、D、E五人在某天夜里合伙捕鱼 最后疲惫不堪各自睡觉
# 第二天A第一个醒来 他将鱼分为5份 扔掉多余的1条 拿走自己的一份
# B第二个醒来 也将鱼分为5份 扔掉多余的1条 拿走自己的一份
# 然后C、D、E依次醒来也按同样的方式分鱼 问他们至少捕了多少条鱼

def exhaustive_method_eg2():
    fish = 6
    while True:
        total = fish
        enough = True
        for _ in range(5):
            if (total - 1) % 5 == 0:
                total = (total - 1) // 5 * 4
            else:
                enough = False
                break
        if enough:
            print(fish)
            break
        fish += 1


'''
# 问题描述：假设小偷有一个背包，最多能装20公斤赃物，他闯入一户人家，发现如下表所示的物品。很显然，他不能把所有物品都装进背包，
# 所以必须确定拿走哪些物品，留下哪些物品。
电脑 200 20
收音机 20 4
时钟 175 10
花瓶 50 2
书 10 1
油画 90 9
'''
#贪婪法：在对问题求解时，总是做出当前看来最好的选择，不追求最优解，快速找到满意解。
#以价值比例为最优解
def greedy_algorithm_eg():
    class Thing(object):

        def __init__(self, name, price, weight):
            self.name = name
            self.price = price
            self.weight = weight

        @property
        def value(self):
            #价格重量比
            return self.price / self.weight
            #价值最高
            #return self.price
            #重量最轻，物体最多
            #return self.weight


    def input_thing():
        '输入物品信息'
        name_str, price_str, weight_str = input('input name,price,weight:').split()
        return name_str, int(price_str), int(weight_str)


    weight_max, num_things = map(int, input('input max weight and nums of things:').split())
    all_things = []
    for _ in range(num_things):
        all_things.append(Thing(*input_thing()))
    all_things.sort(key=lambda x:x.value, reverse=True)
    #all_things.sort(key=lambda x:x.value)
    total_weight = 0
    total_price = 0
    for thing in all_things:
        if total_weight + thing.weight <= weight_max:
            print('小偷偷走了%s!' % thing.name)
            total_weight += thing.weight
            total_price += thing.price
    print('共偷走价值%d的物品' % total_price)


#heapq实现堆排序
import heapq
def hepsort(args):
    h = []
    for i in args:
        heapq.heappush(h, i)
    return [heapq.heappop(h) for i in range(len(h))]

def main():
	print(hepsort([1,4,67,34,1,34,556,7565,23,5,78]))


if __name__ == '__main__':
	main()