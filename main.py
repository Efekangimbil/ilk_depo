sozluk = {
    "Cringe": "Başkasının yaptığı bir şey için kendin utanç duymak",
    "Lag": "Teknolojik bir alette takılma, donma",
    "LOL": "Komik bir şeye verilen cevap Açılımı=Laugh out loud yani Türkçe karşılığı olarak=Sesli bir şekilde gülmek/Kahkaha atmak"
}

kelime = input("Hangi kelimenin anlamını öğrenmek istersiniz?")

if kelime in ["cringe", "Cringe"]:
    print(sozluk["Cringe"])
elif kelime in ["lag", "Lag"]:
    print(sozluk["Lag"])
elif kelime in ["LOL", "lol"]:
    print(sozluk["LOL"])
else:
    print("Bu kelimenin anlamını bulamadım.")

    
