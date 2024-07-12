import requests
import os

# Your GitHub personal access token
TOKEN = os.getenv('TOKEN_FOR_GISTS')

# List of your gists and their corresponding file paths in the repository
GISTS = {
    '7bac0468121a1733efd5c6fa9a1df205': 'docker.md',
    
    # Add more gists and file paths as needed
}

def update_gist(gist_id, file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    
    url = f'https://api.github.com/gists/{gist_id}'
    headers = {
        'Authorization': f'token {TOKEN}',
        'Accept': 'application/vnd.github.v3+json',
    }
    data = {
        'files': {
            os.path.basename(file_path): {
                'content': content
            }
        }
    }
    print(f'Updating gist {gist_id}...')
    print(f'URL: {url}')
    print(f'Headers: {headers}')
    print(f'Data: {data}')
    response = requests.patch(url, json=data, headers=headers)
    if response.status_code == 200:
        print(f'Successfully updated gist {gist_id}')
    else:
        print(f'Failed to update gist {gist_id}: {response.json()}')

if __name__ == '__main__':
    for gist_id, file_path in GISTS.items():
        update_gist(gist_id, file_path)
