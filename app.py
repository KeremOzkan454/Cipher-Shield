import modules.AI_module as AI_module
import modules.main_module as main_module
import os

def execute_the_app():
	while True:
		print("Parola güvenlik düzeyi ölçümü için 1")
		print("Parolanızın veri sızıntılarında açığa çıkıp çıkmadığını sorgulamak için 2")
		print("Güçlü parola önerisi için 3")
		print("Şifre kasasına erişmek için 4")
		print("Shield AI ile konuşmak için 5")
		print("Çıkış yapmak için 6 tuşlayınız")
		user_input = input(">> ")
		
		# Password Security Control
		if user_input == "1":
			password = input("Parolanızı giriniz: ")
			security_level = 0
			oneriler = ""

			uzunluk , kucuk_harf , buyuk_harf , sayi , karakter = main_module.password_control(password)

			if uzunluk:
				security_level += 2
			else:
				oneriler += "- Parolanızın en az 16 karakter uzunluğunda olması gerek\n"

			if kucuk_harf:
				security_level += 1
			else:
				oneriler += "- Parolanız en az bir adet küçük harf içermelidir\n"

			if buyuk_harf:
				security_level += 2
			else:
				oneriler += "- Parolanız mutlaka bir büyük harf içermelidir\n"

			if sayi:
				security_level += 2
			else:
				oneriler += "- Parolanız mutlaka bir sayı içermelidir\n"

			if karakter:
				security_level += 3
			else:
				oneriler += "- Parolanız en az bir tane özel karakter içermelidir\n"

			print(f"Parolanızın güvenlik düzeyi -> {security_level}/10")
			if security_level != 10:
				print(f"Aşağıdaki önerileri dikkate alarak parolanızı güçlendirmeniz önerilir:\n{oneriler}")
			
		# Password Pwned Control
		elif user_input == "2":
			password = input("Parolanızı giriniz: ")
			file = "data/pwned.txt"

			isPwned = main_module.check(password,file)

			if isPwned:
				print("Parolanız bir veri sızıntısında ele geçirilmiş. Parolanızı değiştirmeniz önemle rica olunur!")
			else:
				print("Parolanız şu ana kadarki hiçbir veri sızıntısında ele geçirilmemiş.")

		# Password Suggestion
		elif user_input == "3":
			password = main_module.generate_password()

			print(f"Önerilen güçlü parola: {password}")

		# Cipher Vault
		elif user_input == "4":
			# Kasa parolası yoksa:
			if not os.path.exists("data/VaultPass.txt"):
				main_module.create_vault_pass()
				main_module.create_vault()
				print("Daha önce bir şifre kasası oluşturmamışsınız. Lütfen önce bir kasa parolası belirleyiniz: ")
				vault_password = input()
				main_module.write_vault_password(vault_password)
			
			print("Kasanıza erişmek için lütfen kasa şifrenizi giriniz: ")
			user_vault_password = input()
			isTrue = main_module.check_vault_password(user_vault_password)
			if isTrue:
				while True:
					key = main_module.create_or_load_key()
					print("Kasanıza Hoşgeldiniz!\nKaydedilmiş parolalarınızı görüntülemek için 1\nKasanıza parola kaydetmek için 2\nÇıkış yapmak için 3 tuşlayınız.\n")
					sechenek = input(">> ")
					if sechenek == "1":
						main_module.load_passwords(key)
					elif sechenek == "2":
						user_name = input("Kasnıza kaydedeceğiniz kullanıcı adınızı giriniz: ")
						user_password = input("Kaydetmek istediğiniz parolayı giriniz: ")

						main_module.save_password(user_name,user_password,key)
						print(f"Parolanız {user_name} için kaydedildi!")
					elif sechenek == "3":
						break
					else:
						print("\nLütfen geçerli bir sayı giriniz!\n")
			else:
				print("Girdiğiniz kasa parolası hatalı! Lütfen tekrar deneyin!")

		# Shield AI
		elif user_input == "5":
			print("Shield AI ile sohbetinize son vermek için 'çık' yazabilirsiniz")
			
			while True:
				user_send = input("Siz: ")
				response = AI_module.get_response(user_send)
				if response == "EXIT":
					break
				else:
					print(f"Shield AI: {response}")

		# EXIT
		elif user_input == "6":
			break

		# Hatalı sayı girişi
		else:
			print("Lütfen geçerli bir sayı giriniz!")



if __name__ == "__main__":
	execute_the_app()