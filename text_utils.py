def clean_text(text):
    text = text.lower()
    return text


sample = "Machine Learning, Is FUN!"
print(clean_text(sample))

# Remove Symbols

def clean_text(text):
    text = text.lower()
    text = text.replace("!", "")
    text = text.replace(".", "")
    text = text.replace(",", "")
    return text


sample = "Machine Learning, is FUN!"
print(clean_text(sample))

#Split text into Words

def get_words(text):
    return text.split()


text = clean_text("ML engineers build real systems!")
words = get_words(text)
print(words)
