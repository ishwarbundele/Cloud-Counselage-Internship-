import stepic
from PIL import Image
from cryptography.fernet import Fernet

print("*-------------------------------------*")

key = input(" KEY: ")
dec = Fernet(key)

file = input(" PHOTO: ")

img = Image.open(file)
decoded = stepic.decode(img)
text_dec = dec.decrypt(decoded.encode())

print(" DATA Is : "+ text_dec.decode())

print("*-------------------------------------*")
