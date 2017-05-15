from collections import OrderedDict
from nexusbuilder import NexusBuilder

if __name__ == '__main__':
    copy_l_to_r = \
        OrderedDict([('/raw_data_1/good_frames', '/raw_data_1/good_frames'),
                     ('raw_data_1/instrument', 'raw_data_1/instrument'),
                     ('raw_data_1/instrument/name', 'raw_data_1/instrument/name'),
                     ('raw_data_1/instrument/source', 'raw_data_1/instrument/source'),
                     ('raw_data_1/instrument/source/name', 'raw_data_1/instrument/source/name'),
                     ('raw_data_1/instrument/source/probe', 'raw_data_1/instrument/source/probe'),
                     ('raw_data_1/instrument/source/type', 'raw_data_1/instrument/source/type'),
                     ('raw_data_1/instrument/moderator', 'raw_data_1/instrument/moderator'),
                     ('raw_data_1/instrument/moderator/distance', 'raw_data_1/instrument/moderator/distance'),
                     ])

    builder = NexusBuilder('SANS_test.nxs', 'SANS_example_noComp.hdf5', idf_filename='SANS2D_Definition.xml')
    # builder = NexusBuilder('SANS_test.nxs', 'SANS_example_gzip.hdf5', compress_type='gzip', compress_opts=1)
    # builder = NexusBuilder('SANS_test.nxs', 'SANS_example_blosc.hdf5', compress_type=32001)
    builder.copy_items(copy_l_to_r)
    builder.add_user('Sans2d Team', 'ISIS, STFC')
    builder.add_detector_banks_from_idf()
    copy_l_to_r = \
        OrderedDict([('/raw_data_1/detector_1_events', '/raw_data_1/instrument/detector_2/events'),
                     ('/raw_data_1/detector_1_events/event_id', '/raw_data_1/instrument/detector_2/events/event_id'),
                     ('/raw_data_1/detector_1_events/total_counts',
                      '/raw_data_1/instrument/detector_2/events/total_counts'),
                     ('/raw_data_1/detector_1_events/event_index',
                      '/raw_data_1/instrument/detector_2/events/event_index'),
                     ('/raw_data_1/detector_1_events/event_time_zero',
                      '/raw_data_1/instrument/detector_2/events/event_time_zero'),
                     ('/raw_data_1/detector_1_events/event_time_offset',
                      '/raw_data_1/instrument/detector_2/events/event_time_offset'),
                     ])
    builder.copy_items(copy_l_to_r)
