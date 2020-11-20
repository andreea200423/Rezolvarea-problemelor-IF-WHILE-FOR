a=int(input("Primul nr: "))
b=int(input("Al doilea nr: "))
c=int(input("Al treilea nr: "))
if(a<b+c) and (b<a+c) and (c<a+b):
    if(a==b) or (b==c) or (a==c):
        print("Exista triunghi cu asa lat si e isoscel")
    elif a==b==c:
        print("Exista triunghi cu asa lat si e ehilateral")
    else:
        print("Exista triunghi cu asa lat si e scalen")
else:
    print("Nu estista triunghi cu lat egale cu a,b si c")