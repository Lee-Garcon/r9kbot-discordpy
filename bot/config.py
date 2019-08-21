def config_get():
    file_path = '../.config'
    with open(file_path) as f:
        contents = f.read()

    return parse(contents)

def parse(contents):
    lines = contents.split('\n')
    dic = {}
    for line in lines:
        if ':' in line:
            splice = line.split(':')
            v = splice[0]
            dic[splice[0]] = ':'.join(splice[1:])

    return dic
