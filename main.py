import requests
import random

def get_citation():
    try:
        response = requests.get("https://zenquotes.io/api/quotes")
        if response.status_code == 200:
            citations = response.json()
            citation_choisie = random.choice(citations)
            texte = citation_choisie['q']
            auteur = citation_choisie['a']
            return f"\"{texte}\" - {auteur}"
        else:
            return "Erreur de récupération des citations."
    except Exception as e:
        return f"Erreur : {e}"

def main():
    print("🌟 Bienvenue dans Inspir Quote Generator (Version API) 🌟")
    continuer = 'o'
    while continuer.lower() == 'o':
        citation = get_citation()
        print(f"\n📜 {citation}\n")
        continuer = input("🔄 Veux-tu une autre citation ? (o/n) : ")

    print("\n🙏 Merci d'avoir utilisé Inspir Quote Generator. Continue de t'inspirer chaque jour ! ✨")

if __name__ == "__main__":
    main()
