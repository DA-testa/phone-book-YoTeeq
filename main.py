import json

# Ielasa JSON datni no faila
with open('sample1.json') as f:
    datne = json.load(f)

# Pārveido datus par vārdnīcu
vardnica = dict(datne)

# Izvada vārdnīcas garumu
print(len(vardnica))

# Izvada visas vārdnīcas atslēgas
print(list(vardnica.keys()))

# Izvada visas vārdnīcas vērtības
print(list(vardnica.values()))

# Ielasīs atslēgu no ievades
atslega = input('Ievadi atslēgu: ')

# Parbauda, vai atslēga eksistē vārdnīcā un izvada tās vērtību
if atslega in vardnica:
    print(vardnica[atslega])
else:
    print('Atslēga neeksistē vārdnīcā')

# Definē funkciju, kas izvada vērtību, kura atrodas dotajā atslēgā
def atslegas_vertiba(datnes_nosaukums, atslega):
    with open(datnes_nosaukums) as f:
        datne = json.load(f)
    vardnica = dict(datne)
    if atslega in vardnica:
        print(vardnica[atslega])
    else:
        print('Atslēga neeksistē vārdnīcā')

# Izmanto funkciju, lai izvadītu vērtību, kas atrodas dotajā atslēgā
atslegas_vertiba("sample1.json", "color")