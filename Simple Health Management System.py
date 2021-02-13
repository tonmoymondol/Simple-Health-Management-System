import datetime
def gettime():
    return datetime.datetime.now()
def take(k):
    if k==1:
        c=int(input("Enter 1 for exercise and 2 for food"))
        if(c==1):
            value=input("Please insert your input\n")
            with open("tonmoy-exercise.txt","a") as op:
                op.write(str([str(gettime())])+": "+value+"\n")
            print("You've successfully Inserted The Data")
        elif(c==2):
            value = input("Please insert your input\n")
            with open("tonmoy-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("You've successfully Inserted The Data")
    elif(k==2):
        c = int(input("Enter 1 for exercise and 2 for food"))
        if (c == 1):
            value = input("Please insert your input\n")
            with open("joy-exercise.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("You've successfully Inserted The Data")
        elif (c == 2):
            value = input("type here\n")
            with open("joy-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("You've successfully Inserted The Data")
    elif(k==3):
        c = int(input("enter 1 for exercise and 2 for food"))
        if (c == 1):
            value = input("Please insert your input\n")
            with open("abir-exercise.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("You've successfully Inserted The Data")
        elif (c == 2):
            value = input("Please insert your input\n")
            with open("abir-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("You've successfully Inserted The Data")
    else:
        print("Please enter valid input (1(tonmoy),2(joy),3(abir)")
def retrieve(k):
    if k==1:
        c=int(input("Enter 1 for exercise and 2 for food"))
        if(c==1):
            with open("tonmoy-exercise.txt") as op:
                for i in op:
                    print(i,end="")
        elif(c==2):
            with open("tonmoy-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif(k==2):
        c = int(input("Enter 1 for exercise and 2 for food"))
        if (c == 1):
            with open("joy-exercise.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("joy-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif(k==3):
        c = int(input("Enter 1 for exercise and 2 for food "))
        if (c == 1):
            with open("abir-exercise.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("abir-food.txt") as op:
                for i in op:
                    print(i, end="")
    else:
        print("Please enter valid input (tonmoy,joy,abir)")
print("Simple Health Management System: ")
a=int(input("Press 1 for insert the value and 2 for retrieve "))

if a==1:
    b = int(input("Press 1 for tonmoy 2 for joy 3 for abir "))
    take(b)
else:
    b = int(input("press 1 for tonmoy 2 for joy 3 for abir "))
    retrieve(b)