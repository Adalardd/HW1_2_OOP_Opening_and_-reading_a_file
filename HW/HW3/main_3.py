import os

folder_path = os.path.abspath('.')
file_names = []
for file_name in os.listdir(folder_path):
    if os.path.isfile(os.path.join(folder_path, file_name)):
        if file_name.find('.txt') != -1 and file_name[0].isdigit():
            file_names.append(file_name)
print(file_names)

info_files = {}
for file in range(len(file_names)):
    with open(file_names[file], 'r') as f:
        lines = f.readlines()
        line_count = len(lines)
        f.seek(0)
        a = f.read()
        info_files[f.name] = [line_count, a]

sort_files = {}
for i in sorted(info_files.items(), key=lambda para: para[1][0]):
    sort_files[i[0]] = [i[1][0], i[1][1]]
print(sort_files)

for file in sort_files:
    with open(file, 'r') as fn, open('output.txt', 'a+') as f:
        fn.seek(0)
        a = fn.read()
        f.write(f'{file}\n{sort_files[file][0]}\n{a}\n')