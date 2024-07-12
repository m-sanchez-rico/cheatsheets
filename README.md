# Cheatsheets

Just a packages to get all my commads stored, and updated in all my computers. To make if avaliable from everywhere, Those cheatsheets are mirrared in Gits. Using a GitHub workflow, avery push to this repository will update the gists.

## Configurations:
If you want to create a new cheatsheet:
1. Create the new markdown file, snake_case.
2. Create the asociate gists as well, with the same name. Please add at least a dummy command, can not be empty.
3. Get the gist_id (example: 7bac0468121a1733efd5c6fa9a1df205), you can get it from the browser URL: https://gist.github.com/m-sanchez-rico/c393bd8cbb94bec36e2c2711ad8e8086
4. Add the gist_id and file name in `.github/scripts/update_gists.py`, Example:

``` python
# List of your gists and their corresponding file paths in the repository
GISTS = {
    '7bac0468121a1733efd5c6fa9a1df205': 'docker.md',
    'c393bd8cbb94bec36e2c2711ad8e8086': 'git.md',
    '3d636f41f02596abb320f7feb7e907f9': 'ubuntu.md',
    '03ad546d6ded5b0501d004e59a9a5f82': 'vs_code.md'
    # Add more gists and file paths as needed
}
```
Done, every time push in the main branch, the gist will be updated.

