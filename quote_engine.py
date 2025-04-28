import random
import os
import requests

class Generator_Citation:

    @classmethod
    def lire_citations_fichier(cls, fichier):
        """Lit les citations d'un fichier texte."""
        try:
            with open(fichier, "r", encoding="utf-8") as f:
                citations = [ligne.strip() for ligne in f if ligne.strip()]
            return citations
        except FileNotFoundError:
            return None

    @classmethod
    def charger_citations(cls):
        """Charge les citations depuis un fichier ou une liste locale."""
        fichier = "citations_fr.txt"
        if os.path.exists(fichier):
            print("📚 Chargement des citations depuis le fichier...")
            citations = cls.lire_citations_fichier(fichier)
        else:
            print("📝 Aucune base externe trouvée, utilisation des citations internes.")
            citations = [
                "La vie commence là où commence ta zone d’inconfort.",
                "Ne rêve pas ta vie, vis tes rêves.",
                "Le succès est la somme de petits efforts répétés jour après jour.",
                "Celui qui déplace une montagne commence par déplacer de petites pierres.",
                "N'attends pas que l'opportunité vienne frapper à ta porte, construis-la.",
                "La persévérance transforme les petites gouttes en océans.",
                "C’est en échouant que l’on apprend à mieux réussir."
            ]
        return citations

    @classmethod
    def get_citation(cls):
        """Récupère une citation depuis l'API ZenQuotes."""
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

    @classmethod
    def update(cls):
        """Demande à l'utilisateur s'il veut des citations françaises."""
        reponse = input("Souhaites-tu des citations en français ? (o/n) : ")
        YES = 1 if reponse.lower() in ['o', 'oui', 'y', 'yes'] else 0
        return YES

    @classmethod
    def afficher_citation(cls, citation):
        """Affiche proprement une citation."""
        print("\n📜 Citation du jour :")
        print(f"{citation}\n")


def main():
    gen = Generator_Citation()

    print("🌟 Bienvenue dans Inspir Quote Generator (Version Fusionnée) 🌟")

    mode_fr = gen.update()  # 1 = FR, 0 = API (anglais)

    continuer = 'o'
    while continuer.lower() == 'o':
        if mode_fr:
            citations = gen.charger_citations()
            citation = random.choice(citations)
            gen.afficher_citation(citation)
        else:
            citation = gen.get_citation()
            gen.afficher_citation(citation)

        continuer = input("🔄 Veux-tu une autre citation ? (o/n) : ")

    print("\n🙏 Merci d'avoir utilisé Inspir Quote Generator. Continue de t'inspirer chaque jour ! ✨")

if __name__ == "__main__":
    main()
