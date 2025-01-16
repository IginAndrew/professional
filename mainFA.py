from fastapi import FastAPI, HTTPException

app = FastAPI()

doc = [
    {
"id": 1,
"title": "",
"date_created": "2024-05-01 14:44:44",
"date_updated": "2024-05-01 14:44:44",
"category": "",
"has_comments": True
}
]

com = [
    {
"id": 1,
"document_id": 1,
"text": "Hello world",
"date_created": "2024-05-01 14:44:44",
"date_updated": "2024-05-01 14:44:44",
"author": {
"name": "Петров Петр",
"position": "Администратор"
}}
]

er = [
{
"timestamp": 1716767880,
"message": "Не найдены комментарии для документа",
"errorCode": "2344"}
]


@app.get("/")
def home():
    return {"message": "Hello World"}

@app.get("/api/v1/Documents")
def documents():
    return doc

@app.get("/api/v1/Documents/{document_id}/Comments")
def comments(document_id: int):
    if document_id == doc[0]["id"]:
        return com
    else:
        raise HTTPException(status_code=404, detail=er[0])

@app.post("/api/v1/Documents/{document_id}/Comment")
def comment(document_id: int,text:str, date_created:str, date_updated:str, name:str, position:str):
    if document_id == doc[0]["id"]:
        com.append({
            "id": 2,
            "document_id": document_id,
            "text": text,
            "date_created": date_created,
            "date_updated": date_updated,
            "author": {
                "name": name,
                "position": position
            }
        })
        return com
    else:
        raise HTTPException(status_code=404, detail=er[0])


