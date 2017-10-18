"""
1. napiste program v pythone

- vypisete text: aka je vonku teplota?
- zadate vstup (cislo)
- vyhodnotite ak je teplota vyssie ako 25 tak vypiste: "zober si tricko. "
                ak nie vypiste:  "Zobrer si aj sveter. "

- na konci vypiste: "Mozes ist vonku"

mozne riesenie:
"""
temperature = float(input('What is the temperature? '))

if temperature > 25:
    print('Wear shorts.')
else:
    print('Wear long pants.')
print('Get some exercise outside.')

# podobna uloha - oblubene jedlo
food = 'pizza'
if food == 'pizza':
    print('Ummmm, my favorite!')
    print('I feel like saying it 100 times...')
    # print(100 * (food + '! '))

"""
2. Napiste program v pyhone, ktory po zadani poctu bodov vypise znamku.
 Max pocet bodov za test je 100, napiste metodu ktora vyhodnoti vysledky kde
 A >= 90, B >= 80, C >= 70, >= 60, E >= 50 inak Fx
- pouzite elif
"""
def letterGrade(score):
    if score >= 90:
        letter = 'A'
    elif score >= 80:
        letter = 'B'
    elif score >= 70:
        letter = 'C'
    elif score >= 60:
        letter = 'D'
    elif score >= 50:
        letter = 'E'
    else:
        letter = 'F'
    return letter


""" 3. Vypiste cisla 0,1,2,3,4, pouzitim for """
# Prints out the numbers 0,1,2,3,4
for x in range(5):
    print(x)

"""
4. Vypiste cisla 0,1,2,3,4, pouzitim while
hint: pouzite pocitadlo
"""
count = 0
while count < 5:
    print(count)
    count += 1  # This is the same as count = count + 1


"""
5. Vypiste cisla 0,1,2,3,4, pouzitim while a break
hint: pouzite pocitadlo
"""
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

"""
6. Vypiste len parne cisla, hint: pouzite continue a % (zvysok po deleni), vypiste len cisla mensie ako 15
"""
# Prints out only odd numbers - 1,3,5,7,9 - len parne - pouzitie continue
for x in range(15):
    # Check if x is even
    if x % 2 == 0:
        continue
    print(x)

""" ukazka printu premennej. """
for x in range(0, 3):
    print("We're on time %d" % x)
