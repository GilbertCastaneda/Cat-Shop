class Catype:
    def __init__(self, Name, Size, Weight, Coat, Color, Summary, Cost):
        self.Name = Name # I added names to avoid passing around dictionary keys as values or addt'l params.
        self.Size = Size
        self.Weight = Weight
        self.Coat = Coat
        self.Color = Color
        self.Summary = Summary
        self.Cost = Cost

    def detail(self):
      print(self.Name)
      print(self.Size)
      print(self.Weight)
      print(self.Coat)
      print(self.Color)
      print(self.Summary)
      print(self.Cost)

# There are ways to use loops to display your menus here.
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

def Menu2(cat):
  print ()
  print("      I-----------------------I      ")
  print("                                     ")
  print("                                     ")
  cat.detail()
  print("                                     ")
  print("                                     ")
  print("       Purchase         Decline      ")
  print("         (A)              (B)        ")
  print("       I----------------------I      ")
  print(" Current Cats:      Current Money:   ")
  print ()

def main():
  # In python, this is called a dictionary.
  cats = {
    "Bengal": Catype("          Bengal","          Meduim","          10-lbs","          Meduim",          "          Orange-LightBrown","          Asian Leopard Cat.","          $2,000"),
    "Abyssinian": Catype("          Abyssinian","          Meduim","          7-lbs","          Meduim","          Ruddy","          Abyssinians are highly intelligent and intensely inquisitive.","          $800"),
    "Bobtail": Catype("          Bobtail","          Meduim","          12-lbs","          Short","          Black","          Has many dog-like tendencies.","          $700"),
    "Curl": Catype("          Curl","          Small","          7-lbs","          Short","          Blue","          With unique ears that curl back","          $1100"),
    "Shorthair": Catype("          Shorthair","          Meduim","          11-lbs","          Short","          White","          Formerly used to keep rodents and vermin away from food stores","          $600"),
    "Balinese": Catype("          Balinese","          Medium","          12-lbs","          Medium","          Brown","          The Balinese, also known as Javanese depending on coat color and pattern","          $1300"),
    "Javanese": Catype("          Javanese","          Medium","          9-lbs","          Medium","          Blue","          The Birman is a cat of distinction as well as legend",          "$2000"),
    "Birman": Catype("          Birman","          Medium","          8-lbs","          Glossy","          White","          does not like sudden, loud noises.","          $80"),
    "Munchkin": Catype("          Munchkin","          Long","          9-lbs","          Short","          Black","          The Bombay is an easy-going, yet energetic cat.","          $800"),
    "Tabby": Catype("          Tabby","          large","          18-lbs","          Plush","          Blue","          The British Shorthair is an easygoing feline.","          $1800"),
    "Burmese": Catype("          Burmese","          Medium","          9-lbs","          Short","          Platinum","          The Burmese thrives on companionship with her humans and other cats.","          $2200"),
    "Chartreux": Catype("          Chartreux","          Medium","          13-lbs","          Medium","          Blue","          the Chartreux forms a close bond with her family","          $1300"),
  }

  Menu1()

  cat = input("Select cat number: ")
  selected_cat = None

  if cat == '1':
      selected_cat = cats["Bengal"]
  elif cat == "2":
      selected_cat = cats["Abyssinian"]
  elif cat == "3":
      selected_cat = cats["Bobtail"]
  elif cat == "4":
      selected_cat = cats["Curl"]
  elif cat == "5":
      selected_cat = cats["Shorthair"]
  elif cat == "6":
      selected_cat = cats["Balinese"]
  elif cat == "7":
      selected_cat = cats["Javanese"]
  elif cat == "8":
      selected_cat = cats["Birman"]
  elif cat == "9":
      selected_cat = cats["Munchkin"]
  elif cat == "10":
      selected_cat = cats["Tabby"]
  elif cat == "11":
      selected_cat = cats["Burmese"]
  elif cat == "12":
      selected_cat = cats["Chartreux"]
  elif cat == "A" or cat == "a":
    print("Bye.")
    exit()
  elif cat == "B" or cat == "b":
    print("Unimplemented feature.") # You could implement this feature using a global variable with a List datatype.
    exit()
  else:
      print("Invaild!")
  
  Menu2(selected_cat)
  dot = input(": ")

  if dot == "B" or dot == "b":
    print("Thanks for coming! Sorry you didn't find a cat.")
  elif dot == "A" or dot == "a":
    print("Thanks for guying a cat. Hope you're happy with your " + selected_cat.Name.strip() + ".")
    exit()
  else:
    exit()

# this is a powerful magic - https://stackoverflow.com/questions/419163/what-does-if-name-main-do
if __name__ == "__main__":
  main()