from api.serializers.vim_command import UpdateVimCommand, VimCommand
from api.services.vim_service import VimService
from fastapi import APIRouter


route = APIRouter()


@route.get("/", tags=["vim"])
async def get_data():
    return VimService().scan_item()


@route.post("/", tags=["vim"], status_code=201)
async def post_data(data: VimCommand):
    return VimService().add_data(data)


@route.delete("/{id}", tags=["vim"])
async def delete_data(id: str):
    return VimService().delete_data(id)


@route.put("/", tags=["vim"])
async def update_data(data: UpdateVimCommand):
    return VimService().update_data(data)
