import os

path = os.getcwd()
files = os.listdir(path)
data = {}
for file in files:
    if(file.endswith('.txt')):
        with open(file, encoding='utf-8') as f:
            lines = f.readlines()
            data[file] = len(lines), lines
# print(data)
sorted_tuple = sorted(data.items(), key=lambda x: x[1])
# print(sorted_tuple)
for el in sorted_tuple:
    with open('united', 'a', encoding='utf-8') as f:
        f.write(str(el[0])+'\n')
        f.write(str(el[1][0])+'\n')
        f.write(str(el[1][1])+'\n')




