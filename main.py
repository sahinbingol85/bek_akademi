from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    # Yeni ve doğru yazım şekli:
    return templates.TemplateResponse(request=request, name="index.html")

@app.get("/hakkimizda", response_class=HTMLResponse)
async def read_hakkimizda(request: Request):
    return templates.TemplateResponse(request=request, name="about.html")

@app.get("/programlar", response_class=HTMLResponse)
async def read_programlar(request: Request):
    return templates.TemplateResponse(request=request, name="programs.html")

@app.get("/iletisim", response_class=HTMLResponse)
async def read_iletisim(request: Request):
    return templates.TemplateResponse(request=request, name="contact.html")

@app.post("/iletisim", response_class=HTMLResponse)
async def submit_contact(
    request: Request,
    ad_soyad: str = Form(...),
    telefon: str = Form(...),
    program: str = Form(...),
    mesaj: str = Form("")
):
    print(f"Başvuru: {ad_soyad}") # Terminalde kontrol için
    return templates.TemplateResponse(request=request, name="contact.html", context={"success": True})