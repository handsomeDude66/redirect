from fastapi import FastAPI
from starlette.responses import RedirectResponse

app = FastAPI()

@app.get("/landing")
def redirect_to_url(schema: str):
    response = RedirectResponse(url=schema)
    return response
