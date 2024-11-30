from selectorlib import Extractor
import requests

class Temperature:

    base_url = 'https://www.timeanddate.com/weather/'
    yml_path = 'temperature.yaml'


    def __init__(self, country, city):
        self.country = country.replace(' ', '-')
        self.city = city.replace(' ', '-')

    def _build_url(self):
        url = self.base_url + f'{self.country}/{self.city}/'
        return url

    def _scrape(self):

        url = self._build_url()
        extractor = Extractor.from_yaml_file(self.yml_path)
        resp = requests.get(url)
        full_content = resp.text
        raw_content = extractor.extract(full_content)
        return raw_content

    def get(self):

        scraped_content = self._scrape()
        return float(scraped_content['temp'].replace("°C", " ").strip())

if __name__ == '__main__':
    india = Temperature('india', 'pune')
    print(india.get())