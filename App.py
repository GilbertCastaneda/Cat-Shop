class Catype:
    def __init__(self, Size, Weight, Coat, Color, Summary, Cost):
        self.Size = Size
        self.Weight = Weight
        self.Coat = Coat
        self.Color = Color
        self.Summary = Summary
        self.Cost = Cost
Cat0 = Catype ("          Meduim","          10-lbs","          Meduim",          "          Orange-LightBrown","          Asian Leopard Cat.","          $2,000")
Cat1 = Catype ("          Meduim","          7-lbs","          Meduim","          Ruddy","          Abyssinians are highly intelligent and intensely inquisitive.","          $800")
Cat2 = Catype ("          Meduim","          12-lbs","          Short","          Black","          Has many dog-like tendencies.","          $700")
Cat3 = Catype ("          Small","          7-lbs","          Short","          Blue","          With unique ears that curl back","$          1100")
Cat4 = Catype ("          Meduim","          11-lbs","          Short","          White","          Formerly used to keep rodents and vermin away from food stores","          $600")
Cat5 = Catype ("          Medium","          12-lbs","          Medium","          Brown","          The Balinese, also known as Javanese depending on coat color and pattern","          $1300")
Cat6 = Catype ("          Medium","          9-lbs","          Medium","          Blue","          The Birman is a cat of distinction as well as legend",          "$2000")
Cat7 = Catype ("          Medium","          8-lbs","          Glossy","          White","          does not like sudden, loud noises.","          $80")
Cat8 = Catype ("          Long","          9-lbs","          Short","          Black","          The Bombay is an easy-going, yet energetic cat.","          $800")
Cat9 = Catype ("          large","          18-lbs","          Plush","          Blue","          The British Shorthair is an easygoing feline.","          $1800")
Cat10 = Catype("          Medium","          9-lbs","          Short","          Platinum","          The Burmese thrives on companionship with her humans and other cats.","          $2200")
Cat11 = Catype("          Medium","          13-lbs","          Medium","          Blue","          the Chartreux forms a close bond with her family","          $1300")
def Kat0():
    print("          Cat Breed: Bengal")
    print(Cat0.Size)
    print(Cat0.Weight)
    print(Cat0.Coat)
    print(Cat0.Color)
    print(Cat0.Summary)
    print(Cat0.Cost)
def Kat1():
    print("          Cat Breed: Abyssinian")
    print(Cat1.Size)
    print(Cat1.Weight)
    print(Cat1.Coat)
    print(Cat1.Color)
    print(Cat1.Summary)
    print(Cat1.Cost)
def Kat2():
    print("          Cat Breed: Bobtail")
    print(Cat2.Size)
    print(Cat2.Weight)
    print(Cat2.Coat)
    print(Cat2.Color)
    print(Cat2.Summary)
    print(Cat2.Cost)
def Kat3():
    print("          Cat Breed: Curl")
    print(Cat3.Size)
    print(Cat3.Weight)
    print(Cat3.Coat)
    print(Cat3.Color)
    print(Cat3.Summary)
    print(Cat3.Cost)
def Kat4():
    print("          Cat Breed: Shorthair")
    print(Cat4.Size)
    print(Cat4.Weight)
    print(Cat4.Coat)
    print(Cat4.Color)
    print(Cat4.Summary)
    print(Cat4.Cost)
def Kat5():
    print("          Cat Breed: Balinese")
    print(Cat5.Size)
    print(Cat5.Weight)
    print(Cat5.Coat)
    print(Cat5.Color)
    print(Cat5.Summary)
    print(Cat5.Cost)
def Kat6():
    print("          Cat Breed: Javanese")
    print(Cat6.Size)
    print(Cat6.Weight)
    print(Cat6.Coat)
    print(Cat6.Color)
    print(Cat6.Summary)
    print(Cat6.Cost)
def Kat7():
    print("          Cat Breed: Birman")
    print(Cat7.Size)
    print(Cat7.Weight)
    print(Cat7.Coat)
    print(Cat7.Color)
    print(Cat7.Summary)
    print(Cat7.Cost)
def Kat8():
    print("          Cat Breed: Munchkin")
    print(Cat8.Size)
    print(Cat8.Weight)
    print(Cat8.Coat)
    print(Cat8.Color)
    print(Cat8.Summary)
    print(Cat8.Cost)
def Kat9():
    print("          Cat Breed: Tabby")
    print(Cat9.Size)
    print(Cat9.Weight)
    print(Cat9.Coat)
    print(Cat9.Color)
    print(Cat9.Summary)
    print(Cat9.Cost)
def Kat10():
    print("          Cat Breed: Burmese")
    print(Cat10.Size)
    print(Cat10.Weight)
    print(Cat10.Coat)
    print(Cat10.Color)
    print(Cat10.Summary)
    print(Cat10.Cost)
def Kat11():
    print("          Cat Breed: Chartreux")
    print(Cat11.Size)
    print(Cat11.Weight)
    print(Cat11.Coat)
    print(Cat11.Color)
    print(Cat11.Summary)
    print(Cat11.Cost)
def Menu1():
    print()
    print("  ________________________________ ")
    print("  |           Cat Shop           | ")
    print("  |------------------------------| ")
    print("  | Bengal                  (1   | ")
    print("  | Abyssinian              (2   | ")
    print("  | Bobtail                 (3   | ")
    print("  | Curl                    (4   | ")
    print("  | Shorthair               (5   | ")
    print("  | Javanese                (6   | ")
    print("  | Birman                  (7   | ")
    print("  | Munchkin                (8   | ")
    print("  | Bombay                  (9   | ")
    print("  | Tabby                  (10   | ")
    print("  | Burmese                (11   | ")
    print("  | Chartreux              (12   | ")
    print("  |------------------------------| ")
    print("  | Current Cash:                | ")
    print("  | A)Exit         B)Owned Cats  | ")
    print("  |______________________________| ")
    print()
Menu1()
cat = input("Select cat number: ")
if cat == '1':
    Kat0()
    Menu2()
elif cat == "2":
    Kat1()
    Menu2()

elif cat == "3":
     Kat2()
     Menu2()

elif cat == "4":
    Kat3()
    Menu2()

elif cat == "5":
    Kat4()
    Menu2()

elif cat == "6":
    Kat5()
elif cat == "7":
    Kat6()
elif cat == "8":
    Kat7()
elif cat == "9":
    Kat8()
elif cat == "10":
    Kat9()
elif cat == "11":
    Kat10()
elif cat == "12":
    Kat11()
elif cat == "B":
    Kat10()
elif cat == "b":
    Kat11()
elif cat == "a":
    exit()
elif cat == "A":

    exit()
else:
    print("Invaild!")
def Menu2():
    cqt == Kat0
    print ()
    print("      I-----------------------I      ")
    print("                                     ")
    print("                                     ")
    print("  "+  cqt   + "                      ")
    print("                                     ")
    print("                                     ")
    print("       Purchase         Decline      ")
    print("         (A)              (B)        ")
    print("       I----------------------I      ")
    print(" Current Cats:      Current Money:   ")
    print ()
Menu2()
dot = input(": ")
if dot == 'a':
    print ("Letter a")
elif dot == "A":
    print ("Letter A")
elif dot == "B":
    print ("Letter B")
elif dot == "b":
    print ("b")
else:
    exit()