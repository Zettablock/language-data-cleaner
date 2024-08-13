from cleantext import clean
import pandas as pd
from dataclasses import dataclass
from exceptions import ValueFormatError

@dataclass
class CleanConfig:
    fix_unicode: bool = True
    to_ascii: bool = True,
    lower: bool = True
    no_line_breaks: bool = False,
    no_urls: bool = False,
    no_emails: bool = False,
    no_phone_numbers: bool = False
    no_numbers: bool = False
    no_digits: bool = False
    no_currency_symbols: bool = False
    no_punct: bool = False
    no_emoji: bool = True
    replace_with_url: str = ""
    replace_with_punct: str = ""
    replace_with_number: str = ""


class LanguageDataCleaner:
    def __init__(self, output_format: str, config: dict = None, clean_config: CleanConfig = None):
        self.output_format = output_format
        self.config = config if config else {}
        self.clean_config = clean_config if clean_config else CleanConfig()

    def load_data(self, filepath: str):
        if filepath.endswith('csv'):
            self.data = pd.read_csv(filepath)
        elif filepath.endswith('jsonl'):
            self.data = pd.read_json(filepath, lines=True)
        else:
            raise ValueFormatError(f"Unsupported input format: {filepath}")

    def clean_data(self):
        if 'text_column' in self.config:
            self.data[self.config['text_column']] = self.data[self.config['text_column']].apply(self._clean_text)

    def _clean_text(self, text: str) -> str:
        return clean( 
            text,
            fix_unicode=self.clean_config.fix_unicode,
            to_ascii=self.clean_config.to_ascii,
            lower=self.clean_config.lower,
            no_line_breaks=self.clean_config.no_line_breaks,
            no_urls=self.clean_config.no_urls,
            no_emails=self.clean_config.no_emails,
            no_phone_numbers=self.clean_config.no_phone_numbers,
            no_numbers=self.clean_config.no_numbers,
            no_digits=self.clean_config.no_digits,
            no_currency_symbols=self.clean_config.no_currency_symbols,
            no_punct=self.clean_config.no_punct,
            no_emoji=self.clean_config.no_emoji,
            replace_with_url=self.clean_config.replace_with_url,
            replace_with_punct=self.clean_config.replace_with_punct,
            replace_with_number=self.clean_config.replace_with_number
        )

    def save_data(self, filepath: str):
        if self.output_format == 'csv':
            self.data.to_csv(filepath, index=False)
        elif self.output_format == 'jsonl':
            self.data.to_json(filepath, orient='records', lines=True)
        else:
            raise ValueFormatError(f"Unsupported output format: {self.output_format}")




def main():
    # Example usage of CleanConfig
    custom_clean_config = CleanConfig()

    cleaner = LanguageDataCleaner(output_format='csv', config={'text_column': 'text'}, clean_config=custom_clean_config)
    cleaner.load_data('./data/sample_data.csv')
    cleaner.clean_data()
    cleaner.save_data('./data/cleaned_data.csv')

if __name__ == '__main__':
    main()