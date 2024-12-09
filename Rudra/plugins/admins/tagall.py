import asyncio
from Rudra import app
from pyrogram import filters
from pyrogram.types import ChatMember

SPAM_CHATS = []

async def is_admin(chat_id, user_id):
    # Check if user is an admin or owner in the chat
    chat_member = await app.get_chat_member(chat_id, user_id)
    return chat_member.status in [ChatMember.OWNER, ChatMember.ADMINISTRATOR]

@app.on_message(filters.command(["tagall", "all"]) | filters.command("@all", "") & filters.group)
async def tag_all_users(_, message): 
    user_id = message.from_user.id
    chat_id = message.chat.id

    # Check if the user is an admin
    if not await is_admin(chat_id, user_id):
        return await message.reply_text("**ʏᴏᴜ ᴍᴜsᴛ ʙᴇ ᴀɴ ᴀᴅᴍɪɴ ᴛᴏ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ!**")

    replied = message.reply_to_message  
    if len(message.command) < 2 and not replied:
        await message.reply_text("**ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴏʀ ɢɪᴠᴇ sᴏᴍᴇ ᴛᴇxᴛ ᴛᴏ ᴛᴀɢ ᴀʟʟ**") 
        return                  
    if replied:
        SPAM_CHATS.append(chat_id)      
        usernum = 0
        usertxt = ""
        async for m in app.get_chat_members(chat_id): 
            if chat_id not in SPAM_CHATS:
                break       
            usernum += 5
            usertxt += f"\n⊚ [{m.user.first_name}](tg://user?id={m.user.id})\n"
            if usernum == 1:
                await replied.reply_text(usertxt)
                await asyncio.sleep(2)
                usernum = 0
                usertxt = ""
        try:
            SPAM_CHATS.remove(chat_id)
        except Exception:
            pass
    else:
        text = message.text.split(None, 1)[1]
        
        SPAM_CHATS.append(chat_id)
        usernum = 0
        usertxt = ""
        async for m in app.get_chat_members(chat_id):       
            if chat_id not in SPAM_CHATS:
                break 
            usernum += 1
            usertxt += f"\n⊚ [{m.user.first_name}](tg://user?id={m.user.id})\n"
            if usernum == 5:
                await app.send_message(chat_id, f'{text}\n{usertxt}')
                await asyncio.sleep(2)
                usernum = 0
                usertxt = ""                          
        try:
            SPAM_CHATS.remove(chat_id)
        except Exception:
            pass        
           
@app.on_message(filters.command("tagoff") & filters.group)
async def cancelcmd(_, message):
    user_id = message.from_user.id
    chat_id = message.chat.id

    # Check if the user is an admin
    if not await is_admin(chat_id, user_id):
        return await message.reply_text("**ʏᴏᴜ ᴍᴜsᴛ ʙᴇ ᴀɴ ᴀᴅᴍɪɴ ᴛᴏ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ!**")

    if chat_id in SPAM_CHATS:
        try:
            SPAM_CHATS.remove(chat_id)
        except Exception:
            pass   
        return await message.reply_text("**ᴛᴀɢ ᴀʟʟ sᴜᴄᴄᴇssғᴜʟʟʏ sᴛᴏᴘᴘᴇᴅ!**")     
    else:
        await message.reply_text("**ɴᴏ ᴘʀᴏᴄᴇss ᴏɴɢᴏɪɴɢ!**")  
        return
