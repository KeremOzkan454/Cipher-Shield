# Cipher Shield

**Cipher Shield** kullanıcıya siber dünyada nasıl güvenli bir şekilde hareket edebileceğini öğretmeyi amaçlayan bir uygulamadır. **Password Control** özelliği ile şifrelerinizin güvenli olup olmadaığını kontrol edebilir, **Cipher Vault** özelliği ile de kullanıcı adı ve şifrelerinizi encrypt edilmiş bir kasada depo edip istediğiniz zaman erişebilirsiniz. Ayrıca Cipher Shield uygulaması, 7'den 77'ye her yaştaki insanlara dijital farkındalık kazandırmak için tasarlanmış bir yapay zeka ile donatılmıştır. **Shield AI** sayesinde bireyler siber güvenlik hakkında merak ettikleri sorulara cevap bulabileceklerdir.

---------------
## Geliştirici Günlüğü:

20/11/2024 --- **main.py** dosyasına temelleri attım. Parola güç kontrolü, pwned kontrolü yapıyor ve güçlü parola önerebiliyor.
Daha çok iş var :/

-------------------
22/11/2024 --- **ShieldAI** üzerinde çalışıyorum ama işler pek te beklediğim gibi değil. Saçma sapan hatalar ile karşılaştım ve şuan gece 01:00. Yarın bug fix yapacağım...

-------------------
24/11/2024 --- **Rapor** üzerinde çalışıyorum ve düşündüğümden çok daha iyi oldu. Hala geliştirilmesi gerekiyor ama bana kalırsa şu anki hali gayet muhteşem! :)
Not: Shield AI hala çalışmıyor...

---------------------
26/11/2024 --- **main.py**'a CipherVault özelliği eklemeye çalışıyorum. Şifreleri bir dosyada şifrelenmiş bir şekilde depo etmesi gerekiyor ama hata verdi :/ Yarın ya da öbür gün CipherVault'u da bitirip artık ShieldAI üzerine yoğunlaşabilirim diye ümit ediyorum...

-------------------------
27/11/2024 --- **Rapor** bayağı iyi gidiyor. Yöntem bölümünü neredeyse tamamen bitirdim. Giriş bölümüne eklemek için makaleler araştırıyorum şuan. Yarın umarım onları da ekleyebilirim.

----------------------------
30/11/2024 --- **main.py** 'a sonunda **CipherVault** özelliği ekleyebildim. Kullanıcının girdiği parolaları depo ediyor. Ve bu işlemi **Fernet** encrypt yöntemi ile yapıyor. Kısaca bir saldırgan parolaların depo edildiği dosyayı bulursa kişinin parolalarına erişemiyor. Oldukça güvenli...

------------------------------
01/12/2024 -- **YAŞASINN!!!** **Shield AI** çalışıyor! DataBase ini geliştirmek kaldı sadece. Bir de Rapor tabii...

---------------------------------
