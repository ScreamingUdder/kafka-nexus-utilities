import env
import pytest
import numpy as np
from io import StringIO
from idfparser import IDFParser


def get_fake_idf_file(instrument_name='TEST', source_name=None, sample=None):
    fake_idf_file = StringIO()

    # instrument
    fake_idf_file.write('<?xml version="1.0" encoding="UTF-8"?>\n'
                        '<instrument xmlns="http://www.mantidproject.org/IDF/1.0" '
                        'name="' + instrument_name + '">\n')

    # source
    if source_name is not None:
        fake_idf_file.write('<type name="' + source_name + '" is="Source"></type>\n')
        fake_idf_file.write('<component type="' + source_name + '"><location z="-40.0"/></component>\n')

    if sample is not None:
        fake_idf_file.write(
            '<component type="' + sample['name'] + '"><location x="' + str(sample['position'][0]) + '" y="' + str(
                sample['position'][1]) + '" z="' + str(sample['position'][2]) + '"/></component>')
        fake_idf_file.write('<type name="' + sample['name'] + '" is="SamplePos"/>')

    fake_idf_file.write('</instrument>\n')
    fake_idf_file.seek(0)  # So that the xml parser reads from the start of the file
    return fake_idf_file


def test_get_instrument_name():
    instrument_name = 'TEST_NAME'
    fake_idf_file = get_fake_idf_file(instrument_name)
    parser = IDFParser(fake_idf_file)
    assert parser.get_instrument_name() == instrument_name
    fake_idf_file.close()


def test_get_source_name():
    name = 'TEST_SOURCE'
    fake_idf_file = get_fake_idf_file(source_name=name)
    parser = IDFParser(fake_idf_file)
    assert parser.get_source_name() == name
    fake_idf_file.close()


def test_get_sample_position():
    test_sample = {'name': 'TEST_SAMPLE',
                   'position': [-0.54, 42.0, 0.48]}
    fake_idf_file = get_fake_idf_file(sample=test_sample)
    parser = IDFParser(fake_idf_file)
    np.testing.assert_allclose(parser.get_sample_position(), test_sample['position'])
    fake_idf_file.close()
