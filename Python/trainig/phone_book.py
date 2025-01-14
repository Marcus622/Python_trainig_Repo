
Telefonbuch = {
    "Bernd": "0147 658 94 236",
    "Basti": "0147 621 94 236",
    "Sabine": "0147 658 84 257",
    "Susi": "0155 323 94 236",
    "Alf": "0182 758 94 991",
}
a = input("Welche Telefonnummer brauchst du? ")
if a in Telefonbuch:
    print(a, "Telefonnummer ist", Telefonbuch["Alf"])

else:
    print(a, "ist nicht in unserem Telefonbuch.")

del Telefonbuch[a]
print(a,"wurde gelöscht.")
print(Telefonbuch)

#print("Alfs Telefonnummer ist", Telefonbuch["Alf"])