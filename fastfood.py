from os import system
system('cls')
class fastfood:
    sch=0
    def __init__(self):
        self.lang=int(input("Ozbek tili 1 / Rus tili 2: "))
        if self.lang==1:
            system('cls')
            print("Assalomu aleykum")
            self.kirish()
    def kirish(self):
        print("""Quyidagilardan birini tanlang:\n\n
1.Ichimliklar \t\t\t\t2.Burgerlar\n
3.Lavash         \t\t\t\t4.Pitsalar""")
        natija=input("Tanlang: ")
        match natija:
            case "1":
                self.ichimlik()
            case "2":
                self.burger()
            case "3":
                self.lavash()
            case "4":
                self.pitsa()
    def qaytish(self):
        answer=input("Hurmatli mijoz yana biron nimadir buyurasizmi? (Ha,Yo'q)? ")
        if answer.upper()=="HA":
            self.kirish()
        else:
            system("cls")
            print("Salomat bo'ling")
            print("Hurmatli mijoz sizdan shuncha summa boldi",self.sch)
    def ichimlik(self):
        system('cls')
        print("""Tanlang:
                1.Coca-cola - 15.000
                2.Pepsi - 15.000
                3.Dena - 12.000
                4.Fanta - 18.000
                5.Chortoq - 13.000""")
        suv=input("Tanlang: ")
        match suv:
            case '1':
                self.sch+=15000
            case '2':
                self.sch+=15000
            case '3':
                self.sch+=12000
            case '4':
                self.sch+=18000
            case '5':
                self.sch+=13000
        self.qaytish()
    def burger(self):
        system("cls")
        print("""Quyidagilardan birini tanlang: 
                1.Burger - 25000
                2.Cheeseburger - 30000
                3.Doublechess - 35000""")
        bur=input("Tanlang: ")
        match bur:
            case '1':
                self.sch+=25000
            case '2':
                self.sch+=30000
            case '3':
                self.sch+=35000
        self.qaytish()
    def lavash(self):
        system('cls')
        print("""Quydagilardan birini tanlang: 
                1.Standart - 20.000
                2.cheese - 25.000""")
        lav=input("Tanlang lavashlardan birini : ")
        match lav:
            case '1':
                self.sch+=20000
            case '2':
                self.sch+=25000
        self.qaytish()
    def pitsa(self):
        system('cls')
        print("""Quydagi pitsalardan birini tanlang:
                1.Goshtli - 57.000
                2.Otli - 30.000
                3.Sirli - 55.000 """)
        pit=input("Pitsalardan birini tanlang: ")
        match pit:
            case '1':
                self.sch+=57000
            case '2':
                self.sch+=30000
            case '3':
                self.sch+55000
        self.qaytish()        
f=fastfood()
# f.kirish()
# f.ichimlik()
# f.burger()
# f.lavash()
# f.pitsa()
