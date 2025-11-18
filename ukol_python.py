#Tvým úkolem je vytvořit program pro zjednodušený výpočet daně z nemovitostí. 
#Aplikace bude postavená na principech OOP. Tato daň se vztahuje na pozemky, bytové a komerční prostory. 
#Výše daně se odvíjí od několika faktorů, např. typu nemovitosti, velikosti, lokalitě, kde se nemovitost nachází atd.

from math import ceil

#V rámci aplikace nejprve vytvoř třídu Locality, která označuje lokalitu, kde se nemovitost nachází. 
#Třída bude mít atributy name (název katastru/obce) a locality_coefficient (tzv. místní koeficient, který se používá k výpočtu daně).

class Locality:
    def __init__(self, name, locality_coefficient):
        self.name = name
        self.locality_coefficient = locality_coefficient

#Vytvoř třídu Property, která bude reprezentovat nějakou nemovitost. 
#Třída bude mít atribut locality (lokalita, kde se pozemek nachází, bude to objekt třídy Locality).

class Property:
    def __init__(self, locality):
        self.locality = locality

#Dále vytvoř třídu Estate, která reprezentuje pozemek a je potomkem třídy Property. 
#Třída bude mít atributy locality, estate_type (typ pozemku), area (plocha pozemku v metrech čtverečních). 
#Dále přidej metodu calculate_tax(), která spočítá výši daně pro pozemek a vrátí hodnotu jak celé číslo (pro zaokrouhlení použij funkci ceil() z modulu math).
#Daň vypočítej pomocí vzorce: plocha pozemku * koeficient dle typu pozemku (atribut estate_type) * místní koeficient. 

class Estate(Property):
    def __init__(self, locality, estate_type, area):
        super().__init__(locality)
        self.estate_type = estate_type
        self.area = area
    def calculate_tax(self):

#U atributu estate_type následující hodnoty a koeficienty:
#land (zemědělský pozemek) má koeficient 0.85.
#building site (stavební pozemek) má koeficient 9.
#forrest (les) má koeficient 0.35,
#garden (zahrada) má koeficient 2. 
   
        if self.estate_type == "land":
            coef = 0.85
        elif self.estate_type == "building site":
            coef = 9
        elif self.estate_type == "forrest":
            coef = 0.35
        elif self.estate_type == "garden":
            coef = 2
        else:
            coef = 1

        tax = self.area * coef * self.locality.locality_coefficient
        return ceil(tax)

#Uvažujme tedy například lesní pozemek o ploše 500 metrů čtverečních v lokalitě s místním koeficientem 2. Potom je daň 500 * 0.35 * 2 = 350.
#Vytvoř třídu Residence, která reprezentuje byt, dům či jinou stavbu a je potomkem třídy Property. 
#Třída bude mít atributy locality, area (podlahová plocha bytu nebo domu) a commercial (pravdivostní hodnota, která určuje, zda se jedná o nemovitost používanou k podnikání). 
#Dále přidej metodu calculate_tax(), která spočítá výši daně pro byt a vrátí hodnotu jako číslo. Daň vypočítej pomocí vzorce: podlahová plocha * koeficient lokality * 15. 
#Pokud je hodnota parametru commercial True, tj. pokud jde o komerční nemovitost, vynásob celou daň číslem 2.

#Příklad výpočtu: Uvažujme tedy například byt (určený k bydlení) o ploše 60 metrů čtverečních v lokalitě s koeficientem 3. Potom je daň 60 * 3 * 15 = 2700. Pokud by stejný byt byl používán k podnikání, daň by byla 60 * 3 * 15 * 2 = 5400.

class Residence(Property):
    def __init__(self, locality, area, commercial):
        super().__init__(locality)
        self.area = area
        self.commercial = commercial

    def calculate_tax(self):
        tax = self.area * self.locality.locality_coefficient * 15
        if self.commercial:
            tax = tax * 2
        return tax


#Vyzkoušej svůj program pomocí následujících nemovitostí:

manetin = Locality("Manětín", 0.8)
brno = Locality("Brno", 3)

#Zemědělský pozemek o ploše 900 metrů čtverečních v lokalitě Manětín s koeficientem 0.8. Daň z této nemovitosti je 900 * 0.85 * 0.8 = 612.
zemedelsky_pozemek = Estate(manetin, "land", 900)
print("Daň z pozemku:", zemedelsky_pozemek.calculate_tax(), "Kč")

#Dům s podlahovou plochou 120 metrů čtverečních v lokalitě Manětín s koeficientem 0.8. Daň z této nemovitosti je 120 * 0.8 * 15 = 1440.
dum = Residence(manetin, 120, False)
print("Daň z domu:", dum.calculate_tax(), "Kč")

#Kancelář (tj. komerční nemovitost) s podlahovou plochou 90 metrů čtverečních v lokalitě Brno s koeficientem 3. Daň z této nemovitosti je 90 * 3 * 15 * 2 = 8100.
kancelar = Residence(brno, 90, True)
print("Daň z kanceláře:", kancelar.calculate_tax(), "Kč")
