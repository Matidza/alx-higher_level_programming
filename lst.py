
def lst():
    string = input("What is the Elements (Space-seperated): ")
    lst = string.split()
    print(lst)

lst()

def interval():
    x = int(input("What is your x interval: "))
    y = int(input("What is your y inteerval: "))
    Var = []
    for i in range(x, y):
        Var.append(i)
    print(Var)

interval()


