'''
Взять из папки formats.json.xml файлы с новостями newsafr.json и newsafr.xml
Написать программу, которая будет выводить топ 10 самых часто встречающихся
в новостях слов длиннее 6 символов для каждого файла.
Не забываем про декомпозицию и организацию кода в функции.
В решении домашнего задания вам могут помочь: split(), sort или sorted.
'''

import json
from pprint import pprint
"""Работа с файлом .json"""

def open_file(name_file):
    with open(name_file, encoding='utf-8') as f:
        json_data = json.load(f)
    return json_data
# print(open_file('newsafr.json'))

def list_words_json(file_contents):
 news = file_contents["rss"]["channel"]["items"]
 results = []
 for new in news:
  results.append(new['description'].split())
 return results
# print(list_words_json(open_file('newsafr.json')))

def filtration_by_length(list_news,min_len):
    filtr_list = []
    for news in list_news:
        for word in news:
         if len(word) > min_len:
            filtr_list.append(word)
    return filtr_list
# print(filtration_by_length(list_words_json(open_file('newsafr.json')),6))

def word_repetition_rate(word_list):
    word_periodicity = {}
    for word in word_list:
        word_periodicity[word] = word_periodicity.get(word, 0) + 1
    return word_periodicity
# pprint(word_repetition_rate(filtration_by_length(list_words_json(open_file('newsafr.json')),6)))

def sorted_word_periodicity(dict_word_periodicity):
    word_periodicity_sorted = sorted(dict_word_periodicity.items(), key=lambda x: x[1], reverse=True)
    return word_periodicity_sorted[0:10]
# pprint(sorted_word_periodicity(word_repetition_rate(filtration_by_length(list_words_json(open_file('newsafr.json')),6))))

def output_popular_word_in_json(sorted_words):
    popular_words = ''
    # print(list(sorted_words))
    for elem in sorted_words:
        popular_words += elem[0] + '\n'
    return f'Топ 10 самых часто встречающихся в новостях слов длиннее 6 символов:\n{popular_words}'
print(output_popular_word_in_json(sorted_word_periodicity(word_repetition_rate(filtration_by_length(list_words_json(open_file('newsafr.json')),6)))))





"""Работа с файлом .xml"""

import xml.etree.ElementTree as ET
def open_file(name_file):
    parser = ET.XMLParser(encoding="utf-8")
    tree = ET.parse(name_file, parser)
    root = tree.getroot()
    items = root.findall("channel/item")
    return items
# print(open_file("newsafr.xml"))

def list_words_xml(file_contents):
 results = []
 for item in file_contents:
  results.append(item.find('description').text.split())
 return results
# print(list_words_xml(open_file("newsafr.xml")))

def filtration_by_length(list_news,min_len):
    filtr_list = []
    for news in list_news:
        for word in news:
         if len(word) > min_len:
            filtr_list.append(word)
    return filtr_list
# print(filtration_by_length(list_words_xml(open_file("newsafr.xml")),6))

def word_repetition_rate(word_list):
    word_periodicity = {}
    for word in word_list:
        word_periodicity[word] = word_periodicity.get(word, 0) + 1
    return word_periodicity
# pprint(word_repetition_rate(filtration_by_length(list_words_xml(open_file("newsafr.xml")),6)))

def sorted_word_periodicity(dict_word_periodicity):
    word_periodicity_sorted = sorted(dict_word_periodicity.items(), key=lambda x: x[1], reverse=True)
    return word_periodicity_sorted[0:10]
# pprint(sorted_word_periodicity(word_repetition_rate(filtration_by_length(list_words_xml(open_file("newsafr.xml")),6))))

def output_popular_word_in_xml(sorted_words):
    popular_words = ''
    for elem in sorted_words:
        popular_words += elem[0] + '\n'
    return f'Топ 10 самых часто встречающихся в новостях слов длиннее 6 символов:\n{popular_words}'
print(output_popular_word_in_xml(sorted_word_periodicity(word_repetition_rate(filtration_by_length(list_words_xml(open_file("newsafr.xml")),6)))))
