# strecke_in_Km = 8

# if strecke_in_Km < 7:
#     print("Geh doch zu Fuss.")
# elif strecke_in_Km == 7:
#     print("Nimm gute Schuhe mit.")
#     print("Der Weg ist steinig.")


# else:
#     print("Nimm das Fahrrad.")

alter = int(input("Bitte geben Sie ihr Alter ein: "))
anzahl= int(input(F"Wieviele Tickets möchtest Du kaufen? "))

if alter > 65:
    print(7.5 * anzahl)
elif alter >= 18:
    print(10 * anzahl)
else:
    print(5 * anzahl)