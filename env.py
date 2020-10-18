import os


def get_env(var_name, filePath=None, stripSpace=True):
    if filePath:
        ret = __get_var(var_name, filePath, stripSpace)
    else:
        if os.path.isfile('./.env'):
            ret = __get_var(var_name, './.env', stripSpace)
        elif os.path.isfile('./.ini'):
            ret = __get_var(var_name, './.ini', stripSpace)
        else:
            for f in os.listdir('./'):
                if f.endswith('.ini') or f.endswith('.env'):
                    ret = __get_var(var_name, f, stripSpace)
    return ret


def __get_var(var_name, filePath, stripSpace=True):
    with open(filePath, 'r') as f:
        for line in f.readlines():
            if line.startswith(var_name):
                index = line.find('=')
                if index < 1:
                    continue
                value = line[index+1: len(line) - 1]
                value = value.strip(' ' if stripSpace else '')
                if value.lower() == 'true':
                    return True
                elif value.lower() == 'false':
                    return False
                else:
                    return value
        return None
