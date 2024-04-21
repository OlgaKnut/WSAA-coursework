
# PyGithub was installed

from github import Github
import requests
#config file has apikey in it
from config import config as cfg

filename = "Andrew.txt"
url = 'https://api.github.com/repos/OlgaKnut/aprivateone/'

apikey = cfg["githubapikey"]

g = Github(apikey)

repo=g.get_repo("OlgaKnut/aprivateone")
fileInfo=repo.get_contents("Andrew.txt")
urlOfFile = fileInfo.download_url
#to get original text
response = requests.get(urlOfFile)
#to make changes in text
file_new_text=response.text.replace("Andrew","Olga")
#to push file with ghanges and replace the old one
gitHubResponse=repo.update_file(fileInfo.path,"Andrew replaced with Olga",file_new_text,fileInfo.sha)
