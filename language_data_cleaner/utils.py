import re
from bs4 import BeautifulSoup

def remove_urls(text: str) -> str:
    url_pattern = re.compile(r'https?://\S+|www\.\S+')
    return url_pattern.sub(r'', text)

def remove_html_tags(text: str) -> str:
    return BeautifulSoup(text, "html.parser").get_text()

def remove_special_characters(text: str) -> str:
    # Remove all characters except alphanumeric and basic punctuation
    return re.sub(r'[^a-zA-Z0-9\s.,!?\'"()<>]', '', text)