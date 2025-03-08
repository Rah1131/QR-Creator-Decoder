# QR Code Generator and Scanner

# Import necessary libraries
from pyzbar.pyzbar import decode  # LCibrary to decode QR codes
import pyqrcode  # Library to generate QR codes
import PIL.Image  # PIL for opening images

# Prompt the user to choose an action
n = input('Enter "C" to create a QR Code (or) "U" to Upload QR code path: ')

if n.lower() == "c":
    # Generate a QR code from user input
    n1 = input("Enter the string/URL to convert into a QR Code: ")
    qr = pyqrcode.create(n1)  # Create QR code
    qr.png("myQrCode.png", scale=8)  # Save QR code as PNG with a scale of 8
    print("QR Code saved as myQrCode.png")  # Notify the user

elif n.lower() == "u":
    # Decode a QR code from an uploaded image
    image_path = input("Enter the path of the QR code image: ")
    try:
        img = PIL.Image.open(image_path)  # Open the image
        decoded_data = decode(img)  # Decode the QR code

        if decoded_data:
            print("Scanned QR Code from image: \n", decoded_data[0].data.decode('ascii'))  # Print decoded data
        else:
            print("No QR Code found in the image.")  # Notify if no QR code was detected
    except Exception as e:
        print("Error:", e)  # Print any errors

else:
    print("Invalid option. Please enter C or U.")  # Handle invalid input
