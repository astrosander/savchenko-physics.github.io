import re
import os
import glob

def extract_number_from_path(file_path):
    match = re.search(r'\\\d+\.(\d+)\.', file_path)
    if match:
        return str(match.group(1))
    else:
        return None


def find_and_replace(file_path, old_word, new_word):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # Use regular expression to find and replace the word
        # modified_content = re.sub(r'\b' + re.escape(old_word) + r'\b', new_word, content)
        
        # new_word = '<a href="../#'+extract_number_from_path(file_path)+'">←Назад</a>'
        print(file_path, new_word)
        modified_content = content.replace(old_word, new_word)

        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(modified_content)

        # print(f"Word '{old_word}' replaced with '{new_word}' in {file_path}")

    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

def find_pdfs(directory='.'):
    pdf_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                pdf_files.append(os.path.join(root, file))
    return pdf_files


current_folder = 'C:\\Users\\melnichenkaa\\OneDrive - Berea College\\Documents\\GitHub\\savchenko-physics.github.io\\en'  # Change this to the desired folder path
pdf_files_list = find_pdfs(current_folder)

new_word = """    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="content-language" content="en">
    <meta name="keywords" content="Savchenko Problems in Physics, Savchenko solutions, physics problems, physics olympiad preparation, IPhO, Jaan Kalda">
    <meta name="description" content="The largest dataset of solutions of 'Savchenko. Problems in Physics'. Savchenko’s Problems in General Physics is widely used to prepare for olympiads and it is a useful tool to
master and sharpen your skills and techniques in comptetitive problem solving. Some of these problems were a source
of inspiration for Jaan Kalda’s handouts and to some NBPhO problems. You may find problems from old IPhO
papers.">
    <meta name="author" content="Aliaksandr Melnichenka">
    <meta name="date" content="2023-10" scheme="YYYY-MM">
    <meta property="og:title" content="Savchenko Solutions">
    <meta property="og:image" content="img/logo.png">
    <meta property="og:description" content="A website with solutions to physics problems from Savchenko Textbook">
    <meta name="yandex-verification" content="6cfda41f74038368">
    <title>Savchenko Solutions</title>"""
old_word = """    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="content-language" content="en">
    <meta name="keywords" content="solutions, savchenko, physics problems, olympiad physics, physics book">
    <meta name="description" content="A website with solutions to physics problems from Savchenko Textbook">
    <meta property="og:title" content="Savchenko Solutions">
    <meta property="og:image" content="img/logo.png">
    <meta property="og:description" content="A website with solutions to physics problems from Savchenko Textbook">
    <meta name="yandex-verification" content="6cfda41f74038368">
    <title>Savchenko Solutions</title>"""


for pdf_file in pdf_files_list:
    find_and_replace(pdf_file, old_word, new_word)
