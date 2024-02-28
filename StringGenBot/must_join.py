from config import MUST_JOIN

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden


@Client.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(bot: Client, msg: Message):
    if not MUST_JOIN:
        return
    try:
        try:
            await bot.get_chat_member(MUST_JOIN, msg.from_user.id)
        except UserNotParticipant:
            if MUST_JOIN.isalpha():
                link = "https://t.me/" + MUST_JOIN
            else:
                chat_info = await bot.get_chat(MUST_JOIN)
                link = chat_info.invite_link
            try:
                await msg.reply_photo(
                    photo="https://graph.org/file/185cc8cd00e7b0a0cdc77.jpg", caption=f"✇︙ عـليـك الإنضمـام إلـى [جروب الدعم]({link}) أولاً \n✇︙ ثـم حـاول مـرة اخـرى !",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("𝙷𝙴𝙻𝙿 𝙶𝚁𝙾𝚄𝙿", url=link),
                            ]
                        ]
                    )
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"Promote me as an admin in the MUST_JOIN chat : {MUST_JOIN} !")
