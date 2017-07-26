import random
num=random.random()
while num>0.5:
    num=random.random()
    print(num)



num_heads=0
for i in range(0,100):
    num=random.random()
    if num<0.5:
        num_heads=num_heads+1
print(num_heads)