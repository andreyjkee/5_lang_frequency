import argparse
from collections import Counter
import re


def load_data(filepath):
    if not filepath:
        raise Exception('Не указан путь к файлу')
    with filepath as f:
        return f.read()

def get_most_frequent_words(text, count=10):
    word_list = re.findall(r'(\w+)', text)
    return [pair[0] for pair in Counter(word_list).most_common(count)]


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Get most frequent words")
    parser.add_argument("-f", "--file", type=argparse.FileType('r'), dest="filepath", required=True)
    parser.add_argument("-c", "--count", type=int, default=10)
    options = parser.parse_args()
    text = load_data(options.filepath)
    if text:
        for w in get_most_frequent_words(text, options.count):
            print(w)
