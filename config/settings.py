import os

from dotenv import load_dotenv

load_dotenv()


ENVIRONMENT = os.getenv("ENVIRONMENT", "QA")

BASE_URL = os.getenv("BASE_URL")
