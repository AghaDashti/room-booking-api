from fastapi import FastAPI

from app.routers import rooms

app = FastAPI(title="Room Booking API")
app.include_router(rooms.router)


@app.get("/health")
def health():
    return {"status": "ok"}