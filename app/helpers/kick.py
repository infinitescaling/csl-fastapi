import cloudscraper
import json

def get_kick_info(username: str):
    url = "https://kick.com/stream/livestreams/en?username=" + username
    # headers = {
    #     "Authorization": f"Bearer {access_token}",
    #     "Client-Id": client_id,
    #     "Access-Control-Allow-Origin": "*",
    # }
    scraper = cloudscraper.create_scraper(
        delay=10, 
        browser={'custom': 'ScraperBot/1.0',});
    kick_response = scraper.get(url)
    print(f"kick_response: {kick_response.text}")
    if kick_response.status_code != 200:
        return False;
    print(f"kick_info_raw: {kick_response}")
    kick_info_json = kick_response.json()
    print(f"kick_info_json: {kick_info_json}")
    if kick_info_json["livestream"]:
        return {
            "url": f"kick.com/{username}"
        }
    return False;