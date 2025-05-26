#Nachbarschafts-App: Hilfsbörse
print("Willkommen bei der Hilfsbörse! Bitte schreiben Sie einfach ein Wort bei dem Sie Hilfe brauchen und Ihren Namen.")
eingabe = input("Wobei brauchen Sie Hilfe? :")
name = input("Wie heißen Sie? :")

nachbarn = ["Tom", "Lilly", "Anabell", "Max", "Bernd", "Greta"]
for i in range(0, len(nachbarn)):
    print("Liebe/-r " + nachbarn[i] + ",op " + name + " braucht ihre Hilfe bei/-m " + eingabe)
    
    
for a in range(0, len(nachbarn)):    
    print("Wenn Sie helfen wollen antworten Sie mit Ja, wenn nicht mit Nein.")
    antwort = input("Wollen Sie helfen? :")
    
    if antwort == "Ja" or antwort == "ja":
        print(nachbarn [a] + " will helfen.")
    elif antwort == "Nein" or antwort =="nein":
        print(nachbarn [a] + " will nicht helfen.")
    else:
        print("Ungültige Antwort.")
