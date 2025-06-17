from googletrans import Translator

translator = Translator()
text_to_translate = input("Enter the text to translate: ")
target_language = input("Enter the target language (e.g., 'fr' for French): ")

translated = translator.translate(text_to_translate, dest=target_language)
print(translated.text)