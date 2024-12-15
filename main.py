from datetime import datetime, timedelta

from fastapi import FastAPI, HTTPException, status, Depends

from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
import jwt

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")
SECRET_KEY = "a21679097c1ba42e9bd06eea239cdc5bf19b249e87698625cba5e3572f005544"
ALGORITHM = "HS256"
bcrypt_context = CryptContext(
    schemes=["bcrypt"], deprecated="auto"
)  # шифрование пароля

name = [
    {"name": "Andrew", "password": bcrypt_context.hash("1234")},
]

doc = [
    {
        "id": 1,
        "title": "",
        "date_created": "2024-05-01 14:44:44",
        "date_updated": "2024-05-01 14:44:44",
        "category": "",
        "has_comments": "true",
    },
]

comment = [
    {
        "id": 1,
        "document_id": 1,
        "text": "Hello world",
        "date_created": "2024-05-01 14:44:44",
        "date_updated": "2024-05-01 14:44:44",
        "author": {"name": "Петров Петр", "position": "Администратор"},
    },
]

error = [
    {
        "timestamp": 1716767880,
        "message": "Не найдены комментарии для документа",
        "errorCode": "2344",  # код должен быть больше 1000
    },
]


@app.get("/")
async def welcome() -> dict:
    return {"message": "My professional API"}


def authanticate_user(username: str, password: str):
    if username == name[0]["name"] and bcrypt_context.verify(
            password, name[0]["password"]
    ):
        return name[0]
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )


def create_access_token(username: str):
    encode = {"name": username}
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)


def get_current_user(
        token: str = Depends(oauth2_scheme),
):  # которая декодирует наш JWT токен
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("name")
        if username is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate user",
            )

        return {
            "name": username,
        }
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate user"
        )


@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authanticate_user(form_data.username, form_data.password)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate user"
        )

    token = create_access_token(
        user["name"],
    )
    return {"access_token": token, "token_type": "bearer"}


@app.get("/read_current_user")
def read_current_user(user: str = Depends(get_current_user)):
    return {"User": user}


@app.get("/api/v1/Documents")
async def get_documents(get_user: dict = Depends(get_current_user)):
    if get_user:
        return doc
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="You are authorized to use this method",
        )


@app.get("/api/v1/Document/{documentId}/Comments")
async def get_documents_id(documentId: int, get_user: dict = Depends(get_current_user)):
    if get_user:
        if documentId == doc[0]["id"]:
            return comment
        else:
            raise HTTPException(status_code=404, detail=error[0])
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="You are authorized to use this method",
        )


@app.post("/api/v1/Document/{documentId}/Comment")
async def create_documents_id(
        documentId: int, text: str, date_created: str, date_updated: str, author: dict,
        get_user: dict = Depends(get_current_user)
):
    if get_user:
        if documentId == doc[0]["id"]:
            comment.insert(
                0,
                {
                    "id": int(comment[0]["id"] + 1),
                    "document_id": documentId,
                    "text": text,
                    "date_created": date_created,
                    "date_updated": date_updated,
                    "author": author,
                },
            )
            return comment
        else:
            raise HTTPException(status_code=404, detail=error[0])
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="You are authorized to use this method",
        )


"""uvicorn main:app --reload"""  # запуск сервера
"""http://127.0.0.1:8000/docs#/"""  # посмотреть документацию
