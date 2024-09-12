import re
from deep_translator import GoogleTranslator
previous_text = ""
def translate_russian_to_english(text):
    pattern = re.compile(r'\$\$(.*?)\$\$', re.DOTALL)
    
    parts = pattern.split(text)
    
    translator = GoogleTranslator(source='auto', target='en')
    
    for i in range(0, len(parts), 2):  # only translate even indices (outside $$)
        parts[i] = translator.translate(parts[i])
    
    translated_text = ""
    for i in range(len(parts)):
        if i % 2 == 0:
            translated_text += parts[i]  # Translated part
        else:
            translated_text += f'\n$$ {parts[i]} $$\n'  # Untranslated math expression
            
    return translated_text

def save_to_file(translated_text, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(translated_text)

def read_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()


while True:
    # Import the Russian text from a .txt file
    input_filename = "database/russian.txt"  # Replace with your actual file path
    russian_text = read_from_file(input_filename)

    if russian_text == previous_text:
        continue

    translated_text = translate_russian_to_english(russian_text)

    output_filename = "database/translated_text.txt"
    save_to_file(translated_text, output_filename)
    print(translated_text)
    previous_text = russian_text
    
