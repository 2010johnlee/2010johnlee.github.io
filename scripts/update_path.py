import os
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Replace with the path to your credentials JSON file.
credentials_file = 'credentials.json'

# Create a service account credentials object
credentials = service_account.Credentials.from_service_account_file(
    credentials_file
)

# Create a Google Drive API service
drive_service = build('drive', 'v3', credentials=credentials)

def list_files_in_folder(folder_id):
    try:
        results = drive_service.files().list(
            q=f"'{folder_id}' in parents",
            includeItemsFromAllDrives=True, 
            supportsAllDrives=True, 
            corpora="allDrives", 
            fields="nextPageToken, files(id, name)",
            orderBy="createdTime desc"
        ).execute()

        files = results.get('files', [])
        return files

    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def main():
    # Replace with the ID of the folder you want to list files from.
    folder_id = '1gAIUwRH-k3_VaHd8e5KFY4s704lRJGNc'

    files = list_files_in_folder(folder_id)
    #print(files)
    if not files:
        print(f'Can\'t load any file in folder {folder_id} ')
    else:
        # Get the web view link (URL) of the file
        file_url = files[0]['id']
        file_name = files[0]['name']
        print(files[0]['id'])
        print(f'https://drive.google.com/file/d/{file_url}')
	
        # Write the URL to a Markdown file
        with open('temp_temp.md', 'w') as md_file:
            md_file.write(f'{file_name},https://drive.google.com/uc?export=download&id={file_url}') 
		
	# wget --no-check-certificate 'https://drive.google.com/uc?export=download&id=FILE_ID' -O output_file_name

if __name__ == '__main__':
    main()
