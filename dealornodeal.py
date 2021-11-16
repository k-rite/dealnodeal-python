import random
#Setting briefcase prizes in prizeamt
prizeamt = [200,400,600,800,15000,20000,40000,60000,80000]
# we r using below list to print it index wise, it will also change it's value to open it as the cases are opened
cases = ["[CASE 1]","[CASE 2]","[CASE 3]","[CASE 4]","[CASE 5]","[CASE 6]","[CASE 7]","[CASE 8]","[CASE 9]"]
#randomised/shuffled the list, we will use list indexes as briefcase's inside prizes.
random.shuffle(prizeamt)

#made a empty list to avoid opening 1 briefcase more than one time, ref:def caseopening(s):
openedcases = []
def howtoplay():
    print("--->DEAL OR NO DEAL<---\n1.THERE ARE 9 briefcaseS.\n2.AFTER OPENING, EACH briefcaseS, IT HOLD CERTIAN PRIZE AMOUNT, BANKER WILL OFFER YOU A DEAL TO TAKE IT AND LEAVE THE GAME. YOU ARE FREE TO PICK NO DEAL AND PICK OTHER briefcase.\n3.YOU CAN OPEN IN TOTAL OF 4 briefcaseS ONLY. YOUR 4TH briefcase WILL AUOMATICALLY WILL BE A DEAL.")
    RESPONSE = int(input("Reply with 1, to start the game"))
    if RESPONSE == 1:
        mainscreen()
    else:
        howtoplay()
#made a simple homescreen which will take input to open briefcase, also some data validations and pushes it to chooseacase()
def mainscreen():
                                                                        #used len(openedcases) to limit upto 4 briefcase opening nd displaying in mainscreen
    print("""->WELCOME TO DEAL OR NO DEAL?<-        TOTAL CASES OPENED:""", len(openedcases),"""/4
                """,cases[0],cases[1],cases[2],"""
                """,cases[3],cases[4],cases[5],"""
                """,cases[6],cases[7],cases[8],"""
""")
    s = int(input("WHICH briefcase you want to open?"))
    chooseacase(s)
def chooseacase(s):
    if s == 1:
        print("This briefcase has: $", prizeamt[0])
        caseopening(0)
    elif s == 2:
        print("This briefcase has: $", prizeamt[1])
        caseopening(1)
    elif s == 3:
        print("This briefcase has: $", prizeamt[2])
        caseopening(2)
    elif s == 4:
        print("This briefcase has: $", prizeamt[3])
        caseopening(3)
    elif s == 5:
        print("This briefcase has: $", prizeamt[4])
        caseopening(4)
    elif s == 6:
        print("This briefcase has: $", prizeamt[5])
        caseopening(5)
    elif s == 7:
        print("This briefcase has: $", prizeamt[6])
        caseopening(6)
    elif s == 8:
        print("This briefcase has: $", prizeamt[7])
        caseopening(7)
    elif s == 9:
        print("This briefcase has: $", prizeamt[8])
        caseopening(8)
    else:
        print("Please enter just the briefcase number")
        mainscreen()
    
#Below, we ensure that briefcases are only opened once.Also changes cases value to "OPENED"
def caseopening(s):
    if s in openedcases:
        print("This briefcase is already opened, please open other briefcase")
        mainscreen()
    else:
        openedcases.append(s)
        cases.pop(s)
        x = "[OPENED]"
        cases.insert(s,x) 
        dealornodeal(s)
#bANKER Basic offer with basic maths, and last deal no deal options
def dealornodeal(s):
    if prizeamt[s] > 15001:
        offer = prizeamt[s] - prizeamt[s] / random.randint(2,5)
    else:
        offer = prizeamt[s] + prizeamt[s] / random.randint(1,15)
    print("The Banker is offering you: $",offer)
    dealnodeal = int(input("Respond with 1 if you want to make a DEAL, or 2 if you don't want to make a DEAL. \n(REMEMBER: You do have total of four briefcases to open.)"))
    if len(openedcases) == 4:
        print("YOU HAVE ALREADY OPENED 4 BRIEFCASES")
        print("Congratulations!!!, It's your fourth briefcase, and you won't be able to open any more. You are going home with $",offer)
    elif dealnodeal == 1:
        print("Congratulations!!!, You got a great deal!!! and you're on your way home with $",offer)
        end()
    elif dealnodeal == 2:
        print("Alrighty!!!, Bring-Back the briefcases and choose another..")
        mainscreen()      
        end()
    else:
        print('ENTER 1 OR 2 FOR DEAL OR NO DEAL ONLY')
        mainscreen()
#asking for replay and setting the game back up by fixing lists properly
def end():
    retry = int(input("Send 1 to restart the game and try your luck"))
    if retry == 1:
        cases.clear()
        #fixing case value with proper indexing
        for i in range(1,10):
            VALUE = f'[CASE {i}]'
            cases.append(VALUE)
        openedcases.clear()
        mainscreen()
    else: 
        print("THANK YOU FOR PARTICIPATING IN DEAL OR NO DEAL; WE WILL SEE YOU SOON.")
howtoplay()
#made with <3 by KRITESH
