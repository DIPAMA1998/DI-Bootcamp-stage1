#challenge1
mot= input()
mot= {lettre : [mot.index(lettre) for i in lettre] for lettre in mot}
print(mot)

#challenge2
wallet= 50000
items_purchase = {
  "Water": 1,
  "Bread": 3,
  "TV": 1000,
  "Fertilizer": 20
}
articlpayable=[article for article in items_purchase if items_purchase [article]<=wallet]
print(articlpayable)