#Nachbarschafts-App: Hilfsbörse
print("Willkommen bei der Hilfsbörse! Bitte schreiben Sie einfach einen Satz mit ihrem Namen und wobei Sie Hilfe brauchen.")
eingabe = input("Wobei brauchen Sie Hilfe? :")
name = input("Wie heißen Sie? :")

nachbarn = ["Tom", "Lilly", "Anabell", "Max", "Bernd", "Greta"]
for i in range(0, len(nachbarn)):
    print("Liebe/-r " + nachbarn[i] + ",op " + name + " braucht ihre Hilfe bei/-m " + eingabe)
    
print("Wenn Sie helfen wollen antworten Sie mit Ja, wenn nicht mit Nein.")
antwort = input("Wollen Sie helfen? :")
if antwort == "Nein" or "nein" :
    print(nachbarn[0] + " wollte nicht helfen.")
elif antwort == "Ja" or "ja":
    print(nachbarn[0] + " wollte helfen.")


# ich muss das so machen dass es eine liste gibt in der alle nachbaren sind und dann eine zählschleife gibt die nachbarn mal die nachricht an die nachbarn weitergibt
#die nachricht musst individuell geschickt werden können in der zweiten stuffe wenn man zum bsp beim einkaufen hilfe braucht werden nur leute unter 30 angefragt
# kann man mit namen speichern und lesen lassen und nur dennen wird geschickt