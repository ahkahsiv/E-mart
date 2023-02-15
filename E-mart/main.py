from fastapi import FastAPI
from configs.connection import DATABASE_URL
from fastapi import APIRouter, Request
from starlette.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, RedirectResponse
from user import routes as AdminRoute
from tortoise.contrib.fastapi import register_tortoise


app=FastAPI()

db_url=DATABASE_URL()

templates=Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


app.include_router(AdminRoute.router,tags=["Admin"])

register_tortoise(
    app,
    db_url=db_url,
    modules={'models':['user.models']},
    generate_schemas  = True,
    add_exception_handlers =True
)