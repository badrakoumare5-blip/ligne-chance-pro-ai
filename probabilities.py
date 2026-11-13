def implied_probability(odds: float) -> float:
    """Probabilité implicite brute d'une cote décimale."""
    if odds <= 1:
        raise ValueError("La cote doit être supérieure à 1.00.")
    return 1 / odds

def expected_value(probability: float, odds: float) -> float:
    """Valeur espérée nette par unité misée, avant marge/ajustements."""
    _validate_probability(probability)
    if odds <= 1:
        raise ValueError("La cote doit être supérieure à 1.00.")
    return probability * odds - 1

def edge(probability: float, odds: float) -> float:
    """Écart entre probabilité estimée et probabilité implicite brute."""
    return probability - implied_probability(odds)

def _validate_probability(probability: float):
    if not 0 <= probability <= 1:
        raise ValueError("La probabilité doit être comprise entre 0 et 1.")
