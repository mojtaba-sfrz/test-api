from fastapi import APIRouter, HTTPExeption

from app.api import crud
from app.api.models import NoteDB, NoteSchema


router = APIRouter()



@router.post("/", response_model=NoteDB, status_code=201)
async def creat_note(plauload: Noteschema):
    note_id = await crud.post(playload)

    response_object = {
        "id": note_id,
        "title": playload.title,
        "description": playload.description,
    }

    return response_object

