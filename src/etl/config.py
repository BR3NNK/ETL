from dataclasses import dataclass
import os
from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class Settings:
    api_base_url: str
    database_url: str
    request_timeout: int
    raw_data_path: str


def load_settings() -> Settings:
    database_url = os.getenv("DATABASE_URL")

    if not database_url:
        raise RuntimeError("DATABASE_URL is not set")

    return Settings(
        api_base_url=os.getenv("API_BASE_URL", "https://dummyjson.com"),
        database_url=database_url,
        request_timeout=int(os.getenv("REQUEST_TIMEOUT", 30)),
        raw_data_path=os.getenv("RAW_DATA_PATH", "data/raw"),
    )
