import json

path_chs = r'strings_patched.json'
path_exe = r'D:\SteamLibrary\steamapps\common\HoloCure\HoloCure.exe'

with open(path_chs, 'r', encoding='UTF-8') as chs:
    string=json.load(chs)

with open(path_exe, 'r+b') as source_file:
    for elem in string:
        source_file.seek(int(elem['offset'],16), 0)
        source_file.write(elem['CHS'].encode(encoding='UTF-8'))
        source_file.write(b'\x00')            

