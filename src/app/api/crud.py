from app.api.models import NoteSchema
from app.db import notes, database



async def post(playload: NoteSchema):
    query = notes.insert().values(title=playload.title, description=playload.description)
    return await database.execute(query=query)