
print("1.p repeat \n2.p no-repeat \n3.c repeat \n4.c no-repeat \n5.multiply")

selection = input("Your selection: ")


def pr(n,r):
   print(int(n) ** int(r))

def pnr(n,r):
    print((fact(n)/(fact(n-r))))

def cr(n,r):
    print(fact(r+n-1)/(fact(r)*fact(n-r)))

def cnr(n,r):
    print(fact(n)/(fact(r)*fact(n-r)))

def mul(n,r):
    print(n*r)

def fact(n):
    if(n <= 1):
        return 1
    return n * (fact(n-1))

switcher = {
    1: pr,
    2: pnr,
    3: cr,
    4: cnr,
    5: mul
}

h = switcher.get(int(selection))
n = input("n: ")
r = input("r: ")

if r <= n:
    h(int(n),int(r))
else :
    print("wrong input! \nr is greater than n")



print(h)


# print(fact(5))

