from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os, sys

def print_ktm():
    img = Image.open("Template/lele.png")
    img1 = Image.open(photo1)
    img1 = img1.resize((455, 600), Image.ANTIALIAS)
    img.paste(img1, (185,498))
    d1 = ImageDraw.Draw(img)
    mfont = ImageFont.truetype("Font/Bebas-Regular.ttf",110)
    d1.text((1350,480),nama, font=mfont, fill="white")
    d1.text((1350,630),nim, font=mfont, fill="white")
    d1.text((1350,780),prodi, font=mfont, fill="white")
    d1.text((1350,930),jjng, font=mfont, fill="white")
    #img.show()
    img.save(output, 'PNG')
    print("Image saved as : ",output)

print("""
  _  _________ __  __        __  __       _             
 | |/ /__   __|  \/  |      |  \/  |     | |            
 | ' /   | |  | \  / |______| \  / | __ _| | _____ _ __ 
 |  <    | |  | |\/| |______| |\/| |/ _` | |/ / _ \ '__|
 | . \   | |  | |  | |      | |  | | (_| |   <  __/ |   
 |_|\_\  |_|  |_|  |_|      |_|  |_|\__,_|_|\_\___|_|   
""")
print("""
1) Single
2) Mass
3) Keluar""")
chose = input("\nPilih (1/2/3) : ")

if chose == "1":
    print("===================")
    nama = input("Nama : ")
    nim = input("Nim : ")
    prodi = input("Prodi :")
    jjng = input("jenjang : ")
    photo = input("Photo (ex: lele.png): ")
    photo1 = "Photo/"+ photo
    output = "Output/"+nim+"_"+nama+".png"
    print_ktm()
elif chose == "2":
    jumlah_data = int(input("Jumlah Data : "))
    for i in range(jumlah_data):
        print("===================")
        print("Data ke -",i+1)
        print("===================")
        nama = input("Nama : ")
        nim = input("Nim : ")
        prodi = input("Prodi :")
        jjng = input("jenjang : ")
        photo = input("Photo (ex: lele.png):")
        photo1 = "Photo/"+ photo
        output = "Output/"+nim+"_"+nama+".png"
        print_ktm()
else :
    sys.exit()