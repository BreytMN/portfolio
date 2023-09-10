from __init__ import __title__, templates_directory

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory=templates_directory)


database = {
    "menu_items": ["Home", "About", "Forecast", "Interactive"],
    "chart_items": ["Forecast", "Interactive"]
}


@router.get("/", response_class=HTMLResponse)
async def root(request: Request, item: str = "Home"):

    name = "index.html"
    context = {
        "request": request,
        "title": __title__,
        "item": item,
    }

    return templates.TemplateResponse(name=name, context=context)


@router.get("/content", response_class=HTMLResponse)
async def content(request: Request, item: str = "Home"):

    chart_items = database["chart_items"]

    name = "partials/content.html"
    context = {
        "request": request,
        "chart_items": chart_items,
        "item": item,
    }

    return templates.TemplateResponse(name=name, context=context)


@router.get("/menu", response_class=HTMLResponse)
async def menu(request: Request, selected_item: str = "Home"):

    menu_items = database["menu_items"]

    name = "partials/menu.html"
    context = {
        "request": request,
        "menu_items": menu_items,
        "selected_item": selected_item,
    }

    return templates.TemplateResponse(name=name, context=context)
