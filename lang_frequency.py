import tokenize
from optparse import OptionParser
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
    word_freq = [word_list.count(w) for w in word_list]
    word_freq_dict = dict(zip(word_list, word_freq))
    sorted_words = sorted(word_freq_dict.items(), key=lambda x: x[1])
    return [pair[0] for pair in sorted_words[-count:]][::-1]


if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-f", "--file", type="string", dest="filepath")
    parser.add_option("-c", "--count", type="int", dest="count")
    (options, args) = parser.parse_args()
    count = options.count if options.count else 10
    text = load_data(options.filepath)
    if text:
        for w in get_most_frequent_words(text, count):
            print(w)
