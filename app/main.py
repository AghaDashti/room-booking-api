from fastapi import FastAPI

app = FastAPI(title="Room Booking API")


@app.get("/health")
def health():
    return {"status": "ok"}