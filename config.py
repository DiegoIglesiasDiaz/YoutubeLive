from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access environment variables
YOUTUBE_KEY = os.getenv('YOUTUBE_KEY')
VIDEO_DIRECTORY = os.getenv('VIDEO_DIRECTORY')

