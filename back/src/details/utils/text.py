def short_text(text):
    return text.replace('\n', ' ').strip()[:1000]

def remove_newlines(text):
    return text.replace('\n', ' ')