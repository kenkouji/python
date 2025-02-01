import qrcode
data=input("enter the url you want as qr code: ")
file=input("enter the file name u want the qr to be entered into: ")
qr= qrcode.QRCode(box_size=10,border=4)
qr.add_data(data)
qr.make(fit=True)
image=qr.make_image(fill_color="black",back_color="white")
image.save(file)
