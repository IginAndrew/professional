from fastapi import FastAPI, HTTPException, status

app = FastAPI()

doc = [
    {
        "id": 1,
        "title": "",
        "date_created": "2024-05-01 14:44:44",
        "date_updated": "2024-05-01 14:44:44",
        "category": "",
        "has_comments": 'true'
    },
]

comment = [
    {
        "id": 1,
        "document_id": 1,
        "text": "Hello world",
        "date_created": "2024-05-01 14:44:44",
        "date_updated": "2024-05-01 14:44:44",
        "author": {
            "name": "Петров Петр",
            "position": "Администратор"
        }
    },
]

error= [
{
"timestamp": 1716767880,
    "message": "Не найдены комментарии для документа",
"errorCode": "2344", #код должен быть больше 1000
},
]


@app.get("/")
async def welcome() -> dict:
    return {"message": "My professional API"}

@app.get("/api/v1/Documents")
async def get_documents():
    return doc

@app.get("/api/v1/Document/{documentId}/Comments")
async def get_documents_id(documentId: int):
    if documentId == doc[0]["id"]:
        return comment
    else:
        raise HTTPException(status_code=404, detail=error[0])

@app.post("/api/v1/Document/{documentId}/Comment")
async def create_documents_id(documentId: int):
    if documentId == doc[0]["id"]:
        comment.insert(0, {"id": int(comment[0]["id"] + 1), "document_id": documentId,
                       "text": "Hello world","date_created": "2024-05-01 14:44:44",
                       "date_updated": "2024-05-01 14:44:44",
                       "author": {"name": "Петров Петр", "position": "Администратор"}})
        return comment
    else:
        raise HTTPException(status_code=404, detail=error[0])


'''uvicorn main:app --reload''' #запуск сервера
'''http://127.0.0.1:8000/docs#/''' #посмотреть документацию
