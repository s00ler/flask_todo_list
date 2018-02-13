from configparser import ConfigParser

config = ConfigParser()

config.read('./config.ini')

server_config = config['SERVER']
database_config = config['DATABASE']
mail_config = config['MAIL']
