n = int(input())
#使用不会有重复的集合good放好数
good = set()
#将所有小于 10^9 的2的幂放入列表powers_of_2中，其中数字类型都是字符串
powers_of_2 = []
p = 1
while p <= 10 ** 9:
    powers_of_2.append(str(p))
    good.add(p)
    p *= 2
#进行将数字拼接的循环，每次将拼接后的数字和2的幂拼起来
joint_nums = powers_of_2  #第一次是2的幂和2的幂进行拼接
temp = []  #临时列表，用来传递数据
k = 1
while k < 9:  #因为即使是每次都只将1位数拼起来，拼8次就是九位数了，所以控制拼接次数为8
    for i in joint_nums:  #遍历每一个拼接后的数字
        for j in powers_of_2:  #遍历每一个2的幂
            if len(i + j) > 9:  #(i + j)和(j + i)没有区别
                break  #如果位数大于9，就停止这一次循环，节约时间
            temp.append(i + j)
            good.add(int(i + j))  #注意(i + j)是字符串
    k += 1
    joint_nums = temp  #将新的拼接后的数字存进去，进入下一次循环
    temp = []  #把临时列表空出来
ans = sorted(list(good))  #转换成列表，排列
print(ans[n - 1]) 

