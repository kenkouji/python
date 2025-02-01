import qrcode
data = input('enter the text or url: ').strip()
filename=input("enter the file name u want to see the qr in(use.png): ").strip()
qr=qrcode.QRCode(box_size=10,border=4)
qr.add_data(data)
image=qr.make_image(fill_color="black",back_color="white")
image.save(filename)
print(f"qr code is saved succesfully in{filename}")
