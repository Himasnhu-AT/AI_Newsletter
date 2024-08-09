import requests
from datetime import datetime

date = datetime.now().strftime('%Y-%m-%d')

def get_github_repos(no_of_repo = 10, language='python'):
    """
    Get the top 10 repositories of a specific language, related to machine learning, from Github.

    Args:
        no_of_repo (int, optional): Number of repositories to fetch. Defaults to 10.
        language (str, optional): Language of the repositories to fetch. Defaults to 'python'.

    Returns:
        tuple: A tuple containing the language and a list of dictionaries, each containing the repository ID, name, URL, created date, and number of stars.
    """
    results = requests.get(f'https://api.github.com/search/repositories?q=machine%20Learning&language:{language}&sort=stars&order=desc&per_page={no_of_repo}').json()
    repo_list = []
    for repo in results['items']:
            d_tmp = {'repository_ID': repo['id'],
                    'name': repo['name'],
                    'URL': repo['html_url'],
                    'created_date': datetime.strptime(repo['created_at'], '%Y-%m-%dT%H:%M:%SZ'),
                    'number_of_stars': repo['stargazers_count']}
            repo_list.append(d_tmp)
    return language, repo_list
