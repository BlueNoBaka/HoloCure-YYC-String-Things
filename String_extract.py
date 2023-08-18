import json

path_exe = r'D:\SteamLibrary\steamapps\common\HoloCure\HoloCure.exe'
path_out = r'strings.json'
string_head = 'gml_Script_input_binding_gamepad_button'.encode(encoding='UTF-8')    # first useful string in exe here
string_end = 'invalid type for %s lhs=%s '.encode(encoding='UTF-8') # last useful string in exe here

with open(path_exe, 'rb') as source_file:
    contents = source_file.read()
    start_string = 0

    # looking for the offset of string section
    start_string = contents.find(string_head, start_string)
    end_string = contents.find(string_end, start_string)
    # print('%x %x'%(start_string, end_string))
    
    source_file.seek(start_string,0)
    strings = source_file.read(end_string - start_string)

    ptr = 0
    string_list= [] # list of string_dict

    while ptr>=0:
        string_dict= {} # 'offset':'0x##', 'ORG':'Original String', 'CHS':'Copy of ORG, edit for translation'
        string_org = ''
        string_end = strings.find(b'\x00', ptr)
        if string_end < ptr:
            # strings.find won't return -1
            # it just wraps around
            break

        try:
            string_org = strings[ptr: string_end].decode(encoding='UTF-8')
        except:
            # skip non-UTF8 data
            ptr = string_end + 1
            continue

        if len(string_org)>0:
            string_dict['offset'] = hex(start_string + ptr) # offset in exe
            string_dict['ORG'] = strings[ptr: string_end].decode(encoding='UTF-8')
            string_dict['CHS'] = string_dict['ORG']
            string_list.append(string_dict)
            #print(string_dict)
        ptr = string_end + 1

    with open(path_out, 'w+', encoding='UTF-8') as out:
        json.dump(string_list, out, ensure_ascii=False, indent=4)
