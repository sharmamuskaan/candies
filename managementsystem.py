from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from sqlite3 import *
import requests
import bs4
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date
x=("Bradley Hand ITC",15,"bold")
today = date.today()
con=connect("CanD.db")
cursor=con.cursor()
cursor.execute("SELECT id FROM customer")
resultte = cursor.fetchall()
ed= [i[0] for i in resultte]

def f1():
r.withdraw()
addst.deiconify()
def f2():
addst.withdraw()
r.deiconify()
def f3():
r.withdraw()
viewst.deiconify()
s1=Label(viewst,text="ID",width=13,fg='green')
s2=Label(viewst,text="Name",width=13,fg='green')
s3=Label(viewst,text="Order Placed",width=13,fg='green')
s4=Label(viewst,text="Amount",width=13,fg='green')
s1.grid(row=1,column=2)
s2.grid(row=1,column=3)
s3.grid(row=1,column=4)
s4.grid(row=1,column=5)
con=None
try:
con=connect("CanD.db")
cursor=con.cursor()
cursor.execute("select * from customer")
ii=0
for customer in cursor:
for j in range(len(customer)):
e=Entry(viewst,width=15,fg='green')
e.grid(row=ii+2, column=j+2)
e.insert(END, customer[j])
ii=ii+1
'''rec=cursor.fetchall()
print_rec=""
i=2
for re in rec:
print_rec=re
lab=Label(viewst,text=print_rec)
lab.grid(row=i, column=2, columnspan=2)
i=i+1'''

except Exception as e:
showerror("failure ","updation issue "+str(e))
finally:
if con is not None:
con.close()

def f4():
viewst.withdraw()
r.deiconify()
def f5():
con=None
try:
con=connect("CanD.db")
cursor=con.cursor()
sql="insert into customer values ('%d','%s','%s','%d')"
iddd=int(addst_entid.get())
name=addst_entname.get()
order=addst_entorder.get()
cost=int(addst_entcost.get())
ed.append(iddd)
if iddd<0 or len(name)<2 or cost<10 or len(order)<2:
showerror("issue","one of the following conditions is voilated: id < 0, length of name < 2, cost < 10 or length of order < 2")
else:
cursor.execute(sql %(iddd,name,order,cost))
con.commit()
showinfo("sucess","record inserted")
except ValueError as ve:
    showerror("issue",'No ID provided or no Amount provided')
except Exception as e:
con.rollback()
showerror("failed ","issue "+str(e))
finally:
if con is not None:
con.close()

def f8():
con=None
try:
con=connect("CanD.db")
cursor=con.cursor()
i=int(upeid.get())
n=upename.get()
flag=0
for aq in ed:
if aq==i:
flag=1
else:
pass
if i<0 or len(n)<2 or flag==0:
showerror("issue","one of the following conditions is voilated: id < 0, length of name <2 or ID does not exists")
else:
cursor.execute("select * from customer")
data=cursor.fetchall()
for d in data:
if d[0]==i:
sql="UPDATE customer SET name=('%s') WHERE id =('%d')"
cursor.execute(sql %(n,i))
con.commit()
showinfo("sucess","record updated")
except ValueError as ve:
    showerror("issue",'No ID provided')
except Exception as e:
con.rollback()
showerror("failed ","updation issue "+str(e))
finally:
if con is not None:
con.close()
def f9():
up.withdraw()
r.deiconify()
def f6():
r.withdraw()
up.deiconify()
def f7():
r.withdraw()
u.deiconify()
def f10():
con=None
try:
con=connect("CanD.db")
cursor=con.cursor()
i=int(ueid.get())
o=ueorder.get()
flagg=0
for aq in ed:
if aq==i:
flagg=1
else:
pass
if i<0 or len(o)<2 or flagg==0:
showerror(" ","one of the following conditions is voilated: id<0, length of order < 2 or ID does not exists")
else:
cursor.execute("select * from customer")
data=cursor.fetchall()
for d in data:
if d[0]==i:
sql="UPDATE customer SET order_placed=('%s') WHERE id=('%d')"
cursor.execute(sql %(o,i))
con.commit()
showinfo("sucess","record updated")
except ValueError as ve:
    showerror("issue",'No ID provided')

except Exception as e:
con.rollback()
showerror("failed","updation issue"+str(e))
finally:
if con is not None:
con.close()
def f11():
u.withdraw()
r.deiconify()
def f12():
r.withdraw()
d1.deiconify()
def f17():
r.withdraw()
u1.deiconify()
def f13():
con=None
try:
con=connect("CanD.db")
cursor=con.cursor()
id=int(eee.get())
flaagg=0
for aq in ed:
if aq==id:
flaagg=1
else:
pass

