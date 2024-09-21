class WordsFinder:
    file_name = []
    punc = [',', '.', '=', '!', '?', ';', ':', ' - ']

    def __init__(self, *file_name):
        self.file_name = file_name

    def get_all_words(self, *args):
        all_words = {}
        words = []
        for file in self.file_name:
            with open(file, encoding='utf-8') as f:
                text = f.read()
                for char in self.punc:
                    text = text.replace(char, '')
                    words = text.lower().split()
            all_words[file] = words
        return all_words

    def find(self, word):
        dict = {}
        word = word.lower()
        for name, words in self.get_all_words().items():
            for i in range(len(words)):
                if words[i] == word:
                    dict.update({name: i + 1})
                    break
        return dict

    def count(self, word):
        dict = {}
        word = word.lower()

        for name, words in self.get_all_words().items():
            count = 0
            for i in words:
                if i == word:
                    count += 1
                dict.update({name: count})
            return dict


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
print(finder1.get_all_words())
print(finder1.find('captain'))
print(finder1.count('captain'))