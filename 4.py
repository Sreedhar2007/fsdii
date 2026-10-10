'''class  bank:
    def pay(self):
        print("payment is doing")
class gpay(bank):
    def pay(self):
        super().pay()
        print("payment is done by gpay")
class ppay(bank):
    def pay(self):
        print("payment is done by ppay")
p=ppay()
g=gpay()
g.pay()
p.pay()'''

'''class  notification:
    def send(self):
        print("notification is doing")
class email(notification):
    def send(self):
        super().send()
        print("notification is done by email")
class whatsapp(notification):
    def send(self):
        super().send()
        print("notification is done by whatsapp")
class instagram(notification):
    def send(self):
        super().send()
        print("notification is done by instagram")
        
p=instagram()
g=whatsapp()
e=email()
p.send()
g.send()
e.send()'''

'''class  animal:
    def sound(self):
        print("animal is barking")
class dog(animal):
    def sound(self):
        super().sound()
        print("bow bow")
class cat(animal):
    def sound(self):
        super().sound()
        print("meow meow")
class cow(animal):
    def sound(self):
        super().sound()
        print("amba amba")
        
p=cow()
g=cat()
e=dog()
p.sound()
g.sound()
e.sound()'''

class product:
    def __init__(s,name,price,quantity):
        s.name=name
        s.price=price
        s.quantity=quantity
    def display(s):
        print("name:",s.name)
        print("price:",s.price)
        print("quantity:",s.quantity)
class electronic(product):
    def __init__(s,name,price,quantity,warranty):
        super().__init__(name,price,quantity)
        s.warranty=warranty
    def display(s):
        super().display()
        print("warranty:",s.warranty)
class grocery(product):
    def __init__(s,name,price,quantity,exp_days):
        super().__init__(name,price,quantity)
        s.exp_days=exp_days
    def display(s):
        super().display()
        print("exp-days:",s.exp_days)
class clothing(product):
    def __init__(s,name,price,quantity,size):
        super().__init__(name,price,quantity)
        s.size=size
    def display(s):
        super().display()
        print("size:",s.size)
c=clothing("pandu",34,2,6)
g=grocery("hari",25,6,23)
e=electronic("mahi",23,3,10)
c.display()
g.display()
e.display()


'''class vehicle:
    def _init_(s,vno,rent):
        s.vno=vno
        s.rent=rent
    def cal(s):
        c=s.vno*s.rent
        print("total:",c)
class car(vehicle):
    def _init_(s,vno,rent,speed):
        super()._init_(vno,rent)
        s.speed=speed
    def cal(s):
        super().cal()
        print(s.speed)
class truck(vehicle):
    def _init_(s,vno,rent,load):
        s.load=load
        super()._init_(vno,rent)
    def cal(s):
        super().cal()
        print(s.load)
class bike(vehicle):
    def _init_(s,vno,rent,cost):
        s.cost=cost
        super()._init_(vno,rent)
    def cal(s):
        super().cal()
        print(s.cost)
b=bike(20,1200,10000)
t=truck(33,2000,120000)
c=car(10,500,300000)
b.cal()
t.cal()
c.cal()'''

'''class organisation:
    def _init_(s,cname,dept,income):
        s.cname=cname
        s._dept=dept
        s.__income=income
    def display(s):
        print("======within class====")
        print(s.cname,"public")
        print(s._dept,"protected")
        print(s.__income,"private")
class tcs(organisation):
    def show(s):
        print("======derived class======")
        print(s.cname,"public")
        print(s._dept,"protected")
        #print(s.__income)
t=tcs("oracle","cse",20000)
t.display()
t.show()
print("======outside the class====")
print(t.cname,"public")
print(t._dept,"protected")'''
#print(t.__income,"it is not recommended")'

'''class stu:
    def _init_(self,name,marks):
        self.name=name
        self.__marks=marks
    def get_show(self):
        print("name:",self.name)
        print("marks:",self.__marks)
    def set_show(self,new):
        s.__marks=new
s=stu("pandu",45)
s.get_show()
s.set_show(89)
s.get_show()'''

'''class employee:
    def _init_(s,ename,salary,dept):
        s.ename=ename
        s.__salary=salary
        s._dept=dept
    def show(s):
        print(s.ename)
        print(s.__salary)
        print(s._dept)
class manager(employee):
    def set(s,amt):
        s.__salary=amt
    def dis(s):
        print(s.__salary)
m=manager("pandu",20000,"cse")
m.show()
m.set(23450)
m.dis()'''

'''class atm:
    def _init_(self,pin,balance):
        self.__pin=pin
        self.__balance=balance
    def withdraw(self,amt):
        if amt<self.__balance:
            if self.__pin==1234:
                print("withdraw:",amt)
            else:
                print("wrong password")
        else:
            print("insufficient balance")
a=atm(1234,10000)
a.withdraw(2000)'''

'''try:
    a=10
    b=int(input("enter a number:"))
    c=a/b
    print(c)
except ZeroDivisionError as v:
    print(v)
except ValueError as v:
    print(v)
else:
    print("no errors")
finally:
    print("with and without errors")'''

'''[try:
    a=10
    b="hii"
    c=a+b
    print(c)
except TypeError as v:
    print(v)
else:
    print("no errors")'''

'''try:
    l=[10,20,30]
    print(l[0])
except IndexError as v:
    print(v)'''
'''try:
    d={"name":"sreedhar","city":"mpl"}
    print(d["cit"])
except KeyError as v:
    print(v)'''
'''try:
    n="apple"
    print(c)
except NameError as v:
    print(v)'''
try:
    l=[10,20,30]
    print(l.upper())

except AttributeError as v:
    print(v)
