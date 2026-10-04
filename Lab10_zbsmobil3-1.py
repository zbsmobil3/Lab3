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
    choice="67 xD"
    while choice != "5":
        choice="67 xD"
        file_options={"1": "princess_mars", "2": "Tarzan", "3": "treasure_island", "4": "monte_cristo"}
        print()
        print("--- Word Analyzer ---")
        print()
        for i in file_options:
            print(f"{i}. {file_options[i]}")
        print("5. Exit")
        while not(choice=="0" or choice=="1" or choice=="2" or choice=="3" or choice == "4" or choice == "5"):
            choice=input("Enter your choice (1-5): ")
            if not(choice=="0" or choice=="1" or choice=="2" or choice=="3" or choice == "4" or choice == "5"):
                print("Invalid input. Try again")
        print()
        if choice != "5":
            print(f"Processing '{file_options[choice]}.txt'...")
            print()
            book=WordAnalyzer(file_options[choice]+".txt")
            result=book.process_file()
            if result:
                pass
                book.print_report()
                input("Press Enter to Return to the Menu ")
            else:
                print("Analysis failed")
        else:
            pass
    print("Goodbye!")
    print()


main()
#book1= WordAnalyzer("princess_mars.txt")
#result=book1.process_file()
#if result:
#book1.print_report()