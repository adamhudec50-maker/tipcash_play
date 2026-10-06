from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
@app.head("/")
def read_root():
    return """<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Tipcash Play</title>
    <style>
        body { background: #0f172a; color: #fff; font-family: sans-serif; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; }
        .card { background: #1e293b; padding: 30px; border-radius: 16px; text-align: center; box-shadow: 0 10px 25px rgba(0,0,0,0.5); max-width: 320px; width: 90%; }
        h1 { font-size: 24px; margin-bottom: 10px; }
        .btn { background: #3b82f6; color: #fff; border: none; padding: 12px 20px; border-radius: 8px; font-size: 16px; margin-top: 15px; width: 100%; cursor: pointer; }
    </style>
</head>
<body>
    <div class="card">
        <h1>Tipcash Play</h1>
        <p>Mobilní rozhraní je připraveno.</p>
        <button class="btn" onclick="alert('Funguje!')">Vstoupit do hry</button>
    </div>
</body>
</html>"""
