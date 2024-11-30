import requests

class APIConnector:
    def __init__(self, base_url):
        self.base_url = base_url

    def send_request(self, endpoint, method="GET", data=None, headers=None):
        url = f"{self.base_url}/{endpoint}"
        try:
            if method.upper() == "GET":
                response = requests.get(url, headers=headers)
            elif method.upper() == "POST":
                response = requests.post(url, json=data, headers=headers)
            else:
                raise ValueError("Unsupported HTTP method.")
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error during API call: {e}")
            return None
