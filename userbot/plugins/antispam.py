from telethon.events import ChatAction

from userbot import *
from . import *

"""Bans Spammers/Scammer At time Of Arrival 
If You Add Him The Bot Won't Restrict."""


@borg.on(ChatAction)
async def ok(event):
    juser = await event.get_user()
    if config.legendconfig.ANTISPAM_FEATURE != "ENABLE":
        return
    if event.user_joined:
        hmmyep = await borg.get_permissions(event.chat_id, bot.uid)
        if not hmmyep.is_admin:
            return
        user = sclient.is_banned(juser.id)
        if user:
            await event.reply(
                f"**Legend-Antispam** \n**Detected Malicious User.** \n**User-ID :** `{juser.id}`  \n**Reason :** `{user.reason}`"
            )
            try:
                await borg.edit_permissions(
                    event.chat_id, juser.id, view_messages=False
                )
            except:
                pass
        else:
            pass