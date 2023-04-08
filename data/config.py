import os
from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = env.str("BOT_TOKEN")  # Bot Token
ADMINS = env.list("ADMINS")  # adminlar ro'yxati

DATABASE_URL = env.str("DATABASE_URL")
PGDATABASE = env.str("PGDATABASE")
PGHOST = env.str("PGHOST")
PGPASSWORD = env.str("PGPASSWORD")
PGPORT = env.str("PGPORT")
PGUSER = nev.str("PGUSER")
