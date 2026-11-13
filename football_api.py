"""Connecteur API-Football. Aucune donnée n'est simulée."""
import requests
from config import API_FOOTBALL_KEY, API_FOOTBALL_HOST, REQUEST_TIMEOUT

class FootballAPIError(RuntimeError):
    pass

class FootballAPI:
    def __init__(self):
        if not API_FOOTBALL_KEY:
            raise FootballAPIError(
                "Clé API absente. Ajoutez API_FOOTBALL_KEY dans le fichier .env."
            )
        self.base_url = f"https://{API_FOOTBALL_HOST}/"
        self.headers = {"x-apisports-key": API_FOOTBALL_KEY}

    def get(self, endpoint: str, **params):
        response = requests.get(
            self.base_url + endpoint.lstrip("/"),
            headers=self.headers,
            params=params,
            timeout=REQUEST_TIMEOUT,
        )
        response.raise_for_status()
        payload = response.json()
        if payload.get("errors"):
            raise FootballAPIError(f"Erreur API-Football : {payload['errors']}")
        return payload

    def fixtures_by_date(self, date: str, league: int | None = None, season: int | None = None):
        params = {"date": date}
        if league is not None:
            params["league"] = league
        if season is not None:
            params["season"] = season
        return self.get("fixtures", **params)

    def fixture_statistics(self, fixture_id: int):
        return self.get("fixtures/statistics", fixture=fixture_id)

    def fixture_events(self, fixture_id: int):
        return self.get("fixtures/events", fixture=fixture_id)

    def fixture_lineups(self, fixture_id: int):
        return self.get("fixtures/lineups", fixture=fixture_id)
