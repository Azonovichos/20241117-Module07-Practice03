# Module 7 Practice 3

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                words = []
                for line in file:
                    line = line.lower()
                    line = ''.join(e for e in line if e.isalnum() or e.isspace())
                    words.extend(line.split())
                all_words[file_name] = words
        return all_words

    def find(self, word):
        result = {}
        for name, words in self.get_all_words().items():
            if word.lower() in [w.lower() for w in words]:
                result[name] = words.index(word.lower()) + 1
        return result

    def count(self, word):
        all_words = self.get_all_words()
        result = {}
        for file_name, words in all_words.items():
            result[file_name] = words.count(word.lower())
        return result


finder = WordsFinder('test_file.txt')
print(finder.get_all_words())  # All words
print(finder.find('TEXT'))  # Position of 'TEXT'
print(finder.count('teXT'))  # Count of 'teXT'

#Test yourself
print('\nTest yourself')

#Mother Goose - Monday’s Child
print('\nMother Goose - Monday’s Child')
finder = WordsFinder('Mother_Goose_-_Monday`s_Child.txt')
print(finder.get_all_words())  # All words
print(finder.find('Child'))  # Position of 'Child'
print(finder.count('Mother'))  # Count of 'Mother'

#Rudyard Kipling - If
print('\nRudyard Kipling - If')
finder = WordsFinder('Rudyard_Kipling_-_If.txt')
print(finder.get_all_words())  # All words
print(finder.find('If'))  # Position of 'If'
print(finder.count('my'))  # Count of 'my'

#Walt Whitman - O Captain! My Captain!
print('\nWalt Whitman - O Captain! My Captain!')
finder = WordsFinder('Walt_Whitman_-_O_Captain!_My_Captain.txt')
print(finder.get_all_words())  # All words
print(finder.find('Captain'))  # Position of 'Captain'
print(finder.count('fearful'))  # Count of 'fearful'
