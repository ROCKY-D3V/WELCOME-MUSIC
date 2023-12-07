from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from DAXXMUSIC import app
from config import BOT_USERNAME

start_txt = """**
✪ ωεℓ¢σмє тσ χᴅ яєρσ ✪
 
 ➲ ᴀʟʟ ʀᴇᴘᴏ ᴇᴀsɪʟʏ ᴅᴇᴘʟᴏʏ ᴏɴ ʜᴇʀᴏᴋᴜ ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ᴇʀʀᴏʀ ✰
 
 ➲ ɴᴏ ʜᴇʀᴏᴋᴜ ʙᴀɴ ɪssᴜᴇ ✰
 
 ➲ ɴᴏ ɪᴅ ʙᴀɴ ɪssᴜᴇ ✰
 
 ➲ᴜɴʟɪᴍɪᴛᴇᴅ ᴅʏɴᴏs ✰
 
 ➲ ʀᴜɴ 24x7 ʟᴀɢ ғʀᴇᴇ ᴡɪᴛʜᴏᴜᴛ sᴛᴏᴘ ✰
 
 ► ɪғ ʏᴏᴜ ғᴀᴄᴇ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ᴛʜᴇɴ sᴇɴᴅ ss
**"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("Δᴅᴅ ᴍє", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("нєℓρ", url="https://t.me/ITZ_4_U/2"),
          InlineKeyboardButton("σωиєя", url="https://t.me/ROCKY_ISS_BACK"),
          ],
               [
                InlineKeyboardButton("Δʙᴏᴜᴛ ʀᴏᴄᴋყ", url="https://t.me/II_ROCKY_II"),

],
[
              InlineKeyboardButton("「ϰ∂ ⚚ ϐοτz」", url=f"https://t.me/XD_BOTX"),
              InlineKeyboardButton("︎「ϰ∂ ⚚ иєƚωσɾƙ」", url=f"https://t.me/XD_N3TWORK"),
              ],
              [
              InlineKeyboardButton("⏤͟͟͞͞ 𓆩𝐃ᴇᴄᴇɴᴛ ། ། 𝐂ʜᴀᴛɪɴɢ𓆪『 𝐂ʟᴜʙ 2", url=f"https://t.me/DECENT_CHATING"),
InlineKeyboardButton("ᴅᴘ ᴡᴏʀʟᴅ", url=f"https://t.me/OFFICAL_DP_ZONE"),
],
[
InlineKeyboardButton("sᴛʀɪɴɢʙᴏᴛ", url=f"https://t.me/XD_STRING_BOT"),
InlineKeyboardButton("ғᴇᴅᴇʀᴀᴛɪᴏɴ", url=f"https://t.me/officeal_warrior_fedration"),
],
[
              InlineKeyboardButton("ᴍᴜsɪᴄ ʙᴏᴛ ʀᴇᴘᴏ", url=f"https://t.me/N91Ab/6"),
              InlineKeyboardButton("sƚΔƚυs", url=f"https://t.me/About_Dangerous"),
              ],
              [
              InlineKeyboardButton("𝗞ɪᴅѕ 𝗢ғ 𝗧ᴇʟᴇɢʀᴀᴍ︎", url=f"https://t.me/ho_gya_viral"),
InlineKeyboardButton("ɪɴsᴛᴀ", url=f"https://instagram.com/mr_._rocky_._01?igshid=MzNlNGNkZWQ4Mg=="),
],
[
InlineKeyboardButton("ᴡʜᴀᴛsᴀᴘᴘ", url=f"https://wa.me/qr/474QNG5BZYHRM1"),
InlineKeyboardButton("ᴜᴘᴄᴏᴍɪɴɢ", url=f"https://t.me/admin"),
],
[
InlineKeyboardButton("𝐏𝐀𝐍𝐃𝐀 | 𝐃𝐏𝐙 | 𝐄𝐃𝐈𝐓𝐙 ✨", url=f"https://t.me/PANDA_DPZ_EDITZ"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://graph.org/file/360676a2c160029e03e46.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
