import qrcode

#basic file handelling
file=open("data.txt","r")
datas=(file.read())
data_split_char=","#split logic add anything which suits your data
list_of_data=datas.split(data_split_char)
print(list_of_data)

#Qr logic
for data in list_of_data:
    qr=qrcode.make(data)
    qr.save(f"{data.split()[0]}.png")#text till first space is filename
