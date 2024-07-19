import requests
import os

# Your GitHub personal access token
TOKEN = os.getenv('TOKEN_FOR_GISTS')

# List of your gists and their corresponding file paths in the repository
GISTS = {
    '7bac0468121a1733efd5c6fa9a1df205': 'docker.md',
    'c393bd8cbb94bec36e2c2711ad8e8086': 'git.md',
    '3d636f41f02596abb320f7feb7e907f9': 'ubuntu.md',
    '03ad546d6ded5b0501d004e59a9a5f82': 'vs_code.md',
    '78c47c75715eb99a4b4d51afe8a84347': 'vim.md'
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
