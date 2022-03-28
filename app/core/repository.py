import requests


class CoreRepository:
    def check_url_response_code(self, url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return True
            else:
                return False
        except:
            return False

core_repo = CoreRepository()