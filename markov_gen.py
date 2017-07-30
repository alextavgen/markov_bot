from db import Db
from gen import Generator
from parse import Parser
from sql import Sql
from rnd import Rnd
import sys
import sqlite3
import codecs

SENTENCE_SEPARATOR = '.'
WORD_SEPARATOR = ' '
def generate(number, name):
  count = number
  db = Db(sqlite3.connect(name + '.db'), Sql())
  generator = Generator(name, db, Rnd())
  for i in range(0, count):
    yield generator.generate(WORD_SEPARATOR)