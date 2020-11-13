#btvn in chuoi fibonacci tu 1 den 1000
def fibonacciSequence (n):
    n1, n2 = 0, 1
    count = 0
    if n <= 0:
        print ("please enter a postive intiger: ")
    else:
        print ("Fibonacci sequence:")
    while count < n:
        print (n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth 
        count += 1
print (fibonacciSequence(10))

#nhap vao mot so kiem tra xem co phai so chinh phuong khong?

def squareRoot(n):
    i = 0
    tfalse = False
    while i < n:
        if i*i == n:
            tfalse = True
            break
        i += 1
    return tfalse
print (squareRoot(9))

#s = 1*1 + 2*2 + 3*3 +... + n*n

def total(n):
    i = 1
    a = 0
    while i <= n:
        a = a + i ** 2
        i += 1
    return a
print (total(2))

# tinh tong so let tu 1 den n

def oddNum(n):
    sum = 0
    i = 0
    while i <= n:
        if i % 2 != 0:
            sum = sum + i
        i += 1
    return sum
print (oddNum(7))

def evenNum(n):
    i = 0
    s = 0
    while i <= n:
        if i % n == 0:
            s = s + i
    i += 1
print (evenNum(8))

#btvn: tinh tong s = 1/2 + 1/3 + 1/4 + 1/n

#s = 1.2 + 2.3 + 3.4 + 4.5 + ... + (n-1). n

#viet ham kiem tra n co phai so nguyen to 

# in ra cac so nguyen to tu 1 -> 100