from fastapi import APIRouter, HTTPExeption, Path

from app.api import crud
from app.api.models import NoteDB, NoteSchema

from tying import List

router = APIRouter()



@router.post("/", response_model=NoteDB, status_code=201)
async def creat_note(playload: NoteSchema):
    note_id = await crud.post(playload)

    response_object = {
        "id": note_id,
        "title": playload.title,
        "description": playload.description,
    }

    return response_object



@router.get("/{id}", response_model=NoteDB)
async def read_not(id:int = Path(..., gt=0),):
    note = await crud.get(id)

    if not note:
        raise HTTPExeption(status_code=404, detail="Note not found")
    
    return note


@router.get("/", response_model=List[NoteDB])
async def read_all_notes():
    return await crud.get_all()


@router.put("/{id}", response_model=NoteDB)
async def update_note(playload:NoteSchema, id:int = Path(..., gt=0),):
    note = await crud.get(id)
    if not note:
        raise HTTPExeption(status_code=404, detail="Note not faund")
    
    not_id = await crud.put(id, playload)

    response_object = {
        "id" : not_id,
        "title" : playload.title,
        "description" : playload.description
    }

    return response_object

@router.delete("/{id}", response_model=NoteDB)
async def delete_note(id:int = Path(..., gt=0)):
    note = await crud.get(id)
    if not note:
        raise HTTPExeption(status_code=404, detail="Note not faund")
    
    await crud.delete(id)

    return note