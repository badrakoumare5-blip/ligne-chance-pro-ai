from football.analysis import analyze_markets as analyze_football
from nhl.analysis import analyze_player_market as analyze_nhl

def main():
    print("=== LIGNE CHANCE PRO AI ===")
    print("1. Football | 2. NHL")
    choice = input("Choix : ").strip()
    if choice == "1":
        print("\nFootball : moteur d'analyse des marchés")
        print("Ce premier socle calcule les probabilités à partir de données vérifiées saisies.")
        odds = float(input("Cote Betclic (ex. 1.85) : "))
        probability = float(input("Probabilité estimée en % (ex. 58) : ")) / 100
        result = analyze_football("Marché choisi", odds, probability)
        print(result)
    elif choice == "2":
        print("\nNHL : marchés individuels (buteur, passeur, tirs)")
        market = input("Marché (buteur/passeur/tirs) : ").strip()
        odds = float(input("Cote Betclic : "))
        probability = float(input("Probabilité estimée en % : ")) / 100
        print(analyze_nhl(market, odds, probability))
    else:
        print("Choix invalide.")

if __name__ == "__main__":
    main()
