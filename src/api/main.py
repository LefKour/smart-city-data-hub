from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Route Import

from routes import properties

app = FastAPI(
    title="Smart City Data Hub",
    description="Smart City Data Hub",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Link Routes
app.include_router(
    properties.router,
    prefix="/properties",
    tags=["Properties"]
)

@app.get("/", tags=["Root"])
async def root():
    return {
        "message": "Welcome to Urban Data Hub API",
        "status": "operational",
        "version": "1.0.0",
        "docs": "/docs"
    }

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8001,
        reload=True
    )