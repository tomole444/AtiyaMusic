from config import LOG, LOGGER_ID, BOT_NAME
from AtiyaMusic import app
from AtiyaMusic.utils.database import is_on_off


async def play_logs(message, streamtype):
    if await is_on_off(LOG):
        if message.chat.username:
            chatusername = f"@{message.chat.username}"
        else:
            chatusername = "ᴩʀɪᴠᴀᴛᴇ ᴄʜᴀᴛ"
        logger_text = f"""
**{BOT_NAME} ᴩʟᴀʏ ʟᴏɢɢᴇʀ**

**━━━━━━━━━━━━━━━**
**😇 Cʜᴀᴛ Nᴀᴍᴇ : >** {message.chat.title} [`{message.chat.id}`]
**━━━━━━━━━━━━━━━**
**😘 Nᴀᴍᴇ : ›** {message.from_user.mention}
**━━━━━━━━━━━━━━━**
**😛 Usᴇʀɴᴀᴍᴇ : ›** @{message.from_user.username}
**━━━━━━━━━━━━━━━**
**😁 Iᴅ : ›** `{message.from_user.id}`
**━━━━━━━━━━━━━━━**
**🥴 Cʜᴀᴛ Lɪɴᴋ : >** {chatusername}
**━━━━━━━━━━━━━━━**
**🤫 Sᴇᴀʀᴄʜᴇᴅ Fᴏʀ :** {message.text}
**━━━━━━━━━━━━━━━**
**🥴 Sᴛʀᴇᴀᴍ Tʏᴘᴇ :** {streamtype}
**━━━━━━━━━━━━━━━**"""
        if message.chat.id != LOGGER_ID:
            try:
                await app.send_message(
                    LOGGER_ID,
                    text=logger_text,
                    disable_web_page_preview=True,
                )
            except:
                pass
        return
