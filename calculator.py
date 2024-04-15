###method 1

# while True:
#     a=input("enter first no")
#     b=input("enter second no")
#     m=input("enter operand symbol")
#     def cal(d, e,m):
#         if a==float or int and b==int or float:
#             if m == "+":
#                 print(int(d)+int(e))
#             elif m == "-":
#                 print(int(d)-int(e))
#             elif m=="/":
#                 print(int(d)/int(e))
#             elif m=="*":
#                 print(int(d)*int(e))
#             elif m=="%":
#                 print(int(d)%int(e))
#             else:
#                 return "invalid operator"
#         elif a!=int or float and b!=int or float:
#             return "invalid value"
#     cal(a,b,m)



###method 2 using oops concept

# while True:
#     a=float(input("enter first no"))
#     b=float(input("enter second no"))
#     m=input("enter operand symbol")
#     try:
#         class obj():
#             def __init__(self,a,b):
#                 self.a=a
#                 self.b=b
#             def add(self):
#                 print(self.a+self.b)
#             def sub(self):
#                 print(self.a-self.b)
#             def div(self):
#                 print(self.a/self.b)
#             def mul(self):
#                 print(self.a/self.b)
#             def mod(self):
#                 print(self.a%self.b)
#         g = obj(a, b)
#         if m=="+":
#             g.add()
#         elif m=="-":
#             g.sub()
#         elif m=="*":
#             g.mul()
#         elif m=="/":
#             g.div()
#         elif m=="%":
#             g.mod()
#         else:
#             print("invalid operator")
#     except Exception as r:
#         print("error",r)
