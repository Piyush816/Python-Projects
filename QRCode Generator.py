import pyqrcode
import png

text = input("Enter your message you want to store in QRCode: ")

url = pyqrcode.create(text)

choice = int(input("""
Choose any option

1.To see QRCode
2.Save in png
3.Save in svg

	\n"""))
try:

	if choice == 1:
		url.show()
	elif choice == 2:
		url.png("qr-code.png",scale=3)
	elif choice == 3:
		url.svg("qr-code.svg",scale=3)
	else:
		print("Invalid Input")

except:
	print("failed to save")