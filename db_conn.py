'''
Connector to database postgresql
'''

from configparser import ConfigParser
import psycopg2
from psycopg2 import connect
from psycopg2.extras import DictConnection

class dbConnection:
    def __init__(self, filename='database.ini', section='postgresql'):
        self.parser = ConfigParser()
        self.parser.read(filename)
        self.db = {}
        
        if self.parser.has_section(section):
            self.params = self.parser.items(section)
            for param in self.params:
                self.db[param[0]] = param[1]
            print(self.db)
        else:
            raise Exception (f"Section {section} doesn't exist in file {filnename}")
    def connect(self):
        self.conn = None
        try:
            self.conn = 