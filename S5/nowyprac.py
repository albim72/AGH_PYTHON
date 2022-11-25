import json

def dodaj_nowego_pracownika(new_data,filename="pracownik.json"):
    with open(filename,"r+",encoding="utf-8") as file:
        file_data = json.load(file)
        file_data["pra_info"].append(new_data)
        file.seek(0)
        json.dump(file_data,file,indent=4)


nowy_prac = {
            "imie": "Paula",
            "nazwisko": "Nowak",
            "stanowisko": "sekretarka",
            "lata_pracy": 3,
            "email": "pnowak@firma.pl"
        }


dodaj_nowego_pracownika(nowy_prac)
