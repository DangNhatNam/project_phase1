answer = 17 % 3
# % de lay so du -> kiem tra so tran le
print (answer)
# kiem tra so answer la chan thi in ta so chan, neu la so le thi in ra so le
b = 6 
if (b % 2 == 0):
    print ( "a la so chan ")
else:
    print ("a la so le")
# ** = binh phuong cua mot so
c = 4 
print (c ** 3)
# nhap vao chieu dai cua mot hinh chu nhat, in ra chu vi dien tich
d = 4
r = 6
print (" dien tich la " + str(d * r))
print (" chu vi la " + str((d + r )* 2))
# string -> chuoi
name = "nam"
print (name)
#thao tac chuoi
#cong chuoi
first_name = "bob"
last_name = "john"
# in ra full name
print ( first_name + ' ' + last_name)
#thao tac voi string
#lay chu cai dau tien cua Name
print (name[1])
print (len(name))
print (last_name[1:3])
print (name[-1])
print (first_name[0:])
# nhap vao chu "nghieng" , in ra dao nguoc
d = "nghieng"
print (len(d))
print (d[-1] + d[5] + d[4] + d[3] + d[2] + d[1] + d[0])
# bien la noi luu tru du lieu tam thoi, co 2 loai bien
#bien loai so -> viet bang chu hoa, khong gan duoc
#bien thuong -> gan duoc
PI = 3.14
print (PI)
PI = 6 
print (PI)
name = "abc"
name = "def"
print (name)
# array -> mang - tap hop nhieu tu co kieu do lieu giong hoac khac nhau
toA = ["nam", "tu", "phuong"]
toB = ["a", " b", "c"]
stt = [1, 2, 3, 4]
con = [1, 2, "phuong" , "nam"]
# in ra nhug nguoi thuoc to A
print (toA[0]+ " " + toA[1] + " " + toA[2])
#BTVN : su dung If, nhap vao mot so n, kiem tra so do chia het cho 3, in a "chia het cho 3", neu chia het cho 5, in ra "chia cho 5"
#neu chia het cho ca 3 va 5, in ra " chia het cho 3 va 5"
#n = 15
n = 7
# nếu <-> số âm, lớn hơn 0 và bé hơn 10 -> số bé hơn 100 lớn hơn 10 ->số trung bình và số lớn hơn 100 số lớn 
if n < 0:
    print (" số âm ")
elif n < 10:
    print (" số bé ")
elif n < 100:
    print ("số trung bình ")
else:
    print (" số lớn ")
# data type : number, string, list, (array), boolean (true or false), object -> đối tượng
# mot so phep toan: and, or, not 

if (n % 3 == 0 and n % 5 == 0):
    print ("chia het cho 3 va 5")
elif (n % 5 == 0):
    print ("chia het cho 5")
elif (n % 3 == 0):
    print ("chia het cho 3")
else:
    print ("Khong chia het cho 3 va 5")

for item in toA:
    print (item)

for i in range (5):
    print(i)
for i in range (1,5):
    print (i)
# nhap vao chuoi, dao chuoi
c = "hello Viet Nam"
# in day so tu 1 -> 10
i = 0
while (i <= 10 ):
    print (i)
    i = i + 1
print (i)

lc = len(c)
s = " "
i = lc - 1
while (i >= 0):
    s = s + c[i]
    i = i - 1
print(s)
# lc = 14, i = 13, 10 > 0 -> right, 5 = " " + "m" = "m", i = 12
# i = 12, 12 > 0 -> right, 5 = " " + "a" = "ma", i = 11
# tinh tong s = 1 + 2 + ... + 10
s = 0
i = 1
while (i <= 10):
    s = s + i 
    i = i + 1
print (s)

while (i <= 10 ):
    s += i # -> s = s + 1
    i += 1 # -> i = i + 1
print (s)    
# BTVN:  cho mot so n, tinh tong so chan tu 1 -> 100
# #tinh tong so le
# tinh tong sau = 1^2 + 2^2 + ... + 10^2

i = 1
s = 0
while ( i <= 5):
    s = s + i
    i = i + 2
print (s)

#tinh tong so chan, le 
s = 0 
i = 1
l = 0
while i <= 6:
    if (i % 2 ==0):
        s += i
    else:
        l += i
    i += 1
print (s)
print (l)

#nhap vao so n= 5
#tinh tong tu 1 den 4
#co 2 cach, dung if or dung break
s = 0 
i = 1
n = 5
while i <= n:
    s += i
    if (i == 4):
        break
    i += 1
    print (i)
print (s)
# funcction
def sum(a , b):
    return
print(sum(1, 2))