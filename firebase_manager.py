import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase Admin using the credentials JSON you downloaded
cred = credentials.Certificate('video-download-manager-9af41-firebase-adminsdk-n1vba-62a864c90f.json')
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

# Example usage:
if __name__ == "__main__":
    manager = FirebaseManager()
    test_url = "http://example.com/video123"

    if manager.is_url_downloaded(test_url):
        print("This video has already been downloaded.")
    else:
        print("Downloading video...")
        # Code to download the video
        # ...
        print("Video downloaded successfully.")
        manager.add_downloaded_url(test_url)
