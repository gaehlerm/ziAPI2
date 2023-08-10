from enum import Enum

class Sweeper():
	def __init__(self, daq, dev_id) -> None:
		self._daq = daq # + "sweeper" ?
		self._path = dev_id + "/sweeper/" # does this need the dev_id? It will be set on the next line
		self.set_device(dev_id)

    # What does this device do?
	def set_device(self, dev_id):
		self._daq.set(self._path + "device/", dev_id)

	# TODO this is not how it works... Which nodes do we have to sweep?
	# def sweep_frequency(self):
	# 	self._daq.set(self._path + "gridnode/",) # set the node path here... )

	def sweep_parameter(self, parameter):
		self._daq.set(self._path + "gridnode/", parameter.get_path())

	def set_start_value(self, value):
		self._daq.set(self._path + "start/", value)

	def set_stop_value(self, value):
		self._daq.set(self._path + "stop/", value)

	def set_samplecount(self, value):
		self._daq.set(self._path + "samplecount/", value)

	def set_scan_mode(self, enum_):
		self._daq.set(self._path + "scan/", enum_.value)
	
	class ScanMode(Enum):
		sequential = 0
		binary = 1
		bidirectional = 2
		reverse = 3

	def set_sequence_mode(self, enum_):
		self._daq.set(self._path + "xmapping/", enum_.value)

	class SequenceMode(Enum):
		linear = 0
		log = 1

	def set_max_bandwidth(self, value):
		self._daq.set(self._path + "maxbandwidth/", value)

