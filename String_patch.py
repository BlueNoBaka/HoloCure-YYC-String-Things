import json

path_org = r'strings.json' # string exported
path_patch = r'strings_trim.json'   # trimmed string
# can also be useful when the game updates, just load localized strings.json of the previous version

path_out = r'strings_patched.json'
path_log = r'log_miss.json' # unapplied changes due to can't find the same original string in exported strings
path_warning = r'log_warning.json'  # localized texts longer than oringal ones

with open(path_patch, 'r', encoding='UTF-8-sig') as patch:
    patch_list = json.load(patch)
    text_dict = {}
    for text in patch_list:
        if text['ORG'] != text['CHS']:
            text_dict.update({text['ORG']:text['CHS']})

    for key in text_dict:
        if key == text_dict[key]:
            text_dict.pop(key)


with open(path_org, 'r', encoding='UTF-8') as org:
    string=json.load(org)
    count = 0
    log_warning = []
    for i in range(len(string)):
        if string[i]['ORG'] in text_dict:
            #org_list[i] = text_dict[org_list[i]]
            string[i]['CHS'] = text_dict.pop(string[i]['ORG'])
            count = count + 1
        
        len_org = len(string[i]['ORG'].encode('UTF-8'))
        if len(string[i]['CHS'].encode('UTF-8')) + 1 > len_org + 4 - (len_org + 1) % 4:
            log_warning.append(string[i])
            # all strings are at least 4 bytes aligned, so I just take 4 here
            # localized text might just fit in if it's a little bit longer
            # if it's too long, the following string will overwrite the longer part

    print('%d / %d changes applied'%(count,len(text_dict)+count))

if len(log_warning) >0:
    print('%d changes might be too long, logged in %s'%(len(log_warning), path_warning))
    with open(path_warning, 'w+', encoding='UTF-8') as out:
        json.dump(log_warning, out, ensure_ascii=False, indent=4)

if len(text_dict) > 0:
    print('%d changes failed to be applied, logged in %s'%(len(text_dict), path_log))
    with open(path_log, 'w+', encoding='UTF-8') as out:
        json.dump(text_dict, out, ensure_ascii=False, indent=4)

with open(path_out, 'w+', encoding='UTF-8') as out:
    json.dump(string, out, ensure_ascii=False, indent=4)
