from fastapi import APIRouter

from app.pkg.db.database import get_db

router = APIRouter(
    prefix='/api/v1'
)

@router.get(path="/hello")
def user_hello():

    return {
        "hello": "world"
    }
