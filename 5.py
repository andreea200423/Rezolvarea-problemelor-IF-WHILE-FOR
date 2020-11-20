an=eval(input("Anul e"))
an -= 2000
rest= an % 12
if rest == 0:
    print("Numele anului e dragon")
elif rest ==1:
    print("Numele anului e sarpe")
elif rest ==2:
    print("Numele anului e cal")
elif rest ==3:
    print("Numele anului e oaie")
elif rest ==4:
    print("Numele anului e maimuta")
elif rest ==5:
    print("Numele anului e cocos")
elif rest ==6:
    print("Numele anului e caine")
elif rest ==7:
    print("Numele anului e porc")
elif rest ==8:
    print("Numele anului e sobolan")
elif rest ==9:
    print("Numele anului e bou")
elif rest ==10:
    print("Numele anului e tigru")
else:
     print("Numele anului e iepure")
