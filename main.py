from fastapi import FastAPI, HTTPException, status

app = FastAPI()


@app.get("/")
async def welcome() -> dict:
    return {"message": "My professional API"}


"""uvicorn main:app --reload"""