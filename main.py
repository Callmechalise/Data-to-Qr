import qrcode

#basic file handelling
file=open("data.txt","r")
datas=(file.read())
break_char=","
list_of_data=datas.split(",")
print(list_of_data)

#Qr logic
for data in list_of_data:
    qr=qrcode.make(data)
    qr.save(f"{data.split()[0]}.png")
