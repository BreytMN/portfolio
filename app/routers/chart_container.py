from __init__ import templates_directory

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from charts.charts import get_movies

router = APIRouter()
templates = Jinja2Templates(directory=templates_directory)


@router.get("/chart_container", response_class=HTMLResponse)
async def chart_container(request: Request, item: str):

    name = "partials/chart_container.html"
    context = {
        "request": request,
        "item": item,
    }

    return templates.TemplateResponse(name=name, context=context)


@router.get("/chart", response_class=HTMLResponse)
async def chart(request: Request, item: str):

    chart = await get_movies()

    vega_embed = f"""
    <script>
        vegaEmbed(
            "#chart-container",
            {chart.to_json()},
            {{
                mode: "vega-lite",
            }},
        );
    </script>
    """

    return vega_embed
