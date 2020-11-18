import random
#pertanyaan masa depan======================
print("==========Future word==========")
nama=input("silahkan masukkan nama anda: ")

print("prepare you're self", nama)

pertanyaan = (bool(input("silahkan masukkan pertanyaan anda: ")))

kata=["ya, mungkin","tanyaki mama'nu","coba lagi", 
'mungkin lain kali', "haha you're so funny",
"i dont now about that tings", "liatki kananmu", 
"sakitko memang kau","jangko begitu de", "pertanyaan lain", 
"nda' lapar jako", "dimanako kah", "konapa tidak"]
anjay = random.choice(kata)
print(anjay)