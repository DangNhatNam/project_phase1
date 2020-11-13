#kiem tra 1 so co phai la so chinh phuong khong (true, false)
#in ra cac so chinh phuong 1 -> 100

#quan ly danh sach hoc sinh khoi 8
#viet chuong chinh nhap thong tin hoc sinh theo lop
#thong tin bao gom: lop hoc, ten hoc sinh, diem toan ,van, anh

class8B = []
class8I = []
class8S = []
class8V = []
key = 'o'


while key == 'o':
    name = input("enter name: ")
    classes = input('enter class: ')
    math = input('enter math score: ')
    literature = input('enter literature score: ')
    english = input('enter English score: ')
    obj = {'name': name , 'math' : math , 'literature' : literature , "english" : english}

    if (classes == '8b') or (classes == '8B'):
        class8B.append(obj)
    elif (classes == '8i') or (classes == '8I'):
        class8I.append(obj)
    elif (classes == '8s') or (classes == '8S'):
        class8S.append(obj)
    elif (classes == '8v') or (classes == '8V'):
        class8V.append(obj)

    key = input("press O to continue and any other keystroke to exit: ")
print ('class8B: ' , class8B)
print ('class8I: ' , class8I)
print ('class8S: ' , class8S)
print ('class8V: ' , class8V)

for item in class8B:
    avg = (int(item['math']) + int(item['literature']) + int(item['english'])) /3
    print ("average of", item['name'], avg)
for item in class8I:
    avg = (int(item['math']) + int(item['literature']) + int(item['english'])) /3
    print ("average of", item['name'], avg)
for item in class8S:
    avg = (int(item['math']) + int(item['literature']) + int(item['english'])) /3
    print ("average of", item['name'], avg)
for item in class8I:
    avg = (int(item['math']) + int(item['literature']) + int(item['english'])) /3
    print ("average of", item['name'], avg)

#tinh trung binh theo lop
#tinh trung binh theo khoi
