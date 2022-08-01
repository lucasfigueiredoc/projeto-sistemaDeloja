
from configparser import ConfigParser

def config(filename='database.ini', section='postgresql'):
    parser = ConfigParser()
    parser.read(filename)
    
    db = {}
    if parser.has_secction(section):
        params = parser.items(section)
        for param in params :
            db[param[0]] = param [1]
    
    else:
        raise Exception('Section {0} não esta no {1} arquivo'.format(section, filename))
    
    return db