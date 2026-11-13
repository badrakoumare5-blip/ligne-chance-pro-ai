"""Connecteur vers les données publiques NHL. Vérifier le schéma des réponses à chaque mise à jour."""
import requests
from config import REQUEST_TIMEOUT

class NHLAPIError(RuntimeError):
    pass

class NHLAPI:
    BASE = "https://api-web.nhle.com/v1"

    def get(self, path: str):
        response = requests.get(
            f"{self.BASE}/{path.lstrip('/')}",
            timeout=REQUEST_TIMEOUT,
            headers={"User-Agent": "LigneChanceProAI/0.1"},
        )
        response.raise_for_status()
        try:
            return response.json()
        except ValueError as exc:
            raise NHLAPIError("Réponse NHL non JSON.") from exc

    def scoreboard_now(self):
        return self.get("score/now")

    def club_schedule(self, team_abbrev: str):
        return self.get(f"club-stats/{team_abbrev.upper()}/now")
