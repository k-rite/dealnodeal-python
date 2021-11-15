import random
#Setting breifcase prizes in prizeamt
prizeamt = [200,400,600,800,15000,20000,40000,60000,80000]

#randomised/shuffled the list, we will use list indexes as breifcase's inside prizes.
random.shuffle(prizeamt)

#made a empty list to avoid opening 1 breifcase more than one time, ref:def caseopening(s):
openedcases = []

#made a simple homescreen which will take input to open breifcase, also some data validations and pushes it to chooseacase()
def mainscreen():
                                                                        #used len(openedcases) to limit upto 4 breifcase opening nd displaying in mainscreen
    print("""->WELCOME TO DEAL OR NO DEAL?<-        TOTAL CASES OPENED:""", len(openedcases),"""/4
                [CASE 1]    [CASE 2]    [CASE 3]
                [CASE 4]    [CASE 5]    [CASE 6]
                [CASE 7]    [CASE 8]    [CASE 9]
""")
    s = int(input("WHICH breifcase you want to open?"))
    chooseacase(s)
    print(prizeamt[9])
def chooseacase(s):
    if s == 1:
        print("This breifcase has: $", prizeamt[0])
        caseopening(0)
    elif s == 2:
        print("This breifcase has: $", prizeamt[1])
        caseopening(1)
    elif s == 3:
        print("This breifcase has: $", prizeamt[2])
        caseopening(2)
    elif s == 4:
        print("This breifcase has: $", prizeamt[3])
        caseopening(3)
    elif s == 5:
        print("This breifcase has: $", prizeamt[4])
        caseopening(4)
    elif s == 6:
        print("This breifcase has: $", prizeamt[5])
        caseopening(5)
    elif s == 7:
        print("This breifcase has: $", prizeamt[6])
        caseopening(6)
    elif s == 8:
        print("This breifcase has: $", prizeamt[7])
        caseopening(7)
    elif s == 9:
        print("This breifcase has: $", prizeamt[8])
        caseopening(8)
    else:
        print("Please enter just the Breifcase number")
        mainscreen()
    

def caseopening(s):
    if s in openedcases:
        print("This breifcase is already opened, please open other breifcase")
        mainscreen()
    else:
        openedcases.append(s)
        dealornodeal(s)

	
def dealornodeal(s):
    if prizeamt[s] > 15001:
        offer = prizeamt[s] - prizeamt[s] / random.randint(2,5)
    else:
        offer = prizeamt[s] + prizeamt[s] / random.randint(1,15)
    print("The Bankers is offering you: $",offer)
    dealnodeal = int(input("Reply 1 to make the DEAL or 2 for NO DEAL.(REMEMBER: You can open 4 Breifcases in total."))
    if dealnodeal == 1:
        print("Congratulations!!!, You made a good deal!!! and You are going home with $",offer)
        end()
    elif dealnodeal == 2:
        print("Alrighty!!!, Let bring Breifcases back and pick other one.")
        mainscreen()
    elif len(openedcases) == 4:
        print("Congratulations!!!, It's your forth Breifcase, You cant open more and You are going home with $",offer)
        end()
    else:
        print('ENTER 1 OR 2 FOR DEAL OR NO DEAL ONLY')
        mainscreen()
def end():
    retry = int(input("Send 1 to restart the game"))
    if retry == 1:
        mainscreen()
        openedcases.clear()
mainscreen()