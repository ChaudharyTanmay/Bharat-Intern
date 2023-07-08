from googletrans import Translator

def translate_text(text, target_lang):
    translator = Translator(service_urls=['translate.google.com'])
    translation = translator.translate(text, dest=target_lang)
    return translation.text

source_text = input("Enter the text you want to translate: ")
target_lang = input("Enter the target language: ")

translated_text = translate_text(source_text, target_lang)
print("Translated Text:", translated_text)
