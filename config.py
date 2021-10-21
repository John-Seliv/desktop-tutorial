import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), 'jj.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)
token = os.getenv("TOKEN")
#print(token)