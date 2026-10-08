from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from Driver import run

app = FastAPI()

# Setup Jinja2 templates
templates = Jinja2Templates(directory="templates")


# Route to serve the form
@app.get("/", response_class=HTMLResponse)
async def get_form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})


# Route to handle the form submission and call the custom function
@app.post("/submit/")
async def submit_text(request: Request, input_text: str = Form(...)):
    result = run(input_text)
    return templates.TemplateResponse(
        "result.html", {"request": request, "input_text": input_text, "result": result}
    )
