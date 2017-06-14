import env
import pytest
from io import StringIO
from idfparser import IDFParser


def test_get_instrument_name():
    instrument_name = 'TEST'
    fake_idf_file = StringIO('<?xml version="1.0" encoding="UTF-8"?>\n'
                             '<instrument xmlns="http://www.mantidproject.org/IDF/1.0"\n'
                             'name="' + instrument_name + '">\n'
                                                          '</instrument>')
    parser = IDFParser(fake_idf_file)
    assert parser.get_instrument_name() == instrument_name
