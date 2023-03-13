import csv
from datetime import datetime 
import os.path

# Menu.txt dosyasını okuyarak konsola menüyü bastırır.
def printMenu():
    menu = open("Menu.txt","r",encoding="utf-8")
    read = menu.read()
    print(read)

# Pizza üst sınıfı ve metodları
class Pizza:
    def __init__(self):
        self.description = ""
        self.cost = 0

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost

# Pizza çeşitleri sınıfları
class ClassicPizza(Pizza):
    def __init__(self):
        self.description = "Klasik Pizza"
        self.cost = 50

class MargheritaPizza(Pizza):
     def __init__(self):
        self.description = "Margherita"
        self.cost = 60

class TurkishPizza(Pizza):
     def __init__(self):
        self.description = "Türk Pizzası"
        self.cost = 70

class DominosPizza(Pizza):
     def __init__(self):
        self.description = "Dominos Pizza"
        self.cost = 80

# Decorator üst sınıfı ve metodları
class Decorator(Pizza):
    def __init__(self, sauce):
        self.sauce = sauce

    def get_description(self):
        return self.sauce.get_description() + ', ' + Pizza.get_description(self)

    def get_cost(self):
        return self.sauce.get_cost() + + Pizza.get_cost(self)

# Decorator çeşitleri sınıfları
class Olives(Decorator):
    def __init__(self, sauce):
        self.sauce = sauce
        self.description = "Zeytin"
        self.cost = 5

class Mushrooms(Decorator):
    def __init__(self, sauce):
        self.sauce = sauce
        self.description = "Mantar"
        self.cost = 6

class GoatCheese(Decorator):
    def __init__(self, sauce):
        self.sauce = sauce
        self.description = "Keçi Peyniri"
        self.cost = 7

class Meat(Decorator):
    def __init__(self, sauce):
        self.sauce = sauce
        self.description = "Et"
        self.cost = 8

class Onion(Decorator):
    def __init__(self, sauce):
        self.sauce = sauce
        self.description = "Soğan"
        self.cost = 9

class Corn(Decorator):
    def __init__(self, sauce):
        self.sauce = sauce
        self.description = "Mısır"
        self.cost = 10

# Kullanıcıdan input alma. Alınan inputa göre kullanıcı siparişi oluşturuyor.
def getOrder():

    pizza = ""
    while pizza == "":
        userInput = int(input("Seçtiğiniz pizza tabanını giriniz: "))        
        if userInput == 1:
            pizza = ClassicPizza()
        elif userInput == 2:
            pizza = MargheritaPizza()
        elif userInput == 3:
            pizza = TurkishPizza()
        elif userInput == 4:
            pizza = DominosPizza()
        else:
            print("Lütfen geçerli bir sayı giriniz! ")
   
    sauce = ""
    while sauce == "":
        userInput = int(input("Seçtiğiniz sosu giriniz: "))
        if userInput == 11:
            sauce = Olives(pizza)
        elif userInput == 12:
            sauce = Mushrooms(pizza)
        elif userInput == 13:
            sauce = GoatCheese(pizza)
        elif userInput == 14:
            sauce = Meat(pizza)
        elif userInput == 15:
            sauce = Onion(pizza)
        elif userInput == 16:
            sauce = Corn(pizza)
        else:
            print("Lütfen geçerli bir sayı giriniz! ")
    return sauce

# Ödeme adımı
def payment(userOrder):

    while True:
        userName = input("Adınızı giriniz: ")
        if len(userName) != 0:
            break
        else:
            print("Lütfen geçerli bir ad giriniz!")

    # TC no 11 karakter olmak zorundadır.
    while True:
        userTC = input("TC no giriniz: ")
        if len(userTC) == 11:
            break
        else:
            print("Lütfen geçerli bir TC no giriniz!")
   
    # Kredi kartı numarası 16 hane olmalı (boşluksuz. ex: 1111222233334444)  
    while True:
        userCreditCard = input("Kredi kartı numaranızı giriniz: ")
        if len(userCreditCard) == 16:
            break
        else:
            print("Lütfen geçerli bir kredi kartı numarası giriniz!")
   
   # Kredi kartı şifresi 4 hane olmalı (boşluksuz. ex: 1234)  
    while True:
        userPassword = input("Kredi kartı şifrenizi giriniz: ")
        if len(userPassword) == 4:
            break
        else:
            print("Lütfen geçerli bir şifre giriniz!")
    
    # İşlemler tamamlandıktan sonra CSV dosyasına yazma işlemleri başlatılır.
    writeCSVfile(userOrder, userName, userTC, userCreditCard, userPassword)

def writeCSVfile(userOrder, userName, userTC, userCreditCard, userPassword):

    # Eğer dosya mevcut değilse, oluşturulur. Mevcut ise sona ekleme yapılır.
    file_exists = os.path.isfile("Orders_Database.csv")
    with open("Orders_Database.csv", "a", newline="") as file:
        fieldnames = ["Kullanici adi", "TC no", "Kredi karti no", "Siparis aciklamasi","Siparis tutari", "Siparis zamani", "Kredi karti sifresi"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        
        # Sipariş için sipariş zamanı datetime kullanılarak çekilir ve formatlama yapılır.
        current_time = datetime.now()
        formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

        # Kullanıcı ve sipariş bilgileri CSV dosyasına eklenir.
        writer.writerow({'Kullanici adi': userName, 'TC no': userTC, 'Kredi karti no': userCreditCard, 
                         'Siparis aciklamasi': userOrder.get_description(), 'Siparis tutari': userOrder.get_cost(), 'Siparis zamani': formatted_time,
                         'Kredi karti sifresi': userPassword})

# Main
printMenu()

userOrder = getOrder()

totalPrice = userOrder.get_cost()
pizzaDescription = userOrder.get_description()

print("Your order:")
print("Description: " + pizzaDescription)
print("Price: " + str(totalPrice))

print("Ödeme işlemleri:")
payment(userOrder)
print("Ödeme işlemi başarıyla tamamlandı")

print("*** İşlem Tamamlandı. İyi Günler Dileriz. ***")