if flaagg==0:
showerror("issue","condition is voilated:ID does not exists")
else:
sql="delete from customer where id=('%d')"
cursor.execute(sql %(id))
con.commit()
showinfo("sucess","record deleted")
ed.remove(id)
except ValueError as ve:
    showerror("issue",'No ID provided')
except Exception as e:
con.rollback()
showerror("failed ","issue "+str(e))
finally:
if con is not None:
con.close()
def f14():
d1.withdraw()
r.deiconify()
def f15():
con=None
try:
con=connect("CanD.db")
cursor=con.cursor()
i=int(u1eid.get())
o=int(u1eorder.get())
flaag=0
for aq in ed:
if aq==i:
flaag=1
else:
pass

if i<0 or o<10 or flaag==0:
showerror("issue","one of the following conditions is voilated: id < 0, cost < 10 or ID does not exists")
else:
cursor.execute("select * from customer")
data=cursor.fetchall()
for d in data:
if d[0]==i:
sql="UPDATE customer SET cost=('%d') WHERE id=('%d')"
cursor.execute(sql %(o,i))
con.commit()
showinfo("sucess","record updated")
except ValueError as ve:
    showerror("issue",'No ID provided or no Amount provided')

except Exception as e:
con.rollback()
showerror("failed","updation issue"+str(e))
finally:
if con is not None:
con.close()
def f16():
u1.withdraw()
r.deiconify()
def f18():
try:
con=connect("CanD.db")
cursor=con.cursor()
cursor.execute("SELECT name FROM customer")
result = cursor.fetchall()
final_result = [i[0] for i in result]
except Exception as e:
showerror("issue",e)
try:
con=connect("CanD.db")
cursor=con.cursor()
cursor.execute("SELECT cost FROM customer")
resultt = cursor.fetchall()
final_resultt = [i[0] for i in resultt]
except Exception as e:
showerror("issue",e)
plt.bar(final_result,final_resultt,linewidth=3,label="Bill in rupees")
plt.grid(True)
plt.legend(shadow=True,loc="upper left")
plt.xlabel("Name")
plt.ylabel("Amount")
plt.show()


r=Tk()
r.title("CanD Shoppin!")
r.geometry("600x640+10+10")
r.configure(bg='blue')
btnadd=Button(r,text="Add",font=x,width=10,command=f1)
btnview=Button(r,text="View",font=x,width=10,command=f3)
b3=Button(r,text="Update Name",font=x,width=10,command=f6)
b4=Button(r,text="Update Order Placed",font=x,width=15,command=f7)
b6=Button(r,text="Update Cost",font=x,width=10,command=f17)
b5=Button(r,text="Delete Record",font=x,width=10,command=f12)
b7=Button(r,text="Data Visualisation",font=x,width=15,command=f18)
q=ScrolledText(r,width=45,height=2,font=x)
loc=ScrolledText(r,width=40,height=0.5,font=x)
tt=ScrolledText(r,width=40,height=0.5,font=x)
btnadd.pack(pady=10)
btnview.pack(pady=10)
b3.pack(pady=10)
b4.pack(pady=10)
b6.pack(pady=10)
b5.pack(pady=10)
b7.pack(pady=10)
q.pack(pady=10)
loc.pack(pady=10)
tt.pack(pady=10)

try:
webadd="https://www.brainyquote.com/quote_of_the_day"
res=requests.get(webadd)
data=bs4.BeautifulSoup(res.text,"html.parser")
info=data.find("img",{"class":"p-qotd"})
quote=info['alt']
q.insert(INSERT,"quote of "+str(today)+" is: "+quote)
except Exception as e:
print("issue is : ",e)
try:
end_point="http://ipinfo.io/"
res=requests.get(end_point)
#print(res)
data=res.json()
#print(data)
city_name=data['city']
#print("city is ",city_name)
coordinates=data["loc"]
list=coordinates.split(",")
ll1=list[0]
ll2=list[1]
loc.insert(INSERT,"City: "+city_name+", Co-ordinates:"+ll1+", "+ll2)
except Exception as e:
print("issue ",e)

