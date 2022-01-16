import time

from controller import searchController as sc


print('🔑 - Enter you API URL :')
api_key = input('> ')
print('🔑 - How do your API key start? :')
api_key_start = input('> ')
print('🔑 - Now, enter your Github API :')
github_api = input('> ')

print(f'🔑 - Your API Code is : {api_key}')
print(f'🔑 - Your API Code start with : {api_key_start}...')
print(f'🔑 - Your Github API is : {github_api}')

print('⚙️ - Downloading data...')

try:
    print(f'✅ - Your API Keys is available here: ${sc.search_on_github(f"sort:author-date-desc {api_key}", api_key_start, github_api)}')
except Exception as e:
    print(f'❌ - Une erreur viens de ce produire : {e}')
    print('❌ - Nous allons réessayer dans 30 secondes...')
    time.sleep(30)
    print('⚙️ - Downloading data...')
    print(f'✅ - Your API Keys is available here: ${sc.search_on_github(f"sort:author-date-desc {api_key}", api_key_start, github_api)}')
