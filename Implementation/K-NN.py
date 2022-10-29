import random 
import numpy as np

r = [] # class 1
b = [] # class 0
for i in range(50):
    #크기가 1~10 사이에 있고, 무게가 50~100 사이에 있으면 class 1
    r.append([random.randint(1,10),random.randint(50,100),1])
    #크기가 7~20 사이에 있고, 무게가 80~120 사이에 있으면 class 0
    b.append([random.randint(7,20),random.randint(80,120),0])
    
#점x와 점y의 거리 구하는 함수
def distance(x,y):
    return np.sqrt(pow((x[0]-y[0]),2)+pow((x[1]-y[1]),2))

#knn알고리즘
def knn(x,y,k):
    result=[]
    cnt=0
    for i in range(len(y)):
        result.append([distance(x,y[i]),y[i][2]])
    result.sort()
    for i in range(k):
        if(result[i][1]==i):
            cnt+=1
    if(cnt > (k/2)):
        print("This is class 1")
    else:
        print("This is class 0")

size = input("크기>>")
weight = input("무게>>")
num = input("k>>") #K요소
new = [int(size), int(weight)]

knn(new, r+b, int(num))
