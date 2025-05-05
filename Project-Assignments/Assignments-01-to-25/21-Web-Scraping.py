import requests
from bs4 import BeautifulSoup as bs

github_user = input('Input Github User: ')
url = f"https://github.com/{github_user}"
r = requests.get(url)
soup = bs(r.content, "html.parser") # html.parser is the parser that BeautifulSoup uses to parse the content
profile_img = soup.find('img', {'class' : 'avatar'})['src']
print(profile_img) # Output: https://avatars.githubusercontent.com/u/12345678?v=4