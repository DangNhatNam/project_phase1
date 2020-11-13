#BTVN: kiem tra 1 so co phai la so hoan hao khong, so hoan hao la so co tong = uoc so cua no -> vd: 6 = 3 + 2 + 1
#btn nhap vao 1 so n, kiem tra xem n co phai la so hoan hao khong
def isPerfectNumber (n):
    i = 1
    sum = 0
    while i <= n//2:
        if n % i == 0:
            sum = sum + i
        i = i + 1
    if n == sum:
        return True
    else:
        return False

print (isPerfectNumber(28))

#bt2 in ra day so hoan hao tu 1 den 1000
def printPerfectNumber (n):
    i = 1
    a = []
    while i <= n:
        if isPerfectNumber(i):
            a.append(i)
        i = i + 1
    return (a)
print (printPerfectNumber(1000))

