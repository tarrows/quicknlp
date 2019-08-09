from pathlib import Path
from bs4 import BeautifulSoup

p = Path('resources')
files = list(p.iterdir())

html = files[0].read_text()
soup = BeautifulSoup(html, 'html.parser')
soup.find('ul')
