import json

item_list={
    "1100":{"Name":"Pepsi","Expiry_date":"25/01/2025","Price":10,"Quantity":60,"Vegan":True},
    "1101":{"Name":"Coke","Expiry_date":"23/01/2025","Price":10,"Quantity":30,"Vegan":True},
    "1102":{"Name":"Mountain Dew","Expiry_date":"15/06/2025","Price":100,"Quantity":65,"Vegan":False},
    "1103":{"Name":"Pepsi suger free","Expiry_date":"15/06/2025","Price":100,"Quantity":65,"Vegan":False},
    "1104":{"Name":"Lays","Expiry_date":"17/01/2025","Price":20,"Quantity":110,"Vegan":True},
    "1105":{"Name":"Kurkure","Expiry_date":"31/08/2025","Price":60,"Quantity":200,"Vegan":False},
    "1106":{"Name":"Nachos","Expiry_date":"15/06/2025","Price":100,"Quantity":65,"Vegan":False},
    "1107":{"Name":"Nachos Blue","Expiry_date":"08/08/2025","Price":30,"Quantity":700,"Vegan":True},
    "1108":{"Name":"Nachos Green","Expiry_date":"15/06/2025","Price":100,"Quantity":65,"Vegan":False},
    "1109":{"Name":"Nachos Chilli","Expiry_date":"15/06/2025","Price":100,"Quantity":65,"Vegan":False},
    "1110":{"Name":"Perk","Expiry_date":"25/10/2025","Price":30,"Quantity":600,"Vegan":True},
    "1111":{"Name":"Cadberry","Expiry_date":"15/06/2025","Price":50,"Quantity":70,"Vegan":True},
    "1112":{"Name":"Oreo","Expiry_date":"15/06/2025","Price":100,"Quantity":65,"Vegan":False},
    "1113":{"Name":"Bournvita","Expiry_date":"15/06/2025","Price":100,"Quantity":65,"Vegan":False},
    "1114":{"Name":"Butter Biscuit","Expiry_date":"15/06/2025","Price":100,"Quantity":65,"Vegan":False},
    "1115":{"Name":"Marie Gold Biscuit","Expiry_date":"15/06/2025","Price":100,"Quantity":65,"Vegan":False},
    "1116":{"Name":"Midnight Snack","Expiry_date":"15/06/2025","Price":100,"Quantity":65,"Vegan":False},
    "1117":{"Name":"Oreo","Expiry_date":"15/06/2025","Price":100,"Quantity":65,"Vegan":False},
    "1118":{"Name":"Oreo Extra creamy","Expiry_date":"15/06/2025","Price":100,"Quantity":65,"Vegan":False},
    "1119":{"Name":"Oreo Thin crust","Expiry_date":"15/06/2025","Price":100,"Quantity":65,"Vegan":False},
    "1120":{"Name":"Son Papdi","Expiry_date":"15/06/2025","Price":100,"Quantity":65,"Vegan":False},
    "1121":{"Name":"Red Chilli Sauce","Expiry_date":"15/06/2025","Price":100,"Quantity":65,"Vegan":True},
    "1122":{"Name":"Green Chilli Sauce","Expiry_date":"15/06/2025","Price":100,"Quantity":65,"Vegan":True},
    "1123":{"Name":"Soya Sauce","Expiry_date":"15/06/2025","Price":750,"Quantity":65,"Vegan":True},
    "1124":{"Name":"Mustard Oil","Expiry_date":"15/06/2025","Price":100,"Quantity":65,"Vegan":True},
    "1125":{"Name":"Refine oil","Expiry_date":"15/06/2025","Price":100,"Quantity":65,"Vegan":True},
    "1126":{"Name":"Wafer","Expiry_date":"15/06/2025","Price":50,"Quantity":65,"Vegan":False},
    "1127":{"Name":"Vanilla Ice Cream","Expiry_date":"15/06/2025","Price":400,"Quantity":65,"Vegan":False},
    "1128":{"Name":"Mango ice cream","Expiry_date":"15/06/2025","Price":400,"Quantity":65,"Vegan":False},
    "1129":{"Name":"choco bar","Expiry_date":"08/08/2025","Price":30,"Quantity":700,"Vegan":True},
    "1130":{"Name":"Cold Ice cream","Expiry_date":"15/06/2025","Price":30,"Quantity":65,"Vegan":False},
    "1131":{"Name":"Apple candy","Expiry_date":"15/06/2025","Price":50,"Quantity":65,"Vegan":False},
    
}

num=int(input("Enter the no of products you wanna add\n"))
for i in range(num):
    prod_id1=input("Enter product ID : ")
    Name1=input("Enter Name : ")
    Expiry_date1=input("Enter Expiry_date : ")
    Price1=input("Enter Price : ")
    Quantity1=input("Enter Quantity : ")
    Vegan1=input("State True if its vegan and state False if it's not Vegan : ")
    item_list[prod_id1]={"Name":Name1,"Expiry_date":Expiry_date1,"Price":Price1,"Quantity":Quantity1,"Vegan":Vegan1}


temp1=json.dumps(item_list)



f=open("record.txt","w")
f.write(temp1)
f.close()

print("\nItems added in record.txt\n")




