import random

şehirler = ["New York", "Tokyo", "İstanbul", "Londra"]
bölgeler = ["Doğu", "Batı"]
mülk_tipleri = [
    ("Kiralık Ev", "kiralik_ev"),
    ("Satılık Ev", "satilik_ev"),
    ("Kiralık Ofis", "kiralik_ofis"),
    ("Satılık Ofis", "satilik_ofis")
]


def konum_üret(şehir):
    sokaklar = ["1. Cadde", "Merkez Caddesi", "Park Yolu", "Güneş Bulvarı", "Köprü Sokak"]
    return f"{şehir}, {random.choice(sokaklar)}"


def fiyat_üret(tip):
    if "Kiralık" in tip:
        return random.randint(800, 5000)
    else:
        return random.randint(50000, 500000)


mülkler = []

for şehir in şehirler:
    for tip_adı, kod in mülk_tipleri:
        for i in range(5):
            mülkler.append({
                "şehir": şehir,
                "tip": tip_adı,
                "fiyat": fiyat_üret(tip_adı),
                "konum": konum_üret(şehir)
            })


temsilciler = [
    {"id": 1, "ad": "New York Doğu Temsilcisi", "şehir": "New York", "bölge": "Doğu", "kullanıcı": "nyd", "şifre": "1001"},
    {"id": 2, "ad": "New York Batı Temsilcisi", "şehir": "New York", "bölge": "Batı", "kullanıcı": "nyb", "şifre": "1002"},

    {"id": 3, "ad": "Tokyo Doğu Temsilcisi", "şehir": "Tokyo", "bölge": "Doğu", "kullanıcı": "tkd", "şifre": "2001"},
    {"id": 4, "ad": "Tokyo Batı Temsilcisi", "şehir": "Tokyo", "bölge": "Batı", "kullanıcı": "tkb", "şifre": "2002"},

    {"id": 5, "ad": "İstanbul Doğu Temsilcisi", "şehir": "İstanbul", "bölge": "Doğu", "kullanıcı": "isd", "şifre": "3001"},
    {"id": 6, "ad": "İstanbul Batı Temsilcisi", "şehir": "İstanbul", "bölge": "Batı", "kullanıcı": "isb", "şifre": "3002"},

    {"id": 7, "ad": "Londra Doğu Temsilcisi", "şehir": "Londra", "bölge": "Doğu", "kullanıcı": "lnd", "şifre": "4001"},
    {"id": 8, "ad": "Londra Batı Temsilcisi", "şehir": "Londra", "bölge": "Batı", "kullanıcı": "lnb", "şifre": "4002"},
]



def temsilci_girişi():
    print("=== TEMSİLCİ GİRİŞİ ===")
    kullanıcı = input("Kullanıcı adı: ")
    şifre = input("Şifre: ")

    for t in temsilciler:
        if t["kullanıcı"] == kullanıcı and t["şifre"] == şifre:
            print(f"\n✔ Giriş başarılı! Hoş geldiniz, {t['ad']}.\n")
            return t

    print("❌ Hatalı kullanıcı adı veya şifre! Tekrar deneyin.\n")
    return temsilci_girişi()


def menü_göster(temsilci):
    print("\n--------------------------------")
    print(f"TEMSİLCİ PANELİ: {temsilci['ad']}")
    print("--------------------------------")
    print("1 - Şehrimdeki tüm mülkleri listele")
    print("2 - Tüm şehirlerdeki mülkleri listele")
    print("3 - Şehrimde kiralık / satılık filtrele")
    print("4 - Şehir seç ve tüm mülkleri listele")
    print("5 - Şehir seç ve kiralık / satılık filtrele")
    print("6 - Bütçeme göre mülk ara")
    print("7 - Şehir seç ve bütçeye göre mülk ara")
    print("0 - Çıkış")
    print("--------------------------------")


def mülk_listele(filtre_fonk):
    sonuç = filtre_fonk()
    if not sonuç:
        print("⚠ Bu kriterlere uygun mülk bulunamadı.")
        return
    for m in sonuç:
        print(f"{m['şehir']} | {m['tip']} | {m['fiyat']} USD | {m['konum']}")


def şehir_seç():
    print("Şehir seçiniz:")
    for i, s in enumerate(şehirler, 1):
        print(f"{i} - {s}")
    secim = int(input("Şehir ID: "))
    return şehirler[secim - 1]


def arayüzü_başlat():
    temsilci = temsilci_girişi()

    while True:
        menü_göster(temsilci)
        sel = input("Seçiminiz: ")

        if sel == "1":
            mülk_listele(lambda: [m for m in mülkler if m["şehir"] == temsilci["şehir"]])

        elif sel == "2":
            mülk_listele(lambda: mülkler)

        elif sel == "3":
            t = input("Kiralık için 1, Satılık için 2 yazın: ")
            if t == "1":
                mülk_listele(lambda: [m for m in mülkler if "Kiralık" in m["tip"] and m["şehir"] == temsilci["şehir"]])
            else:
                mülk_listele(lambda: [m for m in mülkler if "Satılık" in m["tip"] and m["şehir"] == temsilci["şehir"]])

        elif sel == "4":
            seçilen = şehir_seç()
            mülk_listele(lambda: [m for m in mülkler if m["şehir"] == seçilen])

        elif sel == "5":
            seçilen = şehir_seç()
            tip = input("Kiralık için 1, Satılık için 2: ")
            if tip == "1":
                mülk_listele(lambda: [m for m in mülkler if "Kiralık" in m["tip"] and m["şehir"] == seçilen])
            else:
                mülk_listele(lambda: [m for m in mülkler if "Satılık" in m["tip"] and m["şehir"] == seçilen])

        elif sel == "6":
            min_f = int(input("Minimum fiyat: "))
            max_f = int(input("Maksimum fiyat: "))
            mülk_listele(lambda: [m for m in mülkler if min_f <= m["fiyat"] <= max_f])

        elif sel == "7":
            seçilen = şehir_seç()
            min_f = int(input("Minimum fiyat: "))
            max_f = int(input("Maksimum fiyat: "))
            mülk_listele(lambda: [m for m in mülkler if m["şehir"] == seçilen and min_f <= m["fiyat"] <= max_f])

        elif sel == "0":
            print("Sistemden çıkılıyor...")
            break



arayüzü_başlat()
