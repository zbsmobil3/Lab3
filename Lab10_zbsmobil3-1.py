"""Word Count by Zach S. to analyze the number of times each word
appears in one of four given texts. No starter code was used. 10/4/26"""

from pathlib import Path
import string

class WordAnalyzer:
    """A class that does smth"""

    def __init__(self, filepath):
        """A func that sets up class vars"""
        self.path=Path(filepath)
        self.words_dict = {}

    def process_file(self):
        full_punc=string.punctuation+"“’”’‘—•"
        try:
            if self.path.exists():
                 self.path.open()
                 self.contents=self.path.read_text(encoding='utf-8')

        except (FileNotFoundError):
             print("File wasn't able to be found")
             return(False)
        else:
            lines= self.contents.splitlines()
            for line in lines:
                words=line.split()
                for word in words:
                    word=word.translate(str.maketrans("","", full_punc))
                    word=word.lower()
                    word=word.strip()
                    self.words_dict[word] = self.words_dict.get(word,0) + 1
    
            return(True)

    def print_report(self):
        a=self.words_dict
        a=dict(sorted(a.items()))
        for i in a:
            print(i,"\t::",a[i], end="\n")

def main():
    file_options={"1": "moby_dict", "2": "Tarzan", "3": "treasure_island", "4": "monte_cristo"}


book1= WordAnalyzer("princess_mars.txt")
result=book1.process_file()
if result:
    book1.print_report()