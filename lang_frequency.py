import os
import re


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath,'r', encoding='utf-8') as file:
        data = file.read()
        return data	


def get_most_frequent_words(text):
    word_frequency = dict()
    cleared_text = re.findall(r'[^\d|\W]+', text)
    for word in cleared_text:
        if word in word_frequency:
            word_frequency[word]+=1
        else:
            word_frequency[word] = 1
    return word_frequency


if __name__ == '__main__':
    filepath = input("Введите путь к файлу: ")
    text = load_data(filepath)
    if text is None:
        print("Файла или папки с таким названием не существует.")
    else:    
        frequency_words = get_most_frequent_words(text)
        for word, frequency in sorted(frequency_words.items(), key=lambda val:val[1], reverse=True)[:10]:
            print ("{} {}".format(word, frequency))    