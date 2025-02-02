from pyrogram import Client, filters
from Rudra import app

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


app.on_message(filters.command("owner") & filters.group)


async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/6eefe0911a08595221a10.jpg",
        caption=f"""🥀 𝐂𝐥𝐢𝐜𝐤 𝐇𝐞𝐫𝐞 𝐅𝐨𝐫 𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐎𝐰𝐧𝐞𝐫 🥀""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🗡️ 𝐎ᴡɴᴇʀ 🗡️", url=f"https://t.me/Nijuko_bot"
                    )],
            ]
        ),
    )


@app.on_message(filters.command("owner") & filters.group)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/6eefe0911a08595221a10.jpg",
        caption=f"""🥀 𝐂𝐥𝐢𝐜𝐤 𝐇𝐞𝐫𝐞 𝐅𝐨𝐫 𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐎𝐰𝐧𝐞𝐫 🥀""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🗡️ 𝐎ᴡɴᴇʀ 🗡️", url=f"https://t.me/Nijuko_bot"
                    )],
            ]
        ),
    )


@app.on_message(filters.command("owner") & filters.private)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/6eefe0911a08595221a10.jpg",
        caption=f"""🥀 𝐂𝐥𝐢𝐜𝐤 𝐇𝐞𝐫𝐞 𝐅𝐨𝐫 𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐎𝐰𝐧𝐞𝐫 🥀""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🗡️ 𝐎ᴡɴᴇʀ 🗡️", url=f"https://t.me/Nijuko_bot"
                    )],
            ]
        ),
    )
