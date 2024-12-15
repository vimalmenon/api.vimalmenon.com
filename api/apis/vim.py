from fastapi import APIRouter

from api.services.vim_service import VimService
from api.serializers.vim_command import VimCommand, DeleteVimCommand, UpdateVimCommand


route = APIRouter()


@route.get("/", tags=["vim"])
async def get_data():
    return VimService().scan_item()


@route.post("/", tags=["vim"])
async def post_data(data: VimCommand):
    return VimService().add_data(data)


@route.delete("/", tags=["vim"])
async def delete_data(data: DeleteVimCommand):
    return VimService().delete_data(data)


@route.put("/", tags=["vim"])
async def update_data(data: UpdateVimCommand):
    return VimService().update_data()
