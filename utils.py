import requests

checked_users = {}

def instagram_exists(username):
    username = username.lower().strip()

    if username in checked_users:
        return checked_users[username]

    url = f"https://www.instagram.com/{username}/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/122.0.0.0 Safari/537.36"
    }

    try:
        response = requests.head(url, headers=headers, timeout=5)
        is_valid = response.status_code == 200
        checked_users[username] = is_valid  # cache result
        return is_valid
    except requests.RequestException:
        checked_users[username] = False  # cache failure
        return False
