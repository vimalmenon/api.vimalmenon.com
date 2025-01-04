import uvicorn
from api.apis.link import route as link_router
from api.apis.vim import route as vim_route
from api.config.env import env
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(debug=env.debug)

app.include_router(vim_route, prefix="/vim")
app.include_router(link_router, prefix="/links")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


def run():
    uvicorn.run(app, host="0.0.0.0", port=8000)
