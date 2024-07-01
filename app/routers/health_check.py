from fastapi import APIRouter

router = APIRouter(
    tags=["Health End Point"]
)


# health endpoint
@router.get('/')
async def health_endpoint():
    return {
        "message": "Application started successfully.",
        "success": True
    }
