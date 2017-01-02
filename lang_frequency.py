import tokenize
from optparse import OptionParser
from collections import Counter
import re


def load_data(filepath):
    if not filepath:
        raise Exception('Не указан путь к файлу')
    try:
        with tokenize.open(filepath) as f:
            return f.read()
    except FileNotFoundError:
        print('Файл : ', filepath, 'не найден')


def get_most_frequent_words(text, count=10):
    word_list = re.findall(r'(\w+)', text)
    return [pair[0] for pair in Counter(word_list).most_common(count)]


if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-f", "--file", type="string", dest="filepath")
    parser.add_option("-c", "--count", type="int", dest="count", default=10)
    options, args = parser.parse_args()
    if not options.filepath:
        parser.error('Option -f is required')
    text = load_data(options.filepath)
    if text:
        for w in get_most_frequent_words(text, options.count):
            print(w)
