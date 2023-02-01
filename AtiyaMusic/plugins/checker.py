from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS

from AtiyaMusic import app
from AtiyaMusic.utils import bot_sys_stats
from AtiyaMusic.utils.database.memorydatabase import get_active_chats



@app.on_message(
    filters.command("respondtostatuschecker") & filters.private & ~BANNED_USERS
)
async def respond(_, message: Message):
    get = await bot_sys_stats()
    active_vc = len(await get_active_chats())
    await message.reply_text(f"{get[0]}~{get[1]}~{active_vc}")
