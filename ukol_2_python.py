#Zadání úkol 2
#Tvým úkolem je vytvořit program, který bude získávat data z obchodního rejstříku s využitím jeho REST API.

#Část 1
#V této části vyhledej informace o konkrétním subjektu na základě jeho identifikačního čísla (IČO). Toto číslo je jedinečným identifikátorem subjektu, pro každé číslo tedy rejstřík vrátí informace pouze o jednom subjektui. Nejprve se pomocí funkce input() zeptej uživatele nebo uživatelky, o kterém subjektu chce získat informace. 
#S využitím modulu requests odešli GET požadavek na adresu https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/ICO, kde ICO nahraď číslem, které zadal(ka) uživatel(ka) (např. https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/22834958). S adresou pracuj jako s obyčejným řetězcem, tj. můžeš využívat formátované řetězce, metodu .replace(), operátor + atd. 
#Text, který API vrátí, převeď na JSON a zjisti z něj obchodní jméno subjektu a adresu jeho sídla (můžeš využít podle textovaAdresa). Získané informace vypiš na obrazovku.

import requests

# 1) Zeptáme se uživatele na IČO
ico = input("Zadej IČO subjektu: ")

# 2) Sestavíme URL adresu
url = f"https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/{ico}"

# 3) Odešleme GET požadavek
response = requests.get(url)

# 4) Převedeme odpověď na JSON
data = response.json()

# 5) Z JSONu získáme potřebné údaje
obchodni_jmeno = data.get("obchodniJmeno")
adresa = data.get("sidlo", {}).get("textovaAdresa")

# 6) Vypíšeme výsledek
print(obchodni_jmeno)
print(adresa)

#Část 2
#Často se stane, že neznáme IČO subjektu, ale známe například jeho název nebo alespoň část názvu. 
#Napiš program, který se zeptá uživatele(ky) na název subjektu, který chce vyhledat. Následně vypiš všechny nalezené subjekty, které ti API vrátí.

import requests

# 1) Zeptáme se uživatele na název subjektu
nazev = input("Zadej název subjektu: ")

# 2) URL pro POST request
url = "https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat"

# 3) Hlavičky
headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
}

# 4) Data ve formátu JSON (jako řetězec!)
data = f'{{"obchodniJmeno": "{nazev}"}}'

# 5) Odeslání POST requestu
response = requests.post(url, headers=headers, data=data)

# 6) Převedení odpovědi na JSON
result = response.json()

# 7) Získání počtu subjektů a seznamu
pocet = result.get("pocetCelkem", 0)
subjekty = result.get("ekonomickeSubjekty", [])

# 8) Výpis výsledků
print(f"Nalezeno subjektů: {pocet}")

for subjekt in subjekty:
    jmeno = subjekt.get("obchodniJmeno")
    ico = subjekt.get("ico")
    print(f"{jmeno}, {ico}")
    
