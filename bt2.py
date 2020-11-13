name = ['nam', 'tuan', 'phuong']
score = [7, 8, 9]
subject = ['math', 'geography' , "Viet"]
#subject of hash = {key : value}
example = {'name' : "nam" , 'toan' : 7 , "ly" : 8, 'hoa' : 9}
#array if hash
atr = ({'name' : "nam" , 'toan' : 7 , "ly" : 8, 'hoa' : 9}, {'name' : "tuan" , 'toan' : 7 , "ly" : 9, 'hoa' : 9})
#in ra thong tin hoc sinh
for item in atr:
    print ("name : " + item['name'] + ', toan ' + str(item['toan']) + ' ly ' + str(item['ly']) + ' hoa ' + str(item['hoa']))

#nhap vao danh sach hoc sinh, gom cac truong, ten, toan, van
#input

a = []
key = "k"
while key == "k":
    name = input('please enter name: ')
    school = input ('please enter school name: ')
    toan = int(input('please enter math score: '))
    van = int(input('please enter literature: '))
    a.append({'school' : school , 'name': name , 'toan': toan , 'van': van })
    print ("please enter k to continue or any keystrokes to exit: ")
    key = input()


b = 0
c = 0
d = 0
for item in a:
    print('school : ' + item['school'] + ', name : ' + item['name'] + ', toan ' + str(item['toan']) + ' van ' + str(item['van']))
#tinh diem trung binh mon toan cua cac hoc sinh 
    b = b + item['toan']
    c += 1
b = b / c
print (b)
tinh diem trung binh cua tung hoc sinh 
b = []
for item in a:
    d = item['toan'] + item['van']
    d /= 2
    b.append(d)
print (b)