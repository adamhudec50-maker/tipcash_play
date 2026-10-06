from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <!DOCTYPE html>
    <html lang="cs">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Tipcash Play</title>
        <style>
            * { box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
            body { background-color: #0f172a; color: #f8fafc; display: flex; justify-content: center; min-height: 100vh; padding: 20px; }
            .card { background: #1e293b; border-radius: 20px; padding: 24px; width: 100%; max-width: 400px; box-shadow: 0 10px 25px rgba(0,0,0,0.5); text-align: center; display: flex; flex-direction: column; justify-content: space-between; height: auto; }
            .badge { background: #10b981; color: #022c22; font-weight: bold; padding: 6px 12px; border-radius: 20px; font-size: 0.8rem; text-transform: uppercase; display: inline-block; margin-bottom: 12px; }
            h1 { font-size: 1.8rem; margin-bottom: 8px; color: #ffffff; }
            p { color: #94a3b8; font-size: 0.95rem; margin-bottom: 24px; }
            .btn { background: #3b82f6; color: white; border: none; padding: 14px 20px; border-radius: 12px; font-size: 1rem; font-weight: 600; cursor: pointer; transition: background 0.2s; width: 100%; text-decoration: none; display: block; }
            .btn:active { background: #1d4ed8; transform: scale(0.98); }
            .footer { margin-top: 20px; font-size: 0.8rem; color: #64748b; }
        </style>
    </head>
    <body>
        <div class="card">
            <div>
                <span class="badge">Aktivní</span>
                <h1>Tipcash Play</h1>
                <p>Vítejte v aplikaci! Mobilní rozhraní je úspěšně připraveno pro vaše tipování.</p>
            </div>
            <div>
                <button class="btn" onclick="alert('Aplikace reaguje!')">Vstoupit do hry</button>
                <div class="footer">Verze 1.0 • Běží na FastAPI</div>
            </div>
        </div>
    </body>
    </html>
    """
