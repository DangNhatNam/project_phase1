# - Project: Quản lý bán hàng
# Thông tin: Nhà sản xuất, danh mục sản phẩm, sản phẩm
# + Nhà sản xuất: Số thứ tự, Tên nhà sản xuất, địa chỉ, phone: owner = [{ 'id': 1, 'name': 'Sam sung', 'address': 'viet nam', 'phone': '0120677773'}]
# + Danh mục:  Số thư tự, Tên danh mục, miêu tả: ví dụ: categories = [{'id': 1, 'name': 'Thời trang', 'description': 'Thời trang cho tre em'}]
# + Sản phẩm: Số thứ tự, Tên sản phẩm, giá, miêu tả, số lượng hàng còn, nhà sản xuất nào, danh mục nào, ảnh: 
# products = [{'id': 1, 'name': 'giay nam', 'description': ' giay cho gioi tre', 'price': 200000, 'owner_id': 1, 'category_id': 1}]

# - Phase 1: 
#  + Nhập xuất danh mục bán hàng
#  + Lưu vào file, txt, excel
#  + Tao class, tao object	
# - Phase 2: 
#  + Tạo phần mềm, xuất nhập 
#  + Lưu dữ liệu vào file đọc ra
#  + Lưu dữ liệu vào sql

continuekey = "k"
i = 1
owner = []
catergories = []
products = []

while continuekey == "k":
    name = input("who's the owner?: ")
    iden = i
    address = input("where's the product from?: ")
    phone = input("what's your phone number?: ")
    obj = {'name' : name , "ID": iden , "address": address , "contact Number": phone}
    owner.append(obj)
    i += 1
    continuekey = input("press k to continue, press any other key to continue: ")


continuekey = "k"
i = 1
while continuekey == "k":
    id = i
    name = input("what's catergory?: ")
    description = input("description: ")
    obj = {'ID' : id , 'catergory' : name , 'description' : description}
    catergories.append(obj)
    i += 1
    continuekey = input("press k to continue, press any other key to continue: ")


continuekey = "k"
i = 1
while continuekey == "k":
    identity = i
    name = input("what's the product name?: ")
    description = input("what's the product description?: ")
    price = input("pricing: ")
    obj = {"ID" : identity , "description" : description , "pricing" : price , "owner_ID" : owner[iden], "catergory_ID" : catergories[id]}
    products.append(obj)
    i += 1
    continuekey = input("press k to continue, press any other key to continue: ")


print (owner) and (catergories) and (products)