
todos = []

for _ in range(100000):

    print("Was willst Du tun? ")
    print("(1) To-dos anzeigen")
    print("(2) To-dos hinzufügen")

    option = input("Bitte auswählen: ")

    if int(option) == 1:
        print("Meine Liste hat diese Elemente:")

        for todo in todos: 
            print(f" - {todo}")

    if int(option) == 2:
        newitem = input("Was möchtest du deiner Liste hinzufügen? ")
        todos.append(newitem)
    
print("")
print("")

print("Programm beendet.")