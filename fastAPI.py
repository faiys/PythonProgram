# pip install fastAPI
# pip install fastAPI uvicorn
# uvicorn is fastapi runserver like that
# Run CMD uvicorn <module_name>:<app_variable> (uvicorn fastAPI:app --reload)

from fastapi import FastAPI

app = FastAPI()

# without async method
# http://127.0.0.1:8000/get?name=Mohamed
@app.get('/get')
def get(name:str):
    return {"message":f"Hello, {name}"}


# Async method
# pip install httpx
import httpx
import asyncio
HEADERS = {
    "Authorization": "Zoho-oauthtoken 1000.2da1828b30a49b659f7d196d00a00ee6.e8a0cd4128c3872a8db2b30a48150241",
    "orgId": "60036863801"
}
ticektIds = ["183086000026210215", "183086000026194232"]
@app.get("/ticket")
async def getHTTp():
    url = "https://desk.zoho.in/api/v1/tickets/"

    async with httpx.AsyncClient(timeout=10) as client:
        # Single api
        # resp = await client.get(url, headers=HEADERS)
        # resp.raise_for_status()
        # return resp.json()

        # multiple concurrenly api
        resp = await asyncio.gather(
            *[client.get(f'{url}{i}', headers=HEADERS ) for i in ticektIds],
            return_exceptions=True
        )
        return [j.json() for j in resp]


@app.get('/noasync')
def withoutAsync():
    op = []
    for i in ticektIds:
        url = f"https://desk.zoho.in/api/v1/tickets/{i}"
        client = httpx.Client()
        resp = client.get(url, headers=HEADERS)
        resp.raise_for_status()
        op.append(resp.json())
    return op