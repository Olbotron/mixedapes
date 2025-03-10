import requests
import base64
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

client_id = os.getenv('SPOTIFY_CLIENT_ID')
client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')

# Encode client ID and client secret
auth_str = f"{client_id}:{client_secret}"
b64_auth_str = base64.b64encode(auth_str.encode()).decode()

# Get access token
token_url = "https://accounts.spotify.com/api/token"
headers = {
    "Authorization": f"Basic {b64_auth_str}",
    "Content-Type": "application/x-www-form-urlencoded"
}
data = {
    "grant_type": "client_credentials"
}

response = requests.post(token_url, headers=headers, data=data)
response_data = response.json()
access_token = response_data.get("access_token")

if not access_token:
    raise Exception("Could not get access token")

# Simplified search query
query = "track:epic artist:faith no more"
search_url = "https://api.spotify.com/v1/search"
headers = {
    "Authorization": f"Bearer {access_token}"
}
params = {
    "q": query,
    "type": "track",
    "limit": 1
}

response = requests.get(search_url, headers=headers, params=params)
search_results = response.json()

# Check if any tracks were found
if not search_results['tracks']['items']:
    raise Exception("No tracks found")

# Extract album art URL directly from search results
album_art_url = search_results['tracks']['items'][0]['album']['images'][0]['url']
print(f"Album Art URL: {album_art_url}")