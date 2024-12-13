import uvicorn
from fastapi import FastAPI

from api.config.env import env


app = FastAPI(debug=env.debug)


@app.get("/")
def read_root():
    return {"Hello": "World"}


def run():
    uvicorn.run(app, host="0.0.0.0", port=8000)
