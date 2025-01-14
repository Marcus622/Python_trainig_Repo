# Schreibe eine Funktion miles_to_kilometer(m), die amerikanische Meilen (m) in 
# Kilometer umrechnet (eine Meile sind 1.60934 Km)

def miles_kilometer(miles):
    result = miles * 1.60934    
    return result
  

miles = 200
variable = miles_kilometer(miles)
print(f"Die {miles} Meilen sind {variable} Km")

# Schreibe eine Funktion kilometer_to_miles(km), die das ganze andersherum betrachtet.

def kilometer_miles(km):
    result = km / 1.60934
    return result

km = 100
variable1 = kilometer_miles(km)
print(f"Die {km} Km sind {variable1} Meilen")
