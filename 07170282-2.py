print("計算票價")
age=int(input("請輸入年齡"))
ticket=100
if(age<=2):
    ticket=0
    print("票價是:{}".format(ticket))
elif(age<=6) or (age>=80):
    ticket=ticket*0.2
    print("票價是:{}".format(ticket))
elif(age<=12) or (age>=60):
    ticket=ticket*0.5
    print("票價是:{}".format(ticket))
elif(age<=18) or (age>=50):
    ticket=ticket*0.8
    print("票價是:{}".format(ticket))
else:
    print("票價是:{}".format(ticket))
