from fastapi import FastAPI
from routers import categoty

app = FastAPI()


@app.get('/')
async def welcome():
    return {"message": "My shop"}


app.include_router(categoty.router)

# python -m uvicorn main:app
# cd app
