from fastapi import FastAPI , Form , Request , Response
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pathlib import Path
from pydantic import BaseModel
from typing import Literal

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI()

templates = Jinja2Templates(directory=str(BASE_DIR/"templates"))

class Temp(BaseModel) : 
    temparature : float 
    unit : Literal["celsius" , "fahrenheit" , "kelvin"]

def celc_to_far(c):
    return (c * 9/5) + 32

def far_to_celc(f):
    return (f - 32) * 5/9

def celc_to_kelvin(c):
    return c + 273.15

def kelvin_to_celc(k):
    return k - 273.15

def far_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_far(k):
    return (k - 273.15) * 9/5 + 32


def feet_to_meter(f):
    return f * 0.3048

def meter_to_feet(m):
    return m / 0.3048


def kg_to_pound(kg):
    return kg * 2.20462

def pound_to_kg(lb):
    return lb / 2.20462


@app.get("/", response_class=HTMLResponse)
def Home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )


@app.post("/temp" , response_class=HTMLResponse)
def tempConvert(request : Request , temp_input : float = Form(...) , tempUnit : str = Form(...) , toConvert :  str = Form(...)):
    value = temp_input
    unit = tempUnit
    unitForConvert = toConvert

    if (unit == "celsius") and (unitForConvert == "fahrenheit"):
        result = celc_to_far(value)
    elif (unit == "celsius") and (unitForConvert == "kelvin"):
        result = celc_to_kelvin(value)
    elif (unit == "fahrenheit") and (unitForConvert == "celsius"):
        result = far_to_celc(value)
    elif (unit == "fahrenheit") and (unitForConvert == "kelvin"):
        result = far_to_kelvin(value)
    elif (unit == "kelvin") and (unitForConvert == "celsius"):
        result = kelvin_to_celc(value)
    elif (unit == "kelvin") and (unitForConvert == "fahrenheit"):
        result = kelvin_to_far(value)
    elif (unit == "--select--") or (unitForConvert == "--select--"):
        result = "select a type first"
    else :
        result = 0
    
    return templates.TemplateResponse(
    "index.html",
    {
        "request": request,
        "result": result,
        "active": "temperature",
        "tempUnit": tempUnit,
        "toConvert": toConvert
    }
)



@app.post("/height", response_class=HTMLResponse)
def heightConvert(
    request: Request,
    height_input: float = Form(...),
    heightUnit: str = Form(...),
    heightToConvert: str = Form(...)
):
    value = height_input
    unit = heightUnit
    to = heightToConvert

    if (unit == "feet") and (to == "meter"):
        result = feet_to_meter(value)

    elif (unit == "meter") and (to == "feet"):
        result = meter_to_feet(value)

    elif (unit == "feet") and (to == "inch"):
        result = value * 12

    elif (unit == "inch") and (to == "feet"):
        result = value / 12

    elif (unit == "meter") and (to == "inch"):
        result = value * 39.3701

    elif (unit == "inch") and (to == "meter"):
        result = value / 39.3701

    elif (unit == "0") or (to == "0"):
        result = "select a type first"

    elif unit == to:
        result = "same unit bro 😐"

    else:
        result = 0

    return templates.TemplateResponse(
    "index.html",
    {
        "request": request,
        "resultHeight": result,
        "active": "height",
        "heightUnit": heightUnit,
        "heightToConvert": heightToConvert
    }
)


@app.post("/weight", response_class=HTMLResponse)
def weightConvert(
    request: Request,
    weight_input: float = Form(...),
    weightUnit: str = Form(...),
    weightToConvert: str = Form(...)
):
    value = weight_input
    unit = weightUnit
    to = weightToConvert

    if (unit == "kg") and (to == "pound"):
        result = kg_to_pound(value)

    elif (unit == "pound") and (to == "kg"):
        result = pound_to_kg(value)

    elif (unit == "kg") and (to == "gram"):
        result = value * 1000

    elif (unit == "gram") and (to == "kg"):
        result = value / 1000

    elif (unit == "pound") and (to == "gram"):
        result = value * 453.592

    elif (unit == "gram") and (to == "pound"):
        result = value / 453.592

    elif (unit == "0") or (to == "0"):
        result = "select a type first"

    elif unit == to:
        result = "same unit bro 😐"

    else:
        result = 0

    return templates.TemplateResponse(
    "index.html",
    {
        "request": request,
        "resultWeight": result,
        "active": "weight",
        "weightUnit": weightUnit,
        "weightToConvert": weightToConvert
    }
)