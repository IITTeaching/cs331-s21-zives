import urllib
import requests

def book_to_words(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    booktxt = urllib.request.urlopen(book_url).read().decode()
    bookascii = booktxt.encode('ascii','replace')
    return bookascii.split()

def radix_a_book(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    wordunsorted = book_to_words(book_url)
    words = []
    maxlen = max(len(x) for x in wordunsorted)
    for i in wordunsorted:
        words.append([i])
    for x in range(maxlen, -1, -1):
        words = sortonpos(words,x)
    wordsorted = []
    for x in words:
        for y in x:
            wordsorted.append(y)
    return wordsorted
    
def sortonpos(l : list, pos : int):
    new = [[] for _ in range(130)]
    for i in l:
        for j in i:
            try:
                new[j[pos]+1].append(j)
            except:
                new[0].append(j)
    return new

def main():
    urls = ['https://www.gutenberg.org/files/1257/1257-0.txt',
    'https://www.gutenberg.org/files/2701/2701-0.txt',
    'https://www.gutenberg.org/files/2591/2591-0.txt',
    'https://www.gutenberg.org/cache/epub/12242/pg12242.txt',
    'https://www.gutenberg.org/files/108/108-0.txt',
    'https://www.gutenberg.org/cache/epub/128/pg128.txt',
    'https://www.gutenberg.org/cache/epub/31/pg31.txt',
    ]
    for x in urls:
        print(80 * "*" + "\n" + x)
        assert (sorted(book_to_words(x)) == radix_a_book(x))
        print("SUCCESS")
    print('All tests succeeded')

if __name__ == '__main__':
    main()