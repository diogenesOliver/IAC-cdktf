from dotenv import load_dotenv
import os

load_dotenv()

value = os.environ['KEY_TEST']
print(value)