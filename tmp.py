import chardet

with open('/Users/oyg/.defog/connection.json', 'rb') as rawdata:
    result = chardet.detect(rawdata.read(10000))

# check what the character encoding might be
print(result)


# File_path, Encoding_Type -> Change Files encoding type
def to_utf8(file_path: str, encoding_in: str):
    try:
        with open(file_path, 'r', encoding=encoding_in) as f:
            datas = f.read()

        with open(file_path, 'w', encoding='utf-8') as k:
            k.write(datas)
    except:
        print('변환 실패')

to_utf8('/Users/oyg/.defog/connection.json', 'UTF-8')