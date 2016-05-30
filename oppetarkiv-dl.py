import requests
import youtube_dl
from bs4 import BeautifulSoup

def program_urls():
    page = requests.get("http://www.oppetarkiv.se/program")
    soup = BeautifulSoup(page.content, 'html.parser')
    a = soup.find_all('a')

    for x in a:
        href = x.get('href')
        if isinstance(href, str) and 'etikett' in href:
            url = "http://www.oppetarkiv.se{}".format(href)
            yield url

def video_urls(program):
    videos = []
    page = requests.get(program)
    soup = BeautifulSoup(page.content, 'html.parser')

    a = soup.find_all('a')

    for x in a:
        href = x.get('href')
        if isinstance(href, str) and 'video' in href:
            url = "http://www.oppetarkiv.se{}".format(href)
            yield url

def download(videos):
    ytdl = youtube_dl.YoutubeDL()
    ytdl.download(videos)

def main():
    programs = program_urls()
    for program in programs:
        videos = video_urls(program)
        for video in videos:
            download([video])
            print("\n")

if __name__ == "__main__":
    main()

