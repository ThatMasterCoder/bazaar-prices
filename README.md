# Bazaar Prices

A website showing price history of commonly used items.  
Frontend in TypeScript, backend with Flask.

---

## Setup

1. Create and activate a virtual environment:
```
python -m venv venv
# Windows
.\venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

2. Install dependencies:
```
pip install -r backend/requirements.txt
```
3. Compile TypeScript:
```
tsc --watch
```

## Running
```
flask --app backend/app.py run
```

Then open http://127.0.0.1:5000 in your browser.