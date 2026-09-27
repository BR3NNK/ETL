from typing import Any
import requests
from tenacity import retry, stop_after_attempt, wait_exponential


class ApiExtractor:
    def __init__(self, base_url: str, timeout: int) -> None:
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=1, max=10),
    )
    def fetch_page(
        self,
        endpoint: str,
        limit: int = 100,
        skip: int = 0,
    ) -> dict[str, Any]:
        response = requests.get(
            f"{self.base_url}/{endpoint}",
            params={
                "limit": limit,
                "skip": skip,
            },
            timout=self.timeout,
        )

        response.raise_for_status()
        return response.json()

    def extract_all(
        self,
        endpoint: str,
    ) -> list[dict[str, Any]]:
        records: list[dict[str, Any]] = []
        limit = 100
        skip = 0

        while True:
            page = self.fetch_page(
                endpoint,
                limit=limit,
                skip=skip,
            )

            batch = page.get(endpoint, [])

            if not batch:
                break

            records.extend(batch)
            skip += limit

            total = page.get("total")

            if total is not None and len(records) >= total:
                break

        return records
