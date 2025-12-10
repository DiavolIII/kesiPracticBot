from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from ...database import get_db
from ...models.session import Session
from ...schemas.session import SessionResponse
from ...deps import get_current_user_id

router = APIRouter()

@router.post("/chat/session", response_model=SessionResponse)
async def create_session(
    db: AsyncSession = Depends(get_db),
    user_id: int = Depends(get_current_user_id)
):
    new_session = Session(user_id=user_id)
    db.add(new_session)
    await db.commit()
    await db.refresh(new_session)
    return new_session