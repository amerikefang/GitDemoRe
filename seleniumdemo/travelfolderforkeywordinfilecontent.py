import os

def find_file(keywords,path):
    file_list = get_all_file(path)
    count = 0
    for file in file_list:
        if file.endswith('.py') or file.endswith('.txt'):
            with open(file,'r',encoding='utf-8') as fr:
                if keywords in fr.read():
                    print(file)
                    count+=1
                    print('=='*20)
    print('Total of matched files is: ',count)

def get_all_file(path):
    file_list = []
    for cur_path, cur_dirs, cur_files in os.walk(path):
        for name in cur_files:
            file_list.append(os.path.join(cur_path,name))
    return file_list
#keywords = input("Please input the key words that you want to search:")
#path = input("Please input the filepath:")
find_file('Qstring','F:\\testpython')