import logging

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from MusicKen.config import (
    BOT_USERNAME,
    KENKAN,
    OWNER,
    PROJECT_NAME,
    SOURCE_CODE,
    SUPPORT_GROUP,
    UPDATES_CHANNEL,
)
from MusicKen.helpers.decorators import authorized_users_only
from MusicKen.modules.msg import Messages as tr

logging.basicConfig(level=logging.INFO)


@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""Hallo {message.from_user.first_name}, bot ini dapat digunakan untuk:
 × Memutar lagu di group
 × Mendownload lagu
 × Mendownload video
 × Mencari link youtube
 × Mencari lirik lagu
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Commands", callback_data=f"help+1"),
                ],
            ]
        ),
        reply_to_message_id=message.message_id,
    )


@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
    await message.reply_photo(
        photo=f"{KENKAN}",
        caption=f"""{PROJECT_NAME} siap digunakan!""",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton(text="Music Downloader", url=f"t.me/lagukamubot")],
            ]
        ),
    )


@Client.on_message(filters.private & filters.incoming & filters.command(["help"]))
def _help(client, message):
    client.send_message(
        chat_id=message.chat.id,
        text=tr.HELP_MSG[1],
        parse_mode="markdown",
        disable_web_page_preview=True,
        disable_notification=True,
        reply_markup=InlineKeyboardMarkup(map(1)),
        reply_to_message_id=message.message_id,
    )


help_callback_filter = filters.create(
    lambda _, __, query: query.data.startswith("help+")
)


@Client.on_callback_query(help_callback_filter)
def help_answer(client, callback_query):
    chat_id = callback_query.from_user.id
    message_id = callback_query.message.message_id
    msg = int(callback_query.data.split("+")[1])
    client.edit_message_text(
        chat_id=chat_id,
        message_id=message_id,
        text=tr.HELP_MSG[msg],
        reply_markup=InlineKeyboardMarkup(map(msg)),
    )


def map(pos):
    if pos == 1:
        button = [
            [
                InlineKeyboardButton(
                    text="Music downloader", url=f"https://t.me/lagukamubot"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="Owner of bot", url="https://t.me/eleaxzeno"
                ),
            ],
        ]
    elif pos == len(tr.HELP_MSG) - 1:
        url = f"https://t.me/{SUPPORT_GROUP}"
        button = [
            [
                InlineKeyboardButton(
                    text="Music downloader", url=f"https://t.me/lagukamubot"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="Owner of bot", url="https://t.me/eleaxzeno"
                ),
            ],
        ]
    else:
        button = [
            [
                InlineKeyboardButton(
                    text="⬅️ sᴇʙᴇʟᴜᴍɴʏᴀ", callback_data=f"help+{pos-1}"
                ),
                InlineKeyboardButton(
                    text="sᴇʟᴀɴᴊᴜᴛɴʏᴀ ➡️", callback_data=f"help+{pos+1}"
                ),
            ],
        ]
    return button


@Client.on_message(filters.command("reload") & filters.group & ~filters.edited)
@authorized_users_only
async def admincache(client, message: Message):
    await message.reply_photo(
        photo=f"{KENKAN}",
        caption="✅ **Bot berhasil dimulai ulang!**\n\n **Daftar admin telah diperbarui**",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton(text="🔵 ᴏᴡɴᴇʀ", url=f"t.me/{OWNER}")],
                [
                    InlineKeyboardButton(
                        text="👥 ɢʀᴏᴜᴘ", url=f"https://t.me/{SUPPORT_GROUP}"
                    ),
                    InlineKeyboardButton(
                        text="ᴄʜᴀɴɴᴇʟ 📣", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton("🌟 ɢɪᴛ ʜᴜʙ 🌟", url=f"{SOURCE_CODE}"),
                    InlineKeyboardButton(
                        "💵 ꜱᴀᴡᴇʀɴʏᴀ", url="https://trakteer.id/kenkansaja/tip"
                    ),
                ],
            ]
        ),
    )


@Client.on_message(filters.command("help") & ~filters.private & ~filters.channel)
async def ghelp(_, message: Message):
    await message.reply_text(
        """
**🔰 Perintah**
      
**=>> Memutar Lagu 🎧**
      
• /play (nama lagu) - Untuk Memutar lagu yang Anda minta melalui youtube
• /ytplay (nama lagu) - Untuk Memutar lagu yang Anda minta melalui youtube
• /yt (nama lagu) - Untuk Memutar lagu yang Anda minta melalui youtube
• /p (nama lagu) - Untuk Memutar lagu yang Anda minta melalui youtube
• /lplay - Untuk Memutar lagu yang Anda reply dari gc
• /player: Buka menu Pengaturan pemain
• /skip: Melewati trek saat ini
• /pause: Jeda trek
• /resume: Melanjutkan trek yang dijeda
• /end: ​​Menghentikan pemutaran media
• /current: Menampilkan trek yang sedang diputar
• /playlist: Menampilkan daftar putar
      
Semua Perintah Bisa Digunakan Kecuali Perintah /player /skip /pause /resume  /end Hanya Untuk Admin Grup
      
**==>>Download Lagu 📥**
      
• /song [nama lagu]: Unduh audio lagu dari youtube

**=>> Saluran Music Play 🛠**
      
⚪️ Hanya untuk admin grup tertaut:
      
• /cplay (nama lagu) - putar lagu yang Anda minta
• /cplaylist - Tampilkan daftar yang sedang diputar
• /cccurrent - Tampilkan sedang diputar
• /cplayer - buka panel pengaturan pemutar musik
• /cpause - jeda pemutaran lagu
• /cresume - melanjutkan pemutaran lagu
• /cskip - putar lagu berikutnya
• /cend - hentikan pemutaran musik
• /userbotjoinchannel - undang asisten ke obrolan Anda""",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton(text="🔵 ᴏᴡɴᴇʀ", url=f"t.me/{OWNER}")],
                [
                    InlineKeyboardButton(
                        text="👥 ɢʀᴏᴜᴘ", url=f"https://t.me/{SUPPORT_GROUP}"
                    ),
                    InlineKeyboardButton(
                        text="ᴄʜᴀɴɴᴇʟ 📣", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton("🌟 ɢɪᴛ ʜᴜʙ 🌟", url=f"{SOURCE_CODE}"),
                    InlineKeyboardButton(
                        "💵 ꜱᴀᴡᴇʀɴʏᴀ", url="https://trakteer.id/kenkansaja/tip"
                    ),
                ],
            ]
        ),
    )
