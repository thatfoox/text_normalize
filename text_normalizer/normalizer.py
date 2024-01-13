import unicodedata
from unidecode import unidecode


class TextNormalizer:
    def normalize(self, text: str) -> str:
        """
        Normalize text by converting emoji-letters to their corresponding English alphabet letters and
        transforming UTF look-alike characters to their standard English alphabet equivalents.
        Arguments:
            :param text: The input text to be normalized
        Returns:
            :returns normalized_text: The normalized text
        """
        # Normalizing the text to Unicode NFKD form to decompose characters
        normalized_text = unicodedata.normalize('NFKD', text)

        # Transforming UTF look-alikes to standard English alphabet
        normalized_text = unidecode(normalized_text)
        return normalized_text
