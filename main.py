from dotenv import load_dotenv
import os
import supabase

load_dotenv()

sburl = os.getenv('URL')
sbkey = os.getenv('Key')


