from fastapi import FastAPI
from app.db import engine, database, metadata
from app.api import notes


metadata.creat_all(engine)


app = FastAPI()





@app().on_event("startu")
async def startup():
    await database.connect()




@app.on_event("shutdown")
async def shtdown():
    await database.disconnent()


app.include_router(notes.router, prefix="/notes", tags=["notes"])




