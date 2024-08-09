import requests
from datetime import datetime

date = datetime.now().strftime('%Y-%m-%d')

def get_github_repos(no_of_repo = 10, language='python'):
        results = requests.get(f'https://api.github.com/search/repositories?q=language:{language}&sort=stars&order=desc&per_page={no_of_repo}').json()
        repo_list = []
        for repo in results['items']:
                d_tmp = {'repository_ID': repo['id'],
                        'name': repo['name'],
                        'URL': repo['html_url'],
                        'created_date': datetime.strptime(repo['created_at'], '%Y-%m-%dT%H:%M:%SZ'),
                        'number_of_stars': repo['stargazers_count']}
                repo_list.append(d_tmp)
        return language, repo_list
