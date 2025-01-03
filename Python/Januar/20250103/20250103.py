# 1. Erstelle ein Python-Programm, in dem die Teilnehmer ein Dictionary erstellen. Das Dictionary soll mindestens 10 deutsche Wörter mit ihren englischen Übersetzungen enthalten.
#2. Danach soll das Programm den Benutzer per Eingabe (input) fragen, welches deutsche Wort ins Englische übersetzt werden soll.
#  Falls das Wort nicht im Dictionary ist, soll eine entsprechende Fehlermeldung angezeigt werden.

# woerterbuch = {
#     "kartoffel": "potato", 
#     "ameise": "ant", 
#     "ei": "egg",
#     "biene": "bee",
#     "affe": "monkey",
#     "buch": "book",
#     "garten": "garden",
#     "lehrer": "teacher",
#     "himmel": "sky",
#     "baum" : "tree",
#     }

# benutzereingabe = input("Gib ein Wort zur Übersetzung ein: ") .lower()
# print(f"Die Übersetzung von {benutzereingabe} lautet {woerterbuch[benutzereingabe]}")

# my_dict = {"apfel": "Apple", "wörterbuch": "dictionary"}
# my_userinput = input("Gib ein deutsches Wort ein: ")
# if my_userinput in my_dict:
#     print(f"Die Übersetzung zu {my_userinput} ist {my_dict[my_userinput]}")
# else:
#     actual_translation = input(
#         "Das Wort gibt es noch nicht, gib die engl. Übersetzung ein: "
#     )
#     my_dict[my_userinput] = actual_translation
#     print(f"Die Übersetzung zu {my_userinput} ist {my_dict[my_userinput]}")

def translate(german_word):
    my_dict = {"Apfel":"apple", "Wörterbuch": "dictionary" }

    if german_word in my_dict:
        print("Die Übersetzung zu {german_word} ist {my_dict[german_word]}" )

    else:
        actual_translation = input("Das Wort gibt es noch nicht, gib die engl. Übersetzung ein: ")
        my_dict[german_word] = actual_translation
        print(f"Die Übersetzung zu {german_word} ist {my_dict[german_word]}")

my_userinput = input("Gib ein deutsches Wort ein: ")
if my_userinput == "exit":
    print("I am not going to translate anything.")
else:
    translate(my_userinput)