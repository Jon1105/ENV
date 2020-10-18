import os


def get_env(var_name, filePath=None):
    if filePath:
        ret = __get_var(var_name, filePath)
    else:
        if os.path.isfile('./.env'):
            ret = __get_var(var_name, './.env')
        elif os.path.isfile('./.ini'):
            ret = __get_var(var_name, './.ini')
        else:
            for f in os.listdir('./'):
                if f.endswith('.ini') or f.endswith('.env'):
                    ret = __get_var(var_name, f)
    return ret


def __get_var(var_name, filePath):
    with open(filePath, 'r') as f:
        for line in f.readlines():
            if var_name in line:
                index = line.find('=')
                if index < 1:
                    continue
                value = line[index+1: len(line) - 1]
                if value.strip().lower() == 'true':
                    return True
                elif value.strip().lower() == 'false':
                    return False
                else:
                    return value
        return None
