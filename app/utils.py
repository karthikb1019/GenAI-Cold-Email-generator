import re


def clean_text(text):
    """
    Clean and normalize text by removing HTML, URLs, special characters, and extra whitespace
    """
    # Remove HTML tags
    text = re.sub(r'<[^>]*?>', '', text)

    # Remove URLs (http, https, www)
    text = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', text)
    text = re.sub(r'www\.(?:[a-zA-Z]|[0-9]|[$-_@.&+])+\.[a-zA-Z]{2,}', '', text)

    # Remove email addresses
    text = re.sub(r'\S+@\S+', '', text)

    # Remove special characters but keep basic punctuation
    text = re.sub(r'[^a-zA-Z0-9\s\.,!?\-]', '', text)

    # Replace multiple spaces with single space
    text = re.sub(r'\s+', ' ', text)

    # Remove leading and trailing whitespace
    text = text.strip()

    return text



