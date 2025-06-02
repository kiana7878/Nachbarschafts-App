#Nachbarschafts-App: Hilfsbörse
print("Willkommen bei der Hilfsbörse! Bitte schreiben Sie einfach ein Wort bei dem Sie Hilfe brauchen und Ihren Namen.") #Eine kleine Anleitung zum benutzen
eingabe = input("Wobei brauchen Sie Hilfe? :") #Es wird gefragt wobei man Hilfe braucht und wie man heißt.
name = input("Wie heißen Sie? :")

nachbarn = ["Tom", "Lilly", "Anabell", "Max", "Bernd", "Greta"] #Das ist die Liste der Nachbarn.
for i in range(0, len(nachbarn)):
    print("Liebe/-r " + nachbarn[i] + ",op " + name + " braucht ihre Hilfe bei/-m " + eingabe)
# In dieser Schleife wird pro Nachbar in der Liste eine Nachricht abgesendet die, die Frage beeinhaltet ob man Helfen möchte.   
    
for a in range(0, len(nachbarn)):    
    print("Wenn Sie helfen wollen antworten Sie mit Ja, wenn nicht mit Nein.") #Wieder eine kleine erklärung was man machen soll.
    antwort = input("Wollen Sie helfen? :")# Die Frage wird gestellt
    
    if antwort == "Ja" or antwort == "ja":
        print(nachbarn [a] + " will helfen.")
    elif antwort == "Nein" or antwort =="nein":
        print(nachbarn [a] + " will nicht helfen.")
    else:
        print("Ungültige Antwort.")
# In dieser Bedingten Anweisund wir kontroliert, welche Antwort man gegeben hat und je nach Antwort eine Aussage ausgegeben.