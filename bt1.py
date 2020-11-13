#function
def sum(a , b):
    return a + b

print(sum(1, 2))
#ham co 2 loai, co gia tri ve va khong co gia tri ve
#ham thi co hoac ko co doi so truyen vao
#ham this chai khi goi
#vd ham khong co dai so

def soPi():
    return 3.14

pi = soPi()
print (pi)
#viet ham tinh tong s = 1 + 2 + 3 + n
def sumOfN(n): # n la bien local 
    s = 0 
    i = 0 
    while i <= n:
        s += i
        i += 1
    return s 
print (sumOfN(5))
#co 2 loai bien, la toan cuc(global) va bien dia phuong(local)
#bien local thi no chi hoat dong chong pham vi khai bao (vong lap hoac ham)
# con bien global this dung o khap noi trong chuong trinh
#viet ham tinh tong so chan 5 = 2 + 4 + 6 + 8 + ... + n
def evenSum (n):
    s = 0
    i = 0
    while i <= n:
        s += i
        i += 2
    return s
print (evenSum(6))
#btvn, ve so do khoi cac bai da hoc, va viet lai bang function 
#tinh tong cac chu so cua 1 so, co 3 chu so
#n = 123 = 6
def threeNumber (n): 
    a = n % 10
    b = (n // 10)% 10
    c = n // 100
    return a + b + c
print (threeNumber(345))

def threeNum (n):
    num = str(n)
    return int(num[0]) + int(num[1]) + int(num[2])
print (threeNum(976))

# def anyNumber (n):
#     num = str(n)
#     i = 0
#     s = 0
#     while i < len(num):
#         s = s + int(num[i])
#         i = i + 1
#     return s    

# key = "k"
# while key == "k":
#     print( "Please enter the number you want: ")
#     num = int(input())
#     print ("Sum of " + str(num) + " is")
#     print (anyNumber(num))
#     print ("press k to continue and any keywork to exit")
#     key = input()

#bt : in ra so chinh phuong tu 1 -> 50
def byTwo(n):
    i = 2
    while i < n:
        s = i**2
        if s > 50:
            break
        i += 1
        print (s)
print ("start printing")
byTwo(50)
#btvn: doc lai bai cu, tao mot file rieng xong code lai 
#nhap vao so n, in ra cac uoc so cua no (9 co uoc la 1 va 3, 9)
#nhap 2 so a,b , tim uoc chung lon nhat cua 2 so
#nhap vao 1 so co 3 chu so, in ra do co phai lam so doi xung khong (vd: 101, 303)
def numberMultiples(n):
     i = 1
     while i <= n:
        if (n % i == 0):
            print (i)
        i += 1
print (numberMultiples(9))

def equalNum(n):
    a = n // 100
    b = n % 10
    if a == b :
        print ("true")
    else:
        print ("false")
print (equalNum(656))

#nhap vao mot so n, kiem tra xem n co phai la so nguyen to khong

def primeNum(n):
    i = 2
    isPrime = True
    while (i < n//2):
        if n % i == 0:
            isPrime = False
            break 
        i += 1
    return isPrime
print (primeNum(8))

def abc(n):
    i = 2 
    while (i <= n) :
        if (primeNum(i)):
            print(i)
        i += 1
abc (100)

