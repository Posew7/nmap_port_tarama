import os

def isIp(kelime):

    global flag
    flag = False
    for i in kelime:
        if (i == "1" or i == "2" or i == "3" or i == "4" or i == "5" or i == "6" or i == "7" or i == "8" or i == "9" or i == "0" or i == "."):
            flag = True
        else:
            flag = False
            break

os.system("apt-get install nmap")
os.system("apt-get install figlet")

os.system("clear")

os.system("figlet PORT TARAMA")

print("""

1 - Normal Tarama
2 - Servis ve Versiyon Tarama (Tüm Port)
3 - İşletim Sistemi Tarama
4 - Detaylı Tarama (Tüm Port)

""")

islem = int(input("Yapmak İstediğiniz İşlemi Girin\n\n"))

if (islem == 1):
    ip_adresi = input("\nIp Adresini Girin\n\n")
    isIp(ip_adresi)
    if (flag):
        os.system("nmap " + ip_adresi)
    else:
        print("olmadı")
elif (islem == 2):
    ip_adresi = input("\nIp Adresini Girin\n\n")
    isIp(ip_adresi)
    os.system("nmap -p- -sV " + ip_adresi)
elif (islem == 3):
    ip_adresi = input("\nIp Adresini Girin\n\n")
    isIp(ip_adresi)
    os.system("nmap -0 " + ip_adresi)
elif (islem == 4):
    ip_adresi = input("\nIp Adresini Girin\n\n")
    isIp(ip_adresi)
    os.system("nmap -p- -sV -A " + ip_adresi)
else:
    print("Yanlış Değer Girdiniz")