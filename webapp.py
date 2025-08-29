from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def root():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Учет расходников</title>
        <meta charset="utf-8">
        <style>
            body { font-family: Arial, sans-serif; padding: 20px; background: #f4f4f4; }
            .card { background: white; padding: 20px; border-radius: 10px; box-shadow: 0 2px 6px rgba(0,0,0,0.1); }
            h1 { color: #333; }
            ul { padding-left: 20px; }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>📦 Остатки на складе</h1>
            <ul>
                <li>Хюбы: 10</li>
                <li>Боксы: 5</li>
                <li>Пигтейлы: 20</li>
            </ul>
        </div>
    </body>
    </html>
    """
