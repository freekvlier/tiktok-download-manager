import os
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials, firestore

# Load environment variables from .env file
load_dotenv()

credentials_path = os.getenv('FIREBASE_CREDENTIALS_PATH')

# Initialize Firebase Admin using the credentials JSON specified in the .env file
cred = credentials.Certificate(credentials_path)
firebase_admin.initialize_app(cred)

# Connect to Firestore Database
db = firestore.client()

class FirebaseManager:
    def __init__(self):
        self.collection = db.collection('downloaded_videos')

    def is_url_downloaded(self, url):
        # Check if the URL is already in the database
        docs = self.collection.where('url', '==', url).get()
        return len(docs) > 0

    def add_downloaded_url(self, url):
        # Add a new URL to the database
        self.collection.add({'url': url})
