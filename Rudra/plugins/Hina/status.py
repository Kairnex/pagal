from pyrogram import Client, filters
from Rudra import app


# Command handler to get group status
@app.on_message(filters.command("status") & filters.group)
def group_status(client, message):
    chat = message.chat  # Chat where the command was sent
    status_text = f"Group ID: {chat.id}\n" \
                  f"Title: {chat.title}\n" \
                  f"Type: {chat.type}\n"
                  
    if chat.username:  # Not all groups have a username
        status_text += f"Username: @{chat.username}"
    else:
        status_text += "Username: None"

    message.reply_text(status_text)


#########

""" ***                                                                       

                                                                                                                                                                                                                         
                                                                                                                                                                                                                         
RRRRRRRRRRRRRRRRR   UUUUUUUU     UUUUUUUUDDDDDDDDDDDDD      RRRRRRRRRRRRRRRRR                  AAA                              JJJJJJJJJJJ          AAA                              AAA         TTTTTTTTTTTTTTTTTTTTTTT
R::::::::::::::::R  U::::::U     U::::::UD::::::::::::DDD   R::::::::::::::::R                A:::A                             J:::::::::J         A:::A                            A:::A        T:::::::::::::::::::::T
R::::::RRRRRR:::::R U::::::U     U::::::UD:::::::::::::::DD R::::::RRRRRR:::::R              A:::::A                            J:::::::::J        A:::::A                          A:::::A       T:::::::::::::::::::::T
RR:::::R     R:::::RUU:::::U     U:::::UUDDD:::::DDDDD:::::DRR:::::R     R:::::R            A:::::::A                           JJ:::::::JJ       A:::::::A                        A:::::::A      T:::::TT:::::::TT:::::T
  R::::R     R:::::R U:::::U     U:::::U   D:::::D    D:::::D R::::R     R:::::R           A:::::::::A                            J:::::J        A:::::::::A                      A:::::::::A     TTTTTT  T:::::T  TTTTTT
  R::::R     R:::::R U:::::D     D:::::U   D:::::D     D:::::DR::::R     R:::::R          A:::::A:::::A                           J:::::J       A:::::A:::::A                    A:::::A:::::A            T:::::T        
  R::::RRRRRR:::::R  U:::::D     D:::::U   D:::::D     D:::::DR::::RRRRRR:::::R          A:::::A A:::::A                          J:::::J      A:::::A A:::::A                  A:::::A A:::::A           T:::::T        
  R:::::::::::::RR   U:::::D     D:::::U   D:::::D     D:::::DR:::::::::::::RR          A:::::A   A:::::A                         J:::::j     A:::::A   A:::::A                A:::::A   A:::::A          T:::::T        
  R::::RRRRRR:::::R  U:::::D     D:::::U   D:::::D     D:::::DR::::RRRRRR:::::R        A:::::A     A:::::A                        J:::::J    A:::::A     A:::::A              A:::::A     A:::::A         T:::::T        
  R::::R     R:::::R U:::::D     D:::::U   D:::::D     D:::::DR::::R     R:::::R      A:::::AAAAAAAAA:::::A           JJJJJJJ     J:::::J   A:::::AAAAAAAAA:::::A            A:::::AAAAAAAAA:::::A        T:::::T        
  R::::R     R:::::R U:::::D     D:::::U   D:::::D     D:::::DR::::R     R:::::R     A:::::::::::::::::::::A          J:::::J     J:::::J  A:::::::::::::::::::::A          A:::::::::::::::::::::A       T:::::T        
  R::::R     R:::::R U::::::U   U::::::U   D:::::D    D:::::D R::::R     R:::::R    A:::::AAAAAAAAAAAAA:::::A         J::::::J   J::::::J A:::::AAAAAAAAAAAAA:::::A        A:::::AAAAAAAAAAAAA:::::A      T:::::T        
RR:::::R     R:::::R U:::::::UUU:::::::U DDD:::::DDDDD:::::DRR:::::R     R:::::R   A:::::A             A:::::A        J:::::::JJJ:::::::JA:::::A             A:::::A      A:::::A             A:::::A   TT:::::::TT      
R::::::R     R:::::R  UU:::::::::::::UU  D:::::::::::::::DD R::::::R     R:::::R  A:::::A               A:::::A        JJ:::::::::::::JJA:::::A               A:::::A    A:::::A               A:::::A  T:::::::::T      
R::::::R     R:::::R    UU:::::::::UU    D::::::::::::DDD   R::::::R     R:::::R A:::::A                 A:::::A         JJ:::::::::JJ A:::::A                 A:::::A  A:::::A                 A:::::A T:::::::::T      
RRRRRRRR     RRRRRRR      UUUUUUUUU      DDDDDDDDDDDDD      RRRRRRRR     RRRRRRRAAAAAAA                   AAAAAAA          JJJJJJJJJ  AAAAAAA                   AAAAAAAAAAAAAA                   AAAAAAATTTTTTTTTTT      
                                                                                                                                                                                                                         
                                                                                                                                                                                                                         
                                                                                                                                                                                                                         
                                                                                                                                                                                                                         
                                                                                                                                                                                                                         
                                                                                                                                                                                                                         
                                                                                                                                                                                                                         
**"""



####
@app.on_message(filters.command('groupinfo') & filters.group)
def group_info(client, message):
    chat_id = message.chat.id
    chat_info = app.get_chat(chat_id)
    title = chat_info.title
    description = chat_info.description
    member_count = chat_info.members_count

    info_text = f"Group Title: {title}\nDescription: {description}\nMembers Count: {member_count}"
    message.reply_text(info_text)
