def git_befehl_uebersicht(befehl):
    git_befehle = {
        "git init": "Initialisiert ein neues Git-Repository im aktuellen Verzeichnis.",
        "git clone": "Kopiert ein bestehendes Git-Repository von einer URL auf deinen lokalen Computer.",
        "git pull": "Holt die neuesten Änderungen von einem entfernten Repository und integriert diese in dein lokales Repository.",
        "git push": "Überträgt deine lokalen Änderungen in ein entferntes Repository.",
        "git commit": "Speichert Änderungen im lokalen Repository mit einer Nachricht, die beschreibt, was geändert wurde.",
        "git status": "Zeigt den aktuellen Status deines Arbeitsverzeichnisses und der Staging-Area an.",
        "git add": "Fügt Änderungen der Staging-Area hinzu, um sie für den nächsten Commit vorzubereiten.",
        "git branch": "Listet die bestehenden Branches auf oder erstellt einen neuen Branch.",
        "git merge": "Führt Änderungen aus einem anderen Branch in den aktuellen Branch zusammen.",
        "git log": "Zeigt die Historie der Commits im aktuellen Repository an.",
        "git reset": "Setzt Änderungen im Repository oder in der Staging-Area zurück.",
        "git remote": "Verwaltet entfernte Repositories, z. B. zum Hinzufügen oder Entfernen eines Remote-Repositories."
    }

    befehl = befehl.lower()  # Sicherstellen, dass die Eingabe klein geschrieben wird, um das Wörterbuch abzugleichen.

    if befehl in git_befehle:
        print(f"Beschreibung von '{befehl}': {git_befehle[befehl]}")
    else:
        print(f"Der Befehl '{befehl}' ist nicht im Git-Befehl-Wörterbuch vorhanden.")

# Benutzeranfrage:
benutzereingabe = input("Gib einen Git-Befehl ein, um mehr darüber zu erfahren (z.B. 'git pull'): ")

git_befehl_uebersicht(benutzereingabe)
