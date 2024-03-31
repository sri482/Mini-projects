from datetime import datetime
name=input("enter your name:")
list='''
Rice             RS 20/- kg
Sugar            Rs 44/- kg
Wheat            Rs 40/- kg
Ground nut oil   Rs 200/- kg
Paneer           Rs 120/- kg
Boost            Rs 220/- kg
Toothpaste       Rs 89/- kg
'''
price=0
pricelist=[]
totalprice=0
finalprice=0
ilist=[]
qlist=[]
plist=[]

#prices for items
items={'Rice':20,
       'Sugar':44,
       'Wheat':40,
       'Ground nut oil':200,
       'Paneer':120,
       'Boost':220,
       'Tooth':89}
option=int(input('to view the list of items press 1'))
if option==1:
       print(list)
else:
       print(list)
for i in range(len(items)):
       inp1=int(input('if you want to buy press 1 or 2 for exit'))
       if inp1==2:
              break
       if inp1==1:
              item=input("enter your items")
              quantity=int(input('enter qty:'))
              if item in items.keys():
                     price=quantity*(items[item])
                     pricelist.append((item,quantity,items,price))
                     totalprice+=price
                     pri=quantity*(items[item])
                     ilist.append(item)
                     qlist.append(quantity)
                     plist.append(price)
                     gst=(totalprice*10)/100
                     finalamount=gst+totalprice
              else:
                     print("sorry this item is not availble")
       else:
              print("you entered wrong number")
       inp=input("can i bill the items yes or no:")
       if inp=='yes':
              pass
       if finalamount !=0:
              print(20*"=","sri super market",20*"=")
              print(25*" ",'BOYIDI',25*" ")
              print("name:",name,15*" ","date:",datetime.now())
              print(58*"-")
              print('s no',5*" ",'items',5*" ",'quantity',8*" ",'cost',4*" ", 'price')
              for i in range(len(pricelist)):
                     print(i,8*' ',ilist[i],8*' ',qlist[i],12*' ',items[item], 7*" ",plist[i])
              print(58*"-")
              print("GST",32*" ","Total amount: Rs",totalprice)
              g=gst/2
              f=gst/2
              print(5*" ","CGST 5%",37*" ",g)
              print(5 * " ", "SGST 5%", 37 * " ", f)
              print(60*"-")
              print(37*" ","Finalamount: Rs",finalamount)
              print(60 * "-")
              print(20*" ","Thanks for visiting")
              print(60 * "-")

