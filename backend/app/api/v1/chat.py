from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession
from ...database import get_db
from ...models.session import Session
from ...models.message import Message
from ...schemas.message import MessageCreate
from ...deps import get_current_user_id
from ...bot import generate_bot_response
from sqlalchemy import select

router = APIRouter()

@router.post("/chat/message")
async def send_message(
    message: MessageCreate,
    session_id: int = Query(...),
    db: AsyncSession = Depends(get_db),
    user_id: int = Depends(get_current_user_id)
):
    result = await db.execute(select(Session).where(Session.id == session_id, Session.user_id == user_id))
    if not result.scalar_one_or_none():
        raise HTTPException(status_code=404, detail="Session not found")
    if not message.text.strip():
        raise HTTPException(status_code=400, detail="Message text cannot be empty")
    
    user_msg = Message(session_id=session_id, sender="user", text=message.text.strip())
    db.add(user_msg)
    await db.commit()
    
    bot_text = generate_bot_response(message.text)
    bot_msg = Message(session_id=session_id, sender="bot", text=bot_text)
    db.add(bot_msg)
    await db.commit()
    
    return {"user_message": message.text, "bot_response": bot_text}