from datetime import datetime
a = ('''
          1) Mini statement
          2) Money withdrawl
          3) password change''')
amount = 1000
print("please insert your card")

pin=1234
while True:
    pas=int(input("please enter your pin"))
    x = input("enter your user id")
    if pas==pin:
        print("Hi",x, "HOW ARE YOU",
                    a)
        while True:

            b=int(input("please enter option"))
            if b==1:
                print("your currecnt balance is ",amount)
            elif b==2:
                c=int(input("enter amount"))
                def amt():
                    if c<=amount:
                        print(c)
                    else:
                        pass
                if c<=amount:
                    print("           *****ICICI BANK*****   ")
                    print("                  LINGALA           ")
                    print("Date:",8*" ", 'ATM NO')
                    print(datetime.now(),"SR11I2207")
                    print("CARD NO.xxxxxxxxx6291-002")
                    print("TO YOUR BALANCES.CALL TOLLFREE ON")
                    print("1800-273-3333 FROM YOUR MOBILE AND")
                    print("GET YOUR BALANCE INSTANTLY")
                    print("s. no    TRAN       AMOUNT")
                    print("RECORD NO.    5166")
                    print("AMOUNT WITHDRAWL       ")
                    print(amt())
                    print("LEDGER BAL     " "RS.",amount)
                    print("avilble        "  "RS",amount-c)

                    print(''' please COLLECT YOUR CASH
                          Thank you
                          visit again''')
                else:
                    print("insufficient balance")
            elif b==3:
                v=int(input("please enter new pin"))
                pin=v
                print("your password has been success fully changed")
            elif b>3 or b<1:
                print("in correct option")
            else:
                break

    else:
        print("Incorrect pin. please try again\n")
