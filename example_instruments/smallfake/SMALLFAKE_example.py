from nexusbuilder import NexusBuilder
from detectorplotter import DetectorPlotter

if __name__ == '__main__':
    output_filename = 'SMALLFAKE_example_geometry.hdf5'
    # compress_type=32001 for BLOSC, or don't specify compress_type and opts to get non-compressed datasets
    builder = NexusBuilder(output_filename, idf_file='minimal_geometry.xml', compress_type='gzip', compress_opts=1)

    builder.add_instrument_geometry_from_idf()
    del builder

    plotter = DetectorPlotter(output_filename)
    plotter.plot_pixel_positions()
