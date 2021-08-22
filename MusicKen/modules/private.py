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
                    text="Music downloader", url=f"https://t.me/lagukamubot"
                ),
                InlineKeyboardButton(
                    text="Owner of bot", url="https://t.me/eleaxzeno"
                ),
            ],
        ]
    return button


@Client.on_message(filters.command("reload") & filters.group & ~filters.edited)
@authorized_users_only
async def admincache(client, message: Message):
    await message.reply_text("""🔊 BOT MUSIK SIAP DIGUNAKAN""",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton(text="Bot commands", url=f"https://telegra.ph/%E1%B4%A2%E1%B4%87%C9%B4%E1%B4%8F-08-21")],
            ]
        ),
    )


@Client.on_message(filters.command("help") & ~filters.private & ~filters.channel)
async def ghelp(_, message: Message):
    await message.reply_text(
        """
𝑪𝒐𝒎𝒎𝒂𝒏𝒅𝒔 𝒊𝒏 𝒁𝑬𝑵𝑶 𝑴𝑺𝑪

𝚏𝚘𝚛 𝚊𝚕𝚕 𝚞𝚜𝚎𝚛𝚜 :
 • /play (song name) : play song from youtube
 • /playlist : show the list song in queue
 • /search (video name) : search video from youtube
 • /lyric (song name) : find the lyrics of the song

𝚏𝚘𝚛 𝚊𝚍𝚖𝚒𝚗𝚜 :
 • /musicplayer (on / off) - disable / enable music player
 • /userbotjoin - invite assistant bot
 • /reload - for refresh the admin list
 • /player - open music player settings panel
 • /skip - skip to the next song
 • /pause - pause the music streaming
 • /resume - resume the music was paused
 • /skip - skip to the next song
 • /end - stop music streaming
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton(text="Music downloader", url=f"t.me/lagukamubot")],
            ]
        ),
    )
