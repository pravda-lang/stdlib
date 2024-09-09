import requests
def main(url):
    return requests.get(url).text
