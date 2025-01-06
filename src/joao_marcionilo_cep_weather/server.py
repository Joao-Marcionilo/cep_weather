import uvicorn
from fastapi import FastAPI

from .models import capitals, CepData


def _launch(_get_data, _get_capital, _get_capital_weather):
    app = FastAPI(
        title="CEP & Weather API",
        description="Local server to test the script of this API",
        version="1.0",
        contact={
            "name": "João Marcionilo",
            "email": "marcionilojob@gmail.com",
        },
        license_info={
            "name": "MIT License",
            "url": "https://github.com/Joao-Marcionilo/cep-weather/blob/main/LICENSE",
        }
    )

    @app.get("/get_data/{cep}")
    async def get_data(cep:str) -> CepData:
        """
        Fetch a capital's data from another API.\n
        Caution: massive use for validation of local databases may block your access for an indefinite period.
        """
        return _get_data(cep)

    @app.get("/get_capital/{cep}")
    async def get_capital(cep:str) -> capitals:
        """
        Try to find the capital of a given CEP connecting to another API.\n
        Caution: massive use for validation of local databases may block your access for an indefinite period.
        """
        return _get_capital(cep)

    @app.get("/get_capital_weather/{capital}")
    async def get_capital_weather(capital:capitals) -> str:
        """Scrape for the weather of a capital"""
        return _get_capital_weather(capital)

    uvicorn.run(app, port=8000)
