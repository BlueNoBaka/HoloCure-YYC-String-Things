import json

path_chs = r'strings_trim.json'
path_var = r'vars.txt'

with open(path_chs, 'r', encoding='UTF-8') as chs:
    string=json.load(chs)

with open(path_var, 'r', encoding='UTF-8') as f:
    var_list=f.read().replace("\"","").splitlines()
    var_list=set(var_list)

    string_out = []
    for elem in string:
        if elem['ORG'] not in var_list:
            if 'GlobalScript' not in elem['ORG']:
                if 'gml_Object_' not in elem['ORG']:
                    if '___struct___' not in elem['ORG']:
                       string_out.append(elem)

with open(r'strings_trim.json', 'w+', encoding='UTF-8') as out:
    json.dump(string_out, out, ensure_ascii=False, indent=4)