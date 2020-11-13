#btvn: tinh tong s = 1/2 + 1/3 + 1/4 + 1/n
def division(a):
    n = 1
    s = 0
    while n <= a:
        s += 1/n
        n += 1
    return s
print (division(9))

#s = 1.2 + 2.3 + 3.4 + 4.5 + ... + (n-1). n
def multiplying(a):
    i = 1
    b = 0
    c = 0
    d = 0
    while b < a:
        d = b*i
        b = i
        i += 1
        c += d
    return c
print (multiplying(3))
def multiple (a):
    s = 0 
    i = 1
    while i < a:
        s += i*(i+1)
        i += 1
    return s 
print (multiple(3))

#s = 1.3 + 3.5 + 5.7 +...+ (n-1). n
def oddnum(a):
    s = 0
    i = 1
    while i < a:
        s += i*(i+2)
        i += 2
    return s
print (oddnum(5))

#viet ham kiem tra n co phai so nguyen to 
def primnum(a):
    trueF= True 
    i = 2
    while i < a:
        if a % i == 0:
            trueF = False
            break
        i += 1
    if a <= 1:
        trueF = False
    return trueF
print (primnum(277))
# in ra cac so nguyen to tu 1 -> 100
i = 1
while i < 100:
    if primnum(i):
        print (i)
    i += 1

# arr = [1,2,3,4,6]
# i = 0
# while i < len(arr):
#     print (arr[i])
#     i += 1


#kiem tra 1 so co phai la so chinh phuong khong (true, false)
#in ra cac so chinh phuong 1 -> 100