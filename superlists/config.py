from dotenv import load_dotenv
import os

load_dotenv()

DJANGO_SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")
