#inheritance
#1.single inheritance
'''class employee():
    def work(s):
        print("worker")
class manager(employee):
    def manage(s):
        print("manager")
m=manager()
m.work()
m.manage()'''

'''class vehicle():
    def start(s):
        print("car is starting")
    def stop(s):
        print("car is stop")
    def milage(s):
        print("car is given good milage")
class electric(vehicle):
    def charge(s):
        print("for electric car we are using charge")

e=electric()
e.start()
e.stop()
e.milage()
e.charge()'''

#2.multilevel
'''class device():
    def power(s):
        print("power")
class landline(device):
    def call(s):
        print("call is ringing")
class smartphone(landline):
    def browser(s):
        print("showing the webpages")
    def camera(s):
        print("taking the photos")
    def gps(s):
        print("it is showing location")
d=smartphone()
d.gps()
d.camera()
d.power()
d.call()
d.browser()'''
#3.multiple
'''class device:
    def power(s):
        print("power")
class landline:
    def call(s):
        print("call is ringing")
class smartphone(device,landline):
    def gps(s):
        print("location")
s=smartphone()
s.gps()
s.power()
s.call()'''
'''class dad:
    def farmer(s):
        print("dad is a farmer")
class son(dad):
    def student(s):
        print("son is a student")
s=son()
s.student()
s.farmer()'''
#multilevel
'''class college:
    def principal(s):
        print("principal is ramanathan")
class faculty(college):
    def subject(s):
        print("faculty of python is mayuri mam")
class student(faculty):
    def reading(s):
        print("reading the python")
s=student()
s.principal()
s.subject()
s.reading()'''
#multiple
'''class dad:
    def farmer(s):
        print("dad is a farmer")
class mom:
    def housewife(s):
        print("mom is a housemaker")
class son(mom,dad):
    def student(s):
        print("son is a student")       
s=son()
s.student()
s.housewife()
s.farmer()'''
'''class bankaccount:
    def _init_(s,name,balance):
        s.name=name
        s.balance=balance
    def deposit(s,amt):
     s.amt=amt
     c=s.balance+s.amt
     print(f"deposited amt is {s.amt}")
     print("total:",c)
class savingaccount(bankaccount):
    def _init_(s,name,balance,interest_rate):
        super()._init_(name,balance)
        s.interest_rate=interest_rate
        
    def calculate_interest(s):
            interest=s.balance*s.interest_rate/100
            print("interest:",interest)
            
b=savingaccount("pandu",1000,10)
b.deposit(100)
b.calculate_interest()'''

'''class employee:
    def _init_(s,name,salary):
        s.name=name
        s.salary=salary
    def display(s):
        print("name:",s.name)
        print("salary:",s.salary)
    def annualsalary(s):
        total=s.salary*12
        print("total salary is:",total)
class manager(employee):
    def _init_(s,name,salary,dept):
        s.dept=dept
        super()._init_(name,salary)
        print("department is:",dept)
    def calculate_bonus(s):
        bonus=s.salary*0.1
        print("bonus is:",bonus)
m=manager("sree",1000,"cse")
m.display()
m.annualsalary()
m.calculate_bonus()'''

'''class vehicle:
    def _init_(s,brand):
        s.brand=brand
    def start(s):
        print("car is start")
    def display_brand(s):
        print(f"brand is {s.brand}")
class car(vehicle):
    def _init_(s,brand,model):
        s.model=model
        super()._init_(brand)
    def drive(s):
        print("safe drive")
    def display_model(s):
        print(f"model is {s.model}")
class ec(car):
    def _init_(s,brand,model,battery):
        s.battery=battery
        super()._init_(brand,model)
    def charge(s):
        print("electric is charge")
    def display_battery(s):
        print("battery:",s.battery)
e=ec("nexon",2022,"amaron")
e.start()
e.display_brand()
e.drive()
e.display_model()
e.charge()
e.display_battery()'''

###heirarchical###

'''class bank:
    def details(s):
        print("a")
class saving(bank):
    def dis(s):
        print("b")
class zero(bank):
    def show(s):
        print("c")
z=zero()
s=saving()

z.show()
s.dis()

z.details()
s.dis()'''


'''class teacher:
    def _init_(s,subject,classes):
        s.subject=subject
        s.classes=classes
    def teach(s):
        print("teaching is good")
    def di(s):
        print(f"{s.classes}")
class researcher:
    def _init_(s,area,papers):
        s.area=area
        s.papers=papers
    def research(s):
        print("researcher")
    def dis(s):
        print(s.area)
class professor(teacher,researcher):
    def _init_(s,university,area,papers,subject,classes):
        s.university=university
        teacher._init_(s,area,papers)
        researcher._init_(s,subject,classes)
    def disp(s):
        print(f"{s.university}")
    def work(s):
        print("work")
p=professor("maths",2,24,"goodqualitypapers","mits")
p.teach()
p.di()
p.research()
p.dis()
p.work()
p.disp()'''

