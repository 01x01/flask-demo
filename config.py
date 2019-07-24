# coding: utf-8 
import os 


class Config(object):
    SECRET_KEY = os.getenv('SECRET_KEY')


class DevConfig(Config):
    pass


config = {
    "dev":DevConfig,
}