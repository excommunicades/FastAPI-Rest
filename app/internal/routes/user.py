from fastapi import APIRouter

router = APIRouter(
    prefix='/api/v1'
)

@router.get(path="/hello")
def user_hello():

    return {
        "hello": "world"
    }