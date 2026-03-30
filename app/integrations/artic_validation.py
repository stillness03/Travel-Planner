import httpx
from app.schemas.schemas import PlaceCreate

ART_API_URL = "https://api.artic.edu/api/v1/artworks/{}"

async def fetch_artwork(external_id: int):
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            response = await client.get(
                ART_API_URL.format(external_id)
            )

        if response.status_code != 200:
            return None

        data = response.json()

        artwork = data.get("data")
        if not artwork:
            return None

        return artwork

    except httpx.RequestError:
        return None