'''class employee:
    def _init_(s,name,salary):
        s.name=name
        s.salary=salary
    def display(s):
        print(s.name)
        print(s.salary)
class developer(employee):
    def _init_(s,name,salary,language):
        s.language=language
        super()._init_(name,salary)
    def dis(s):
        print(s.name)
        print(s.salary)
        print(s.language)
class tester(employee):
    def _init_(s,name,salary,tool):
        s.tool=tool
        super()._init_(name,salary)
    def disp(s):
         print(s.name)
         print(s.salary)
         print(s.tool)

t=tester("pandu",12400,"post")
d=developer("sree",15000,"checking")
t.disp()
t.display()'''


'''class college:
    def _init_(s,cname,cid):
        s.cname=cname
        s.cid=cid
     def dispplay(s):

         print(s.cname)
class student(college):
    def _init_(s,cname,cid,sname,rollno,department):
        s.rollno=rollno
        s.sname=sname
        s.department=department
        super()._init_(cname,cid)
    def show(s):
         print(s.cname)
         print(s.cid)
         print(s.sname)
         print(s.rollno)
class academics(student):'''


'''class college:
     def details(self):
         self.cname=input("enter college name:")
         self.cid=int(input("enter id:"))
class student(college):
    def show(self):
        self.sname=input("enter name:")
        self.sroll=int(input("enter rollno:"))
        self.sdept=input("enter dept:")
class academics(student):
    def dis(self):
        self.python=int(input("enter python marks:"))
        self.java=int(input("enter  java marks:"))
        self.c=int(input("enter c marks:"))
    def cal_total(self):
        self.total=self.python+self.java+self.c
class sports(student):
    def display(self):
        self.smarks=int(input("enter  sports marks:"))
class report(academics,sports):
    def cal_percentage(self):
        self.percentage=(self.total/150)*100
    def display_det(self):
        print("---------------")
        print("cname:",self.cname)
        print("cid:",self.cid)
        print("sname:",self.sname)
        print("sid:",self.sroll)
        print("dept:",self.sdept)
        print("python marks:",self.python)
        print("java marks:",self.java)
        print("c marks:",self.c)
        print("total marks:",self.total)
        print("sports marks:",self.smarks)
        print("percentage:",self.percentage)
r=report()
r.details()
r.show()
r.dis()
r.cal_total()
r.display()
r.cal_percentage()
r.display_det()'''

'''class vehicle:
     def _init_(s,brand):
          s.brand=brand
     def start(s):
          print("start")
     def d_brand(s):
          print(s.brand)
class car(vehicle):
     def _init_(s,brand,model):
          s.model=model
          super()._init_(brand)
     def drive(s):
          print("drive")
     def d_model(s):
          print(s.model)
class ec(car):
     def _init_(s,brand,model,battery):
          s.battery=battery
          super()._init_(brand,model)
     def charge(s):
          print("charge")
     def d_battery(s):
          print(s.battery)
v=ec("bmw",2,4)
v.start()
v.d_brand()
v.drive()
v.d_model()
v.charge()
v.d_battery()'''

'''class teacher:
     def _init_(s,subject,classes):
          s.subject=subject
          s.classes=classes
     def teach(s):
          print("teach is good")
     def di(s):
          print(s.subject)
class researcher:
     def _init_(s,area,papers):
          s.area=area
          s.papers=papers
     def research(s):
          print("researcheer")
     def dis(s):
          print(s.papers)
class professor(teacher,researcher):
     def  _init_(s,subject,classes,area,papers,university):
          s.university=university
          teacher._init_(s,subject,classes)
          researcher._init_(s,area,papers)
     def work(s):
          print("work")
     def disp(s):
          print(s.university)
p=professor("maths",2,5,"quality","mits")
p.teach()
p.di()
p.research()
p.dis()
p.work()
p.disp()'''

class employee:
     def __init__(s,name,salary):
          s.name=name
          s.salary=salary
     def display(s):
          print(s.name)
class developer(employee):
     def __init__(s,name,salary,language):
          s.language=language
          super().__init__(name,salary)
     def dis(s):
          print(s.name)
          print(s.language)
class tester(employee):
     def __init__(s,name,salary,test):
          s.test=test
          super().__init__(name,salary)
     def disp(s):
          print(s.salary)
          print(s.test)
t=tester("sree",2000,"post")
d=developer("hari",2890,"java")
t.display()
t.disp()
d.dis()
