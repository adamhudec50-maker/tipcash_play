from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
@app.head("/")
def read_root():
    return """<!DOCTYPE html>
<html>
<head>
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

HTML_CONTENT = """<!DOCTYPE html>
<html lang="cs">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Tipcash Play</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    <style>
        body { background-color: #0f172a; color: #f8fafc; font-family: system-ui, -apple-system, sans-serif; }
        .glass { background: rgba(30, 41, 59, 0.7); backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.08); }
    </style>
</head>
<body class="pb-20">
    <!-- Header -->
    <header class="glass sticky top-0 z-50 px-4 py-3 flex justify-between items-center border-b border-slate-800">
        <div class="flex items-center space-x-2">
            <i class="fa-solid fa-trophy text-amber-400 text-xl"></i>
            <span class="font-bold text-lg bg-gradient-to-r from-amber-400 to-orange-500 bg-clip-text text-transparent">Tipcash Play</span>
        </div>
        <div class="bg-slate-800 px-3 py-1 rounded-full border border-slate-700 text-xs font-semibold text-emerald-400">
            🟢 LIVE
        </div>
    </header>

    <!-- Main Content -->
    <main class="max-w-md mx-auto p-4 space-x-0 space-y-4">
        <!-- Banner / Welcome -->
        <div class="glass p-5 rounded-2xl bg-gradient-to-br from-indigo-900/40 to-slate-900/80 border border-indigo-500/20">
            <h2 class="text-xl font-bold mb-1 text-white">Vítej v Tipcash Play ⚽</h2>
            <p class="text-xs text-slate-400">Tipuj zápasy, sbírej body a porážej kámoše v žebříčku!</p>
        </div>

        <!-- Matches Section -->
        <div>
            <h3 class="text-sm font-semibold text-slate-400 uppercase tracking-wider mb-3 px-1">Dnešní Zápasy</h3>
            
            <!-- Match Card 1 -->
            <div class="glass p-4 rounded-xl mb-3 space-y-3">
                <div class="flex justify-between text-xs text-slate-400">
                    <span>Liga Mistrů • 21:00</span>
                    <span class="text-amber-400 font-medium">Otevřeno pro tipy</span>
                </div>
                <div class="flex justify-between items-center py-2">
                    <div class="flex items-center space-x-3 w-5/12">
                        <span class="font-semibold text-sm">Real Madrid</span>
                    </div>
                    <span class="text-xs font-bold text-slate-500">VS</span>
                    <div class="flex items-center space-x-3 w-5/12 justify-end">
                        <span class="font-semibold text-sm text-right">Man. City</span>
                    </div>
                </div>
                <div class="flex space-x-2 pt-1">
                    <input type="number" id="m1_h" placeholder="0" class="w-1/2 bg-slate-900 border border-slate-700 rounded-lg py-2 text-center text-white text-sm focus:outline-none focus:border-amber-400">
                    <input type="number" id="m1_a" placeholder="0" class="w-1/2 bg-slate-900 border border-slate-700 rounded-lg py-2 text-center text-white text-sm focus:outline-none focus:border-amber-400">
                </div>
                <button onclick="saveTip('Real vs City', 'm1_h', 'm1_a')" class="w-full bg-indigo-600 hover:bg-indigo-500 text-white font-medium py-2 rounded-lg text-xs transition duration-200">
                    Uložit tip
                </button>
            </div>

            <!-- Match Card 2 -->
            <div class="glass p-4 rounded-xl mb-3 space-y-3">
                <div class="flex justify-between text-xs text-slate-400">
                    <span>Premier League • 18:30</span>
                    <span class="text-amber-400 font-medium">Otevřeno pro tipy</span>
                </div>
                <div class="flex justify-between items-center py-2">
                    <div class="flex items-center space-x-3 w-5/12">
                        <span class="font-semibold text-sm">Arsenal</span>
                    </div>
                    <span class="text-xs font-bold text-slate-500">VS</span>
                    <div class="flex items-center space-x-3 w-5/12 justify-end">
                        <span class="font-semibold text-sm text-right">Chelsea</span>
                    </div>
                </div>
                <div class="flex space-x-2 pt-1">
                    <input type="number" id="m2_h" placeholder="0" class="w-1/2 bg-slate-900 border border-slate-700 rounded-lg py-2 text-center text-white text-sm focus:outline-none focus:border-amber-400">
                    <input type="number" id="m2_a" placeholder="0" class="w-1/2 bg-slate-900 border border-slate-700 rounded-lg py-2 text-center text-white text-sm focus:outline-none focus:border-amber-400">
                </div>
                <button onclick="saveTip('Arsenal vs Chelsea', 'm2_h', 'm2_a')" class="w-full bg-indigo-600 hover:bg-indigo-500 text-white font-medium py-2 rounded-lg text-xs transition duration-200">
                    Uložit tip
                </button>
            </div>
        </div>

        <!-- Leaderboard -->
        <div>
            <h3 class="text-sm font-semibold text-slate-400 uppercase tracking-wider mb-3 px-1">Tabulka Hráčů</h3>
            <div class="glass rounded-xl overflow-hidden">
                <div class="flex justify-between p-3 border-b border-slate-800 text-xs font-semibold text-slate-400">
                    <span>Hráč</span>
                    <span>Body</span>
                </div>
                <div class="divide-y divide-slate-800/50 text-sm">
                    <div class="flex justify-between p-3 items-center">
                        <span class="font-medium">1. Adam 👑</span>
                        <span class="font-bold text-amber-400">15 b</span>
                    </div>
                    <div class="flex justify-between p-3 items-center">
                        <span class="font-medium text-slate-300">2. Petr</span>
                        <span class="font-bold text-slate-300">12 b</span>
                    </div>
                    <div class="flex justify-between p-3 items-center">
                        <span class="font-medium text-slate-400">3. Michal</span>
                        <span class="font-bold text-slate-400">8 b</span>
                    </div>
                </div>
            </div>
        </div>
    </main>

    <!-- Notification toast -->
    <div id="toast" class="fixed bottom-5 left-1/2 -translate-x-1/2 bg-emerald-500 text-white px-4 py-2 rounded-full text-xs font-semibold shadow-lg hidden">
        Tip byl úspěšně uložen! 🚀
    </div>

    <script>
        function saveTip(match, hId, aId) {
            const h = document.getElementById(hId).value;
            const a = document.getElementById(aId).value;
            if (h === '' || a === '') {
                alert('Vyplňte prosím obě skóre!');
                return;
            }
            const toast = document.getElementById('toast');
            toast.innerText = match + ' (' + h + ':' + a + ') uložen! 🚀';
            toast.classList.remove('hidden');
            setTimeout(() => toast.classList.add('hidden'), 3000);
        }
    </script>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
@app.head("/")
def read_root():
    return HTML_CONTENT
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
