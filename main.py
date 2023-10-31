import gc

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.services.login_service import login_router

gc.collect()

tags_meta = [{"name": "Convey Application", "description": "API's to Get convey data"}]
app = FastAPI(
    title="Convey",
    version="v1.0",
    description="convey application",
    openapi_tags=tags_meta,
    root_path=""
)


app.include_router(login_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "DELETE", "PUT"],
    allow_headers=["*"],
)
