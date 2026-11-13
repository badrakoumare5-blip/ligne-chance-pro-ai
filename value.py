from engine.probabilities import implied_probability, expected_value, edge

def evaluate_market(name: str, odds: float, probability: float) -> dict:
    if odds <= 1:
        raise ValueError("Cote invalide : elle doit être supérieure à 1.00.")
    if not 0 <= probability <= 1:
        raise ValueError("Probabilité invalide : utiliser une valeur entre 0 et 1.")
    ev = expected_value(probability, odds)
    gap = edge(probability, odds)
    if ev >= 0.08 and gap >= 0.04:
        status = "VALUE POTENTIELLE"
        risk = "À vérifier"
    elif ev > 0:
        status = "AVANTAGE FAIBLE"
        risk = "Prudent"
    else:
        status = "PAS DE VALUE"
        risk = "À éviter"
    return {
        "marché": name,
        "cote": round(odds, 2),
        "probabilité_estimée": f"{probability*100:.1f}%",
        "probabilité_implicite_brute": f"{implied_probability(odds)*100:.1f}%",
        "écart": f"{gap*100:+.1f} points",
        "valeur_espérée": f"{ev*100:+.1f}%",
        "décision": status,
        "risque": risk,
        "avertissement": "Estimation à valider avec des données récentes et des cotes réellement disponibles."
    }
