import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-not-guess-this-shit'
    AT_USERNAME = "njugunamadeit"
    AT_API_KEY = "3e02f2b037e629702337fb82e9cf1b3cf7d743d6cf79cda58cecedc30b186474"
    PRODUCT_NAME = "data_test"

class SafaricomPrefix():
    SAFARICOM_NUMBERS = [
    '0701',
    '0702',
    '0703',
    '0704',
    '0705',
    '0706',
    '0707',
    '0708',
    '0709',
    '0710',
    '0711',
    '0712',
    '0713',
    '0714',
    '0715',
    '0716',
    '0717',
    '0718',
    '0719',
    '0720',
    '0721',
    '0722',
    '0723',
    '0724',
    '0725',
    '0726',
    '0727',
    '0728',
    '0729',
    '0740',
    '0741',
    '0742',
    '0743',
    '0744',
    '0745',
    '0746',
    '0747',
    '0748'
]