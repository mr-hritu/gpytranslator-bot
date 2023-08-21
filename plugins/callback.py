from pyrogram import Client, filters
from pyrogram.types import CallbackQuery
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup 
from pyrogram.errors import UserBannedInChannel, UserNotParticipant
import constants


@Client.on_message(filters.text & filters.private & filters.incoming)
async def fore(c, m):
      try:
        chat = await c.get_chat_member(-1001785446911, m.from_user.id)
        if chat.status=="kicked":
           await c.send_message(chat_id=m.chat.id, text="You are Banned ☹️\n\n📝 If u think this is an ERROR message in @Privates_chats", reply_to_message_id=m.id)
           m.stop_propagation()
      except UserBannedInChannel:
         return await c.send_message(chat_id=m.chat.id, text="Hai you made a mistake so you are banned from channel so you are banned from me too 😜")
      except UserNotParticipant:
          button = [[InlineKeyboardButton('Updates Channel 🇮🇳', url='https://t.me/Private_Bots')]]
          markup = InlineKeyboardMarkup(button)
          return await c.send_message(chat_id=m.chat.id, text="""Hai bro,\n\nYou must join my channel for using me.\n\nPress this button to join now 👇""", reply_markup=markup)
      m.continue_propagation()

@Client.on_callback_query(filters.regex(r"^back$"))
async def backtostart(bot: Client, query: CallbackQuery):
    await query.message.edit(
        constants.start_message_text.format(query.from_user.mention()),
        reply_markup=constants.start_message_reply_markup,
    )


@Client.on_callback_query(filters.regex(r"^help$"))
async def helpbutton(bot: Client, query: CallbackQuery):
    await query.message.edit(constants.help_text, reply_markup=constants.help_markup)


@Client.on_callback_query(filters.regex(r"^Credits$"))
async def credits(bot: Client, query: CallbackQuery):
    await query.answer(constants.credits, show_alert=True)


@Client.on_callback_query(filters.regex(r"^closethismsg$"))
async def close_error_message_callback(bot: Client, query: CallbackQuery):
    await query.message.delete()
