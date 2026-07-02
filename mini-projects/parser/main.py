import requests
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator



html = requests.get("https://beautiful-soup-4.readthedocs.io/en/latest/").text

soup = BeautifulSoup(html, "html.parser")
titles = soup.find_all("p")

translator = GoogleTranslator(source = 'auto', target = 'uk')

for t in titles:
    text = t.get_text(strip=True)
    if text:
        translated_text = translator.translate(text)
        print(translated_text)
        


