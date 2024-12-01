import re
import modules.AI_module as AI_module

# Ana döngü
print("Shield AI: Sohbetinize son vermek için 'kapat' ya da 'çıkış' yazabilirsiniz.")
while True:
    # ShieldAI dan çıkış
    user_input = input("Siz: ")
    if re.search(r"çık|kapat|kapa|çıkış", user_input.lower()):
        print("Shield AI: Görüşmek üzere.")
        break
    else:
        response = AI_module.user_input_control(user_input=user_input.lower())
        print(f"Shield AI: {response}")