# python-nexus-utilities
Functions to assist with building example NeXus files in the proposed format for ESS from existing NeXus files and Mantid IDFs.

Tested with Python 3.6, >=3.4 should be fine. You can install dependencies with
```
pip install -r requirements.txt
```
and then the nexusutils package with
```
pip install -e /path/to/python-nexus-utils
```
replacing the path with the path to your local working tree for this repository.

To display the plots generated by `DetectorPlotter` you may need to install tk libraries, on Ubuntu for example:
```
sudo apt install python3-tk
```
on CentOS (with EPEL installed):
```
sudo yum install python34-tkinter
```

## To create a NeXus file

Use `python nexusutils/build.py <input_IDF_file_path>`.

To view a list of optional arguments use `./build.py --help` 

## Examples

`NexusBuilder` has functionality beyond that which is exposed by `build.py`.
Examples scripts can be found in the `examples` directory. Example scripts should be run from their own directory with the root directory of the repository in `PYTHONPATH` (IDEs such as PyCharm do this by default).

- `SANS2D_example.py` example using a NeXus file and Mantid instrument definition from the SANS2D instrument. This outputs a new NeXus file in the proposed new format and contains examples of using the proposed `NXsolid_geometry` group to describe pixel shape.

- `WISH_example` geometry example using a Mantid IDF for the WISH instrument. This demonstrates conversion from a polar coordinates system and more complex geometry with many (10 panels x 152 tubes x 512 pixels) detector pixels.

- `LOKI_example.py` geometry example using a Mantid IDF for the LOKI instrument. It contains an example of using an `NXsolid_geometry` group to describe the shape of entire detector panels. 

- `SANS2D_NXlog_example.py` demonstrates how one can use the `cue` datasets in the new `NXevent_data` group or in the updated `NXlog` to extract data for a specific time period from the file.

- `all/` contains all current IDFs from Mantid. Running `parse_all.py` will attempt to convert all of these to the NeXus format. This is intended to help discover where the parser currently fails.

- `SMALLFAKE_example` creates a small (~35 kB) NeXus file for a fake instrument with a few tube detectors.

## Tools

To assist in creating the IDF to NeXus conversion scripts there are a couple of simple tools: "Detector Plotter" and "HDF5 Size Profiler". 

### Detector Plotter

Plots the pixel offsets in the XY and XZ planes.

Usage example:
```python
from nexusutils.detectorplotter import DetectorPlotter
plotter = DetectorPlotter('example_instruments/wish/WISH_example_gzip_compress.hdf5')
plotter.plot_pixel_positions()
```
example output:

![WISH](examples/wish/wish_plot.png)

### HDF5 Size Profiler

Prints a table of datasets (ignoring links) from largest to smallest with details of data type, number of elements etc. Can also output a pie chart of dataset sizes.

Usage example:
```python
from nexusutils.hdf5sizeprofiler import HDF5SizeProfiler
profiler = HDF5SizeProfiler('example_instruments/wish/WISH_example_gzip_compress.hdf5')
profiler.print_stats_table()
profiler.draw_pie_chart()
```
example table output (truncated):
```
Total uncompressed size is 4.981903 megabytes, compressed file size is 1.332304 megabytes
  Size (elements)    % of total size  Datatype      Size (bytes)  Dataset name
-----------------  -----------------  ----------  --------------  -------------------------------------------------------
            77824       12.4971       float64             622592  raw_data_1/instrument/detector_1/x_pixel_offset
            77824       12.4971       float64             622592  raw_data_1/instrument/detector_1/y_pixel_offset
            77824       12.4971       float64             622592  raw_data_1/instrument/detector_1/z_pixel_offset
            77824        6.24854      int32               311296  raw_data_1/instrument/detector_1/detector_number
            77824        6.24854      int32               311296  raw_data_1/instrument/detector_10/detector_number
...
```

## Tests

Unit tests require pytest (`pip install pytest`) can be run with
```
pytest
```

An html test coverage report can be generated using pytest-cov (`pip  install pytest-cov`): 
```
pytest --cov-config .coveragerc --cov-report html --cov=. tests/
```
