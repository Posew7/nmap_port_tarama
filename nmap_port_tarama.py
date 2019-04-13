import os

def isIp(ip_adresi):


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
    os.system("nmap " + ip_adresi)
elif (islem == 2):
    ip_adresi = input("\nIp Adresini Girin\n\n")
    os.system("nmap -p- -sV " + ip_adresi)
elif (islem == 3):
    ip_adresi = input("\nIp Adresini Girin\n\n")
    os.system("nmap -0 " + ip_adresi)
elif (islem == 4):
    ip_adresi = input("\nIp Adresini Girin\n\n")
    os.system("nmap -p- -sV -A " + ip_adresi)
else:
    print("Yanlış Değer Girdiniz")