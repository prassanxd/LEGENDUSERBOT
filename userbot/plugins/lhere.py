import asyncio
import random
from userbot.cmdhelp import CmdHelp
from . import *

from userbot.utils import admin_cmd, sudo_cmd
NUMBER = ["0", "1"]

MEDHU = [
    "I AM LEGEND {ALIVE_NAME}",
    "PLS DONT DISTURB HIM LEGEND IS BUSY NOW WHEN HE COME BACK HE REPLY U",
    "DON'T BREAK THE HEART OF THE HACKER BCOZ U DON'T KNOW WHAT WILL HAPPN TN",
    "IF U NEED ANY HELP U CAN TYPE WHEN HE COME BACK HE WILL REPLY U",
]

que = {}


@bot.on(admin_cmd(incoming=True))
@bot.on(sudo_cmd(incoming=True, allow_sudo=True))
async def _(event):
    global que
    queue = que.get(event.sender_id)
    if not queue:
        return
    async with event.client.action(event.chat_id, "typing"):
        await asyncio.sleep(0.3)
    async with event.client.action(event.chat_id, "typing"):
        await event.client.send_message(
            entity=event.chat_id,
            message="""{}""".format(random.choice(MEDHU)),
            reply_to=event.message.id,
        )

@bot.on(admin_cmd(pattern="lstart (?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="lstart (?: |$)(.*)", allow_sudo=True))
async def _(event):
    global que
    if event.fwd_from:
        return
    if event.reply_to_msg_id:
        a = await event.get_reply_message()
        b = await event.client.get_entity(a.sender_id)
        e = b.id
        c = b.first_name
        username = f"[{c}](tg://user?id={e})"
        event = await edit_or_reply(event, "LEGEND")
        que[e] = []
        qeue = que.get(e)
        appendable = [e]
        qeue.append(appendable)
        await event.edit(f"LEGEND{ALIVE_NAME}")
    else:
        user = event.pattern_match.group(1)
        event = await edit_or_reply(event, "LEGEND START RAID")
        a = await event.client.get_entity(user)
        e = a.id
        c = a.first_name
        username = f"[{c}](tg://user?id={e})"
        que[e] = []
        qeue = que.get(e)
        appendable = [e]
        qeue.append(appendable)
        await event.edit(f"LEGEND {ALIVE_NAME}")


@bot.on(admin_cmd(pattern="lstop (?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="lstop (?: |$)(.*)", allow_sudo=True))
async def _(event):
    global que
    if event.fwd_from:
        return
    if event.reply_to_msg_id:
        a = await event.get_reply_message()
        b = await event.client.get_entity(a.sender_id)
        e = b.id
        c = b.first_name
        username = f"[{c}](tg://user?id={e})"
        event = await edit_or_reply(event, "I KNOW U ARE WAITING FOR ME I AM BACK....")
        queue = que.get(e)
        queue.pop(0)
        await event.edit(f"LEGEND")
    else:
        user = event.pattern_match.group(1)
        event = await edit_or_reply(event, "Reply Raid De-activating....")
        a = await event.client.get_entity(user)
        e = a.id
        c = a.first_name
        username = f"[{c}](tg://user?id={e})"
        queue = que.get(e)
        queue.pop(0)
        await event.edit(f"LEGEND STOPED RAID {ALIVE_NAME}")
CmdHelp("lhere").add_command(
     'lstart', None, 'Reply to him or her to start legend personal file'
).add_command(
     'lstop', None, 'Reply To her Ya him To stop legend personal file'
).add()