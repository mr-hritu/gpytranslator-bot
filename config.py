from pyrogram import filters
API_ID: int = 28888037
API_HASH: str = "9fbe164b5591df05fbd8577e3b1d6d21"
TOKEN: str = "6660071929:AAH6JvMfr3uNEEOVkR1YTZq7c5tPrx-Jc64"

sudousers: list = [6387027582,5190902724]
sudofilter = filters.user(sudousers)
db_url: str = "sqlite://userlanguages.db"
