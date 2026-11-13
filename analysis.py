from engine.value import evaluate_market
from nhl.markets import NHL_MARKETS

def analyze_player_market(market: str, odds: float, probability: float) -> dict:
    key = market.lower().strip()
    if key not in NHL_MARKETS:
        raise ValueError("Marché NHL non reconnu. Choisir buteur, passeur ou tirs.")
    return evaluate_market(NHL_MARKETS[key], odds, probability)
