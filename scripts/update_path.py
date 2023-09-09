from google.oauth2 import service_account
from googleapiclient.discovery import build

# Replace 'your-credentials.json' with the path to your Google Cloud credentials JSON file
credentials_file = 'your-credentials.json'
file_path = '/path/to/your/file/on/google/drive/filename.ext'

# Load credentials from the JSON file
credentials = service_account.Credentials.from_service_account_file(
    credentials_file, scopes=['https://www.googleapis.com/auth/drive.readonly'])

# Create a Drive API service
drive_service = build('drive', 'v3', credentials=credentials)

# Search for the file
results = drive_service.files().list(q=f"name='{file_path}'").execute()
files = results.get('files', [])

if not files:
    print(f'File "{file_path}" not found on Google Drive.')
else:
    # Get the web view link (URL) of the file
    file_url = files[0]['webViewLink']

    # Write the URL to a Markdown file
    with open('output.md', 'w') as md_file:
        md_file.write(f'[Link Text]({file_url})')
