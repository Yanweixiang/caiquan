import random
person=input("请输入:石头(0)剪刀(1)布(2)\n")
person=int(person)
computer=random.randint(0,2)
if person==0:
    print("玩家：石头")
if person==1:
    print("玩家：剪刀")
if person==2:
    print("玩家：布")
if computer==0:
    print("电脑：石头")
if computer==1:
    print("电脑：剪刀")
if computer==2:
    print("电脑：布")

if person==computer:
    print("平局")
elif person==0 and computer==1 or person==1 and computer==2 or person==2 and computer==0:
    print("恭喜你，你赢了")
else:
    print("很遗憾，你输了")