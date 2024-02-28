from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_message(
        chat_id=msg.chat.id,
        text=f"""✇︙ مرحـباً بـك عزيـزي  {msg.from_user.mention} فـي بـوت اسـتـخـراج الـجـلـسـات لسـورس X
✇︙ يمكنك استخراج الجلسات الـتالية
✇︙ بايروجرام v1 للميوزك والتليثون الإصدار القديم
✇︙ بايروجرام v2 للميوزك والتليثون الاصدار الجديد
✇︙ تريمكس (تليثون)  للحسابات & للبوتات

✇︙ بواسطـة : [𝙼𝚛. 𝚇](t.me/iivlf) """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="‹ بـدء إسـتـخـراج جـلـسـة ›", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("𝚀𝚄𝚁𝙰𝙽‌ 𝙲𝙷", url="https://t.me/M_w7d"),
                    InlineKeyboardButton("𝙼𝚈 𝚆𝙾𝚁𝙻𝙳", url="https://t.me/oooj30")
                ],
                [
                    InlineKeyboardButton("ᯓ 𝙳𝙴𝚅 𝙼𝚛. 𝚇 ❥", user_id=6367974448)
                ]
            ]
        ),
        disable_web_page_preview=True,
    )
