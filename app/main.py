from http import HTTPStatus

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.schemas import Message, UserDB, UserList, UserPublic, UserSchema

app = FastAPI()

templates = Jinja2Templates(directory='app/templates')

db = []


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def root():
    return {'message': 'Hello World!'}


@app.get(
    '/hello-world', status_code=HTTPStatus.OK, response_class=HTMLResponse
)
def hello_world(request: Request):
    return templates.TemplateResponse(
        'hello_world.html', {'request': request, 'message': 'Hello World!'}
    )


@app.get('/users/', status_code=HTTPStatus.OK, response_model=UserList)
def get_users():
    return {'users': db}


@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    user_with_id = UserDB(**user.model_dump(), id=len(db) + 1)

    db.append(user_with_id)
    return user_with_id


@app.put(
    '/users/{user_id}', status_code=HTTPStatus.OK, response_model=UserPublic
)
def update_user(user_id: int, user: UserSchema):
    user_with_id = UserDB(**user.model_dump(), id=user_id)

    if user_id < 1 or user_id > len(db):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='User not found',
        )

    db[user_id - 1] = user_with_id
    return user_with_id


@app.delete(
    '/users/{user_id}', status_code=HTTPStatus.OK, response_model=UserPublic
)
def delete_user(user_id: int):
    if user_id < 1 or user_id > len(db):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='User not found',
        )

    user = db.pop(user_id - 1)
    return user
