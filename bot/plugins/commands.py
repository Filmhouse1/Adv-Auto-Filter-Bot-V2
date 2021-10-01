#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from bot import Translation, LOGGER # pylint: disable=import-error
from bot.database import Database # pylint: disable=import-error

db = Database()

@Client.on_message(filters.command(["start"]) & filters.private, group=1)
async def start(bot, update):
    
    try:
        file_uid = update.command[1]
    except IndexError:
        file_uid = False
    
    if file_uid:
        file_id, file_name, file_caption, file_type = await db.get_file(file_uid)
        
        if (file_id or file_type) == None:
            return
        
        caption = file_caption if file_caption != ("" or None) else ("<code>" + file_name + "</code>")
        try:
            await update.reply_cached_media(
                file_id,
                quote=True,
                caption = f"<code>{file_name}</code>\n \n🔊Group:https://t.me/joinchat/QdhQir0It3s3ZmJl\n \n🔊ᴍᴏᴠɪᴇꜱ ᴜᴘᴅᴀᴛᴇꜱ: @kl_films @FilmHouse_2\n \n🔊ʏᴏᴜᴛᴜʙᴇ ᴄʜᴀɴɴᴇʟ:https://youtube.com/c/THCV20\n \n🎗️ʝσιи 🎗️ ѕнαяє🎗️ ѕυρρσят",
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    'FILMHOUSE_Kerala', url="https://t.me/joinchat/QdhQir0It3s3ZmJl"
                                )
                        ]
                    ]
                )
            )
        except Exception as e:
            await update.reply_text(f"<b>Error:</b>\n<code>{e}</code>", True, parse_mode="html")
            LOGGER(__name__).error(e)
        return

    buttons = [[
        InlineKeyboardButton('⚜️ My Developer ⚜️', url='https://t.me/DS_KUNJAVA'),
        InlineKeyboardButton('🔰 ᴍᴏᴠɪᴇ ʜᴏᴜꜱᴇ 🔰', url ='https://t.me/movie_house2')
    ],[
        InlineKeyboardButton('FILM🎬HOUSE', url='https://t.me/joinchat/QdhQir0It3s3ZmJl'),
        InlineKeyboardButton('FILM🎬HOUSE_2', url='https://t.me/FilmHouse_2')
    ],[
        InlineKeyboardButton('KL_FILMS', url='https://t.me/kl_films'),
        InlineKeyboardButton('Kerala University News', url='https://t.me/All_Kerala_University')  
    ],[
        InlineKeyboardButton('💢 ʏᴏᴜᴛᴜʙᴇ ᴄʜᴀɴɴᴇʟ 💢', url='https://youtube.com/c/THCV20')        
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_photo(
        chat_id=update.chat.id,
        photo="https://telegra.ph/file/fad937b0c0ef864d06d2e.jpg",
        caption=Translation.START_TEXT.format(
                update.from_user.first_name),
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["help"]) & filters.private, group=1)
async def help(bot, update):
    buttons = [[
        InlineKeyboardButton('Home ⚡', callback_data='start'),
        InlineKeyboardButton('About 🚩', callback_data='about')
    ],[
        InlineKeyboardButton('Close 🔐', callback_data='close')
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_TEXT,
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["about"]) & filters.private, group=1)
async def about(bot, update):
    
    buttons = [[
        InlineKeyboardButton('Home ⚡', callback_data='start'),
        InlineKeyboardButton('Close 🔐', callback_data='close')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.ABOUT_TEXT,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )
