print ('hello,world')
texts = [
    "Привіт, як справи?",         # Українська
    "Hello, how are you?",        # Англійська
    "Bonjour, comment ça va?"     # Французька
]
from langdetect import detect

for text in texts:
    print(f"'{text}' -> {detect(text)}")
    print('hello,worlddddd')