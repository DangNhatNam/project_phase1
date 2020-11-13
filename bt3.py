#thuat toan
#thuat toan tim kiem tinh
#bai toan cho 1 mang a va mot so n, tim kietm xem co thuoc khong
a = [1, 4, 5, 6 ,7 , 9, 20, 10]
n =  5

#xay dung ham 
def findingNum(a, n):
    trueORfalse = False
    for item in a:
        if (item == n):
            trueORfalse = True
            break
    return trueORfalse
print(findingNum(a, n))
#tim kiem, nhi phan ap dung cho 1 mang da duoc sap xep
a = [1 , 3, 5, 6 , 8, 10, 12]
n = 5
#1. lay lam giua
#2. kiem tra n co bang a[mid] khong, neu bang thi tra ve true
#3. kiem tra neu n < a[mid] thi tim kiem trong khsn tu a[0] den a[mid -1]
#4. neu n > a[mid] thi tim kiem trong khoang tu a[mid + 1] den a[len(a) - 1]
def searchBinary(a, n):
    isRight = False
    mid = len(a) // 2
    for item in a:
        if (n == a[mid]):
            isRight = True
        elif (n < a[mid]): 
            i = 0 
            while i <= (mid - 1):
                if (n == a[i]):
                    isRight = True
                    break
                i += 1
        else:
            j = mid + 1
            while j <= len(a) - 1:
                if (n == a[j]):
                    isRight = True
                    break
                j += 1
        return isRight
print(searchBinary(a, n))

#BTVN: kiem tra 1 so co phai la so hoan hao khong, so hoan hao la so co tong = uoc so cua no -> vd: 6 = 3 + 2 + 1
#btn nhap vao 1 so n, kiem tra xem n co phai la so hoan hao khong
#bt2 in ra day so hoan hao tu 1 den 1000