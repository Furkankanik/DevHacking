import os

def Lordmap():
    os.system("figlet Lordmap Hacking")

    print("""
    Lordmap Programına Hoş Geldiniz...
          
    1-İp Adresi Tara
    2-Hostname Veya Domain Tara
    3-Birden Fazla İp Adresi Tara
    4-İp Aralığı Tara
    5-Tüm Ağı Tara
    6-İşletim Sistemi Bilgilerini Al
    7-Güvenlik Duvarı Hakkında Bilgi Al
    8-Belirli Port Tara
    9-TCP Ve UDP Portlarını Tara
    10-Bağlantı Hizmet Ve Sürüm Bilgilerini Tespit Et
    11-Seçilen İp Adreslerini hariç Tutarak Tara
    12-Dosyadan Liste Tutarak Tara
    13-Dosyadan Hariç Tutulan İp Adreslerini Alarak Tara
    14-Belirli Bir Port Aralığını Tara
    15-Tüm Portları Tara
    16-Tüm TCP Portlarını Tara
    17-Tüm UDP Portlarını Tara
    18-Sadece Açık Portları Tara
    19-Tarama Sırasında İşletim Sistemi Bilgisi Al
    20-Paket Filter Ve/Veya Firewall Algıla
    21-Tarama Günlüğünü Belirli Bir Dosyaya Kaydet
    """)

    seçim = input("Lütfen Ne Tür Tarama İstediğinizi Seçiniz:")

    if seçim == "1":
        ip = input("Hedef İP Adresini Giriniz:")
        os.system("nmap " + ip)
    elif seçim == "2":
        host = input("Hedef Hostname veya Domaini Giriniz:")
        os.system("nmap " + host)
    elif seçim == "3":
        ipler = input("Hedef İp Adreslerini Giriniz (virgülle ayırarak):")
        os.system("nmap " + ipler)
    elif seçim == "4":
        ip_Aralığı = input("Hedef İp Aralığını Giriniz (örn: 192.168.1.1-100):")
        os.system("nmap " + ip_Aralığı)
    elif seçim == "5":
        tüm_Ağı_Tara = input("Hedef Ağ İp Giriniz (örn: 192.168.1.0/24):")
        os.system("nmap " + tüm_Ağı_Tara)
    elif seçim == "6":
        Os_Bilgisi = input("Hedef İp Adresini Giriniz:")
        os.system("nmap -O " + Os_Bilgisi)
    elif seçim == "7":
        Güvenlik_Duvarı = input("Hedef İp Adresini Giriniz:")
        os.system("nmap -sA " + Güvenlik_Duvarı)
    elif seçim == "8":
        Port_Tarama = input("Hedef İp Adresini Giriniz:")
        os.system("nmap -p " + Port_Tarama)
    elif seçim == "9":
        Port_Tarama = input("Hedef İp Adresini Giriniz:")
        os.system("nmap -p " + Port_Tarama)
    elif seçim == "10":
        baglanti_hizmeti = input("Hedef İp Adresini Giriniz:")
        os.system("nmap -sV " + baglanti_hizmeti)
    elif seçim == "11":
        ip_liste = input("Hedef İp Adreslerini Giriniz (virgülle ayırarak):")
        os.system("nmap --exclude " + ip_liste)
    elif seçim == "12":
        dosya_yolu = input("Dosya Yolu ve Adı Giriniz:")
        os.system("nmap -iL " + dosya_yolu)
    elif seçim == "13":
        dosya_yolu = input("Dosya Yolu ve Adı Giriniz:")
        os.system("nmap --excludefile " + dosya_yolu)
    elif seçim == "14":
        port_aralığı = input("Port Aralığını Giriniz (örn: 20-100):")
        ip_adresi = input("Hedef İp Adresini Giriniz:")
        os.system("nmap -p " + port_aralığı + " " + ip_adresi)
    elif seçim == "15":
        tüm_portlar = input("Hedef İp Adresini Giriniz:")
        os.system("nmap -p- " + tüm_portlar)
    elif seçim == "16":
        tüm_tcp_portlar = input("Hedef İp Adresini Giriniz:")
        os.system("nmap -sT " + tüm_tcp_portlar)
    elif seçim == "17":
        tüm_udp_portlar = input("Hedef İp Adresini Giriniz:")
        os.system("nmap -sU " + tüm_udp_portlar)
    elif seçim == "18":
        açık_portlar = input("Hedef İp Adresini Giriniz:")
        os.system("nmap --open " + açık_portlar)
    elif seçim == "19":
        işletim_sistemi = input("Hedef İp Adresini Giriniz:")
        os.system("nmap -O -v " + işletim_sistemi)
    elif seçim == "20":
        paket_filter = input("Hedef İp Adresini Giriniz:")
        os.system("nmap -sS " + paket_filter)
    elif seçim == "21":
        tarama_günlüğü = input("Günlük Dosya Adı ve Yolu Giriniz:")
        hedef_ip = input("Hedef İp Adresini Giriniz:")
        os.system("nmap -oN " + tarama_günlüğü + " " + hedef_ip)
    else:
        print("Geçersiz seçim. Lütfen geçerli bir seçenek seçin.")

Lordmap()
