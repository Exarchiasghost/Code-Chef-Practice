import sys

happylist = list()

def isdivby5(num):
        if int(num)%5==0:
                return True
        else:
                return False

def withdraw(amount, account):
        if float(amount) >= float(account) or float(account) < 5.4:
                return float(account)
        else:
                if float(account) > 0.5:
                        while float(amount) > 0:
                                if isdivby5(float(amount)):
                                        account = float(account) - float(amount)
                                        account = float(account) - 0.5
                                        if float(amount)<10:
                                                return float(account) + 0.5
                                        else:
                                                return float(account)
                                        amount = 0
                                else:
                                        amount = float(amount) - 0.5
                

for line in sys.stdin:
        happylist = line.split()
        print("%.2f" % withdraw(happylist[0],happylist[1]))
        
