import time

from controller import searchController as sc


print('π - Enter you API URL :')
api_key = input('> ')
print('π - How do your API key start? :')
api_key_start = input('> ')
print('π - Now, enter your Github API :')
github_api = input('> ')

print(f'π - Your API Code is : {api_key}')
print(f'π - Your API Code start with : {api_key_start}...')
print(f'π - Your Github API is : {github_api}')

print('βοΈ - Downloading data...')

try:
    print(f'β - Your API Keys is available here: ${sc.search_on_github(f"sort:author-date-desc {api_key}", api_key_start, github_api)}')
except Exception as e:
    print(f'β - Une erreur viens de ce produire : {e}')
    print('β - Nous allons rΓ©essayer dans 30 secondes...')
    time.sleep(30)
    print('βοΈ - Downloading data...')
    print(f'β - Your API Keys is available here: ${sc.search_on_github(f"sort:author-date-desc {api_key}", api_key_start, github_api)}')
