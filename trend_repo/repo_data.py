import requests
import json
from datetime import datetime, timedelta
from collections import Counter

today = datetime.now()
date = today - timedelta(days=10)


today = datetime.now()
date = today - timedelta(days=10)

url = "https://api.github.com/search/repositories?q=create:>{date}z&sort=stars&order=desc"
response = requests.get(url)
data = response.json()
repo_data_list = data['items']
final_repo = repo_data_list[:3]

language = []
lang_num=[]
for repo in final_repo:
    language.append(repo['language'])
for lang in repo_data_list:
    if lang['language'] in language:
        lang_num.append(lang['language'])
final_lang = Counter(lang_num)