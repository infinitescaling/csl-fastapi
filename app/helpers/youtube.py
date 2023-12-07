from requests_html import HTMLSession
from bs4 import BeautifulSoup


def get_youtube_info(username: str):
    video_url = f"https://www.youtube.com/{username}/live"
    session = HTMLSession()
    response = session.get(video_url)
    response.html.render(sleep=60)
    soup = BeautifulSoup(response.html.html, "lxml")

    if soup.select_one('#info-strings').text[:8] == 'Streamed':
        video_type = 'live'
        return True
    else:
        video_type = 'video'
        return False
    