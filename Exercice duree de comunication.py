def durée_de_communication(temps) :
    if temps>120 :
        t1=(temps-120)*0.5+100
        print("the best for you is to pay 200 dh, you will get to infinity time.")
        return t1
    elif temps>60 and temps<120 :
        t2=(temps-60)*1+50
        return t2
    elif temps>30 and temps<60 :
        t3=(temps-30)*1.5+20
        return t3
    elif temps<30 :
        t4=temps*2
        return t4

while True :
    T=int(input("Enter the communication duration of the month in minutes: "))
    print("the total to be paid at the end of the month is : ",durée_de_communication(T))
    x=input("Exit the program (Yes/No) : ")
    if x!="No" :
        break
