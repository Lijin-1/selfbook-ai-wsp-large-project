from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def home():
    return {"project": "SelfBook AI", "status": "LIVE", "student": "Lijin.T", "wsp": "Large Project DONE"}

@app.get("/health")
def health():
    return {"ok": True}

@app.get("/docs-test")
def test():
    return {"message": "FastAPI is running on port 8000"}