try:
a1="http://api.openweathermap.org/data/2.5/weather?q=Mumbai&units=metric&APPID=2d7262c30d4b342ab6ec3154eca6b2ea"
website_address=a1
res=requests.get(website_address)
data=res.json()
mainn=data['main']
t=mainn['temp']
tt.insert(INSERT,"temperature is: "+str(t)+" degree celsius")
except Exception as e:
print("issue: ",e)

addst=Toplevel(Tk())
addst.title("Add Customer")
addst.geometry("500x600+10+10")
addst.configure(bg='#afeeee')
addst.withdraw()
addst_lblid=Label(addst,text="Enter ID",font=x)
addst_entid=Entry(addst,bd=5,font=x)
addst_lblname=Label(addst,text="Enter Name",font=x)
addst_entname=Entry(addst,bd=5,font=x)
addst_lblorder=Label(addst,text="Enter Order Placed",font=x)
addst_entorder=Entry(addst,bd=5,font=x)
addst_lblcost=Label(addst,text="Enter Amount",font=x)
addst_entcost=Entry(addst,bd=5,font=x)
addst_btnsave=Button(addst,text="SAVE",font=x,command=f5)
addst_btnback=Button(addst,text="BACK",font=x,command=f2)

addst_lblid.pack(pady=10)
addst_entid.pack(pady=10)
addst_lblname.pack(pady=10)
addst_entname.pack(pady=10)
addst_lblorder.pack(pady=10)
addst_entorder.pack(pady=10)
addst_lblcost.pack(pady=10)
addst_entcost.pack(pady=10)
addst_btnsave.pack(pady=10)
addst_btnback.pack(pady=10)

viewst=Toplevel(Tk())
viewst.configure(bg='lightgreen')
viewst.title("View Customer Data")
viewst.geometry("500x500+10+10")
viewst_back=Button(viewst,text="BACK",font=x,command=f4)
viewst_back.grid(row=1, column=6)
viewst.withdraw()

up=Toplevel(Tk())
up.title("Update Customer Name")
up.geometry("500x500+10+10")
up.configure(bg='red')
upid=Label(up,text="Enter ID",font=x)
upeid=Entry(up,bd=5,font=x)
upname=Label(up,text="Enter Name",font=x)
upename=Entry(up,bd=5,font=x)
up_b1=Button(up,text="SAVE",font=x,command=f8)
up_b2=Button(up,text="BACK",font=x,command=f9)

upid.pack(pady=10)
upeid.pack(pady=10)
upname.pack(pady=10)
upename.pack(pady=10)
up_b1.pack(pady=10)
up_b2.pack(pady=10)
up.withdraw()

u=Toplevel(Tk())
u.configure(bg='pink')
u.title("Update customer Order")
u.geometry("500x500+10+10")
uid=Label(u,text="Enter ID",font=x)
ueid=Entry(u,bd=5,font=x)
uorder=Label(u,text="Enter Updated Order",font=x)
ueorder=Entry(u,bd=5,font=x)
u_b1=Button(u,text="SAVE",font=x,command=f10)
u_b2=Button(u,text="BACK",font=x,command=f11)

uid.pack(pady=10)
ueid.pack(pady=10)
uorder.pack(pady=10)
ueorder.pack(pady=10)
u_b1.pack(pady=10)
u_b2.pack(pady=10)
u.withdraw()

u1=Toplevel(Tk())
u1.configure(bg='yellow')
u1.title("Update Amount")
u1.geometry("500x500+10+10")
u1id=Label(u1,text="Enter ID",font=x)
u1eid=Entry(u1,bd=5,font=x)
u1order=Label(u1,text="Enter Updated Cost",font=x)
u1eorder=Entry(u1,bd=5,font=x)
u1_b1=Button(u1,text="SAVE",font=x,command=f15)
u1_b2=Button(u1,text="BACK",font=x,command=f16)

u1id.pack(pady=10)
u1eid.pack(pady=10)
u1order.pack(pady=10)
u1eorder.pack(pady=10)
u1_b1.pack(pady=10)
u1_b2.pack(pady=10)
u1.withdraw()

d1=Toplevel(Tk())
d1.configure(bg='black')
d1.title("Delete record")
d1.geometry("500x500+10+10")
lll=Label(d1,text="Enter ID",font=x)
eee=Entry(d1,bd=5,font=x)
ddd=Button(d1,text="DELETE",font=x,command=f13)
bbb=Button(d1,text="BACK",font=x,command=f14)

lll.pack(pady=10)
eee.pack(pady=10)
ddd.pack(pady=10)
bbb.pack(pady=10)
d1.withdraw()

r.mainloop()