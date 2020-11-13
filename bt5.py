# sap xep mot mang tang giam dan 
# tim so lan nhat, nho nhat trong mot mang 
def findMax (a):
    b = a[0]
    i = 1 
    while i < len(a):
        if a[i] > b:
            b = a[i]
        i = i + 1
    return b
a = [1, 2, 3, 11, 8, 7 , 5]
print (findMax(a))

def findMin (n):
    b = n[0]
    i = 1
    while i < len(n):
        if n[i] < b:
            b = n[i]
        i = i + 1
    return b
n = [2, 3, 11, 8, 7 , 5, 1]
print (findMin(n))

#btvn in chuoi fibonacci tu 1 den 1000

