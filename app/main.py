from http import HTTPStatus

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.schemas import Message

app = FastAPI()

templates = Jinja2Templates(directory='app/templates')


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
