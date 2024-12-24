# part1列表
# part2线性表和索引
# part3越界
# part4列表的修改
a = [1,2,3,4,5,6,7,8,9,10]
print(a)
a[0] = 100 # 修改列表中的元素
print(a)

FriendName = ["kevin","tony","asum"] # 给一个变量FriendName赋值["kevin","tony","asum"]；
print(FriendName) # 输出["kevin","tony","asum"]；
print(FriendName[0]) # 输出"kevin"；

# 越界是描述访问超过线性结构本身长度的行为
# 越界通常发生在线性结构的尾部
# 定义一个Specia1Date的列表，给它赋值三个整型19930305，20100505，20140214，
# 然后修改这个列表的第一个数据Specia1Date[0]，给它重新赋值19930704，
# 最后输出SpecialDate的第一个数据。
SpecialDate = [19930305,20100505,20140214] # 给一个变量SpecialDate赋值[19930305,20100505,20140214]；
print(SpecialDate) # 输出[19930305,20100505,20140214]；
SpecialDate[0] = 19930704 # 修改这个列表的第一个数据SpecialDate[0]，给它重新赋值19930704；
print(SpecialDate) # 输出[19930704,20100505,20140214]；
print(SpecialDate[0]) # 输出19930704；

# 定义一个名为animals的list，它包含三个元素：bear、Python、peacock。
# 要求用格式化输出的形式依次打印这个list当中的元素。
animals = ["bear","Python","peacock"] # 给一个变量animals赋值["bear","Python","peacock"]；
print(animals) # 输出["bear","Python","peacock"]；
print(f"第一个元素是{animals[0]}") # 输出第一个元素是bear；
print(f"第二个元素是{animals[1]}") # 输出第二个元素是Python；
print(f"第三个元素是{animals[2]}") # 输出第三个元素是peacock；

# 现有一个字符串"NocturneProgramming"
# 输出其第一个，第四个和第十个字母。
# 输出其倒数第一个，倒数第四个和倒数第十个字母。
# 输出其第三个到第七个字母。
# 输出其倒数第七个到倒数第三个字母。
a = "NocturneProgramming" # 给一个变量a赋值"NocturneProgramming"；
print(a[0]) # 输出第一个字母；
print(a[3]) # 输出第四个字母；
print(a[9]) # 输出第十个字母；
print(a[-1]) # 输出倒数第一个字母；
print(a[-4]) # 输出倒数第四个字母；
print(a[-10]) # 输出倒数第十个字母；
print(a[2:7]) # 输出第三个到第七个字母；
print(a[-7:-2]) # 输出倒数第七个到倒数第三个字母；
