from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi
from .api.v1 import auth, sessions, chat
from .database import engine
from .models.base import Base

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Чат-Бот Поддержки",
        version="0.1.0",
        routes=app.routes,
    )
    openapi_schema.get("components", {}).pop("securitySchemes", None)
    openapi_schema.pop("security", None)
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app = FastAPI(
    title="Чат-Бот Поддержки",
    version="0.1.0",
    swagger_ui_init_oauth=None,
    swagger_ui_oauth2_redirect_url=None,
)

app.openapi = custom_openapi

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(sessions.router)
app.include_router(chat.router)

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        
        
@app.get("/")
def root():
    return {"message": "Chat Bot API is running!"}