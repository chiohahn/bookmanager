from pathlib import Path
import os, re


'''
manga_info = {
    'round_brackets':[
        {open:위치 } close:위치}
        {open:위치, close:위치} 
        
    'squere_brackets':[
        {open:위치,close:위치}, 
        {open:위치, close:위치}
        ]
    'extension':zip or rzr
    'title':책이름
    '
}


manga = {
    ## key, value로 
    'author': [],
    'title': [],
    'edition': [],
    'circlename': '',
    'publiser':'',
    'date': '',
    'isbn':'',
    'path': ''
}

mangalist = []
'''


def get_square_brackes(filename):
    pattern = re.compile('(?<=\[)([^]]+)(?=\])')  
    items = re.finditer(pattern, filename)

    if items:
        for item in items:
            print('+',item.span(), item.group())

        return items
    return None
    
def get_round_brackes(filename):
    pattern = re.compile('(?<=\()([^)]+)(?=\))')
    items = re.finditer(pattern, filename)

    if items:
        for item in items:
            print('-',item.span(), item.group())
        return items
    return None

def get_titles(filename):
    title = ''
    if filename.startswith('[') | filename.startswith('('):
        pattern = re.compile('(?<=\])(.*?)(?<=\(|\[)')
        items = re.finditer(pattern, filename)
        
        for item in items:
            print(item.start(), item.end())
            print('*', item.span(), filename[item.start():item.end()-1])
            title = filename[item.start():item.end()-1]
    else:
        title = filename[:-4]
        print(title)
    
    return title


 

def make_booklist(work_dir):
    book_list = []

    for path, dirs, files in os.walk(work_dir):
        for filename in files:
            if filename.endswith('.zip') | filename.endswith('.rar'):
                get_round_brackes(filename)
                #get_square_brackes(filename)
                #get_titles(filename)
                
                '''
                if os.path.join(path, filename) != None:
                    book['path']    = os.path.join(path, filename)

                if book != None:
                    book_list.append(book)
                '''
                
    print('end')
    return book_list


def book_main():
    work_dir = 'C:\\Users\\gendo_3d0ywse\\Downloads'
    booklist= make_booklist(work_dir)
    
    for item in booklist:
        print(item)


if __name__ == "__main__":
    book_main()    