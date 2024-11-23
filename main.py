import module

while True:
    print("Parolanızın güvenliğini kontrol etmek için 1")
    print("Parolanızın veri ihlallerinde açığa çıktığını sorulamak için 2")
    print("SGüçlü parola önerisi için 3")
    user_input = input("Uygulamadan çıkış yapmak için 4 tuşlayınız\n>>>")
    
    # Parola Güvenlik kontrolü
    if user_input == "1":

        parola = input("Parolanızı giriniz >>> ")
        uzunluk, kucuk_harf, buyuk_harf, sayi, karakter = module.password_control(parola)
        parola_uzunlugu = len(parola)
        deger = 0

        if uzunluk:
            deger += 2
        if kucuk_harf:
            deger += 1
        if buyuk_harf:
            deger += 2
        if sayi:
            deger += 2
        if karakter:
            deger += 3

        print(f"Parolanızın güvenlik düzeyi: {deger} / 10\n")

        if deger == 0:
            print("[_ _ _ _ _ _ _ _ _ _]")
        elif deger == 1:
            print("[# _ _ _ _ _ _ _ _ _]")
        elif deger == 2:
            print("[# # _ _ _ _ _ _ _ _]")
        elif deger == 3:
            print("[# # # _ _ _ _ _ _ _]")
        elif deger == 4:
            print("[# # # # _ _ _ _ _ _]")
        elif deger == 5:
            print("[# # # # # _ _ _ _ _]")
        elif deger == 6:
            print("[# # # # # # _ _ _ _]")
        elif deger == 7:
            print("[# # # # # # # _ _ _]")
        elif deger == 8:
            print("[# # # # # # # # _ _]")
        elif deger == 9:
            print("[# # # # # # # # # _]")
        elif deger == 10:
            print("[# # # # # # # # # #]")

        if deger > 9:
            print("\nYaşasın! Parolanız oldukça güvenli.")
        elif deger > 4 and deger < 10:
            print("\nParolanız kısmen güvenli. Lütfen aşağıdaki önerilere dikkat ederek farklı bir parola belirleyiniz!")
        elif deger <= 4:
            print("\nParolanız çok zayıf. Lütfen aşağıdaki önerilere dikkat ederek farklı bir parola belirleyiniz!")
        
        if not uzunluk:
            print(f"\nParolanız en az 12 karakter uzunluğunda olmalıdır! Sizin parolanız ise {parola_uzunlugu} uzunluğunda.")
        if not kucuk_harf:
            print("\nParolanız küçük harf içermelidir!")
        if not buyuk_harf:
            print("\nParolanız büyük harf içermelidir!")
        if not sayi:
            print("\nParolanız sayı içermelidir!")
        if not karakter:
            print("\nParolanız özel karakter içermelidir!")

    # Parola pwned kontrolü
    elif user_input == "2":
        parola = input("Parolanızı giriniz >>> ")
        is_pwn = module.check(parola)

        if not is_pwn:
            print("Parolanız şu ana kadarki hiçbir veri ihlalinde açığa çıkmamış. Parolanız güvende.")
        else:
            print("Eyvah! Görünüşe göre parolanız bir veri ihlalinde ortaya çıkarılmış. Bu parolayı değiştirmeniz şiddetle tavsiye edilir!")

    # Parola önerisi
    elif user_input == "3":
        oneri = module.generate_password()
        print(f"Güçlü parola: {oneri}")

    # Çıkış   
    elif user_input == "4":
        print("Tekrar görüşmek dileğiyle...")
        break

    # Hatalı sayı girişi 
    else:
        print("Lütfen geçerli bir sayı giriniz!!!")

