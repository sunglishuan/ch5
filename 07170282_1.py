x=int(input("請輸入三個數字"))
if(x!=int(x)):
    print("請輸入資料")
if(x>y):
    t=x
    x=y
    y=t
if(x>z):
    t=z
    z=x
    x=t
if(y>z):
    t=y
    y=z
    z=t
print("從小到大的數字為:{},{},{}".format(x,y,z))
