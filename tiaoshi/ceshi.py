from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import re
import requests

def search4letters(phrase:str, letters:str) -> set:
    """给定一个检查对象和一个词语，查出在该词语中也在检查对象中的字母"""
    return set(phrase).intersection(set(letters))

if __name__ == '__main__':
    letters = 'aabdef'
    phrase = 'abbeigasada'
    print(search4letters(phrase,letters))