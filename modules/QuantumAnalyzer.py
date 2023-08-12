from enum import Enum

class Save():
	# TODO Is this code redundant?
	def __init__(self, daq, path) -> None:
		self._daq = daq
		self._path = path + "/save/"

	class CSVLocale(Enum):
		# TODO figure out how this works
		comma = "C"
		use_region_settings = " "

	def set_CSV_locale(self, enum_):
		self._daq.set(self._path + "csvlocale", enum_.value)

	def set_CSV_separator(self, value):
		self._daq.set(self._path + "csvseparator", value)

	def set_directory(self, value):
		self._daq.set(self._path + "directory")

	class FileFormat(Enum):
		matlab = 0
		csv = 1
		zview = 2
		sxm = 3
		hdf5 = 4

	def set_file_format(self, enum_):
		self._daq.set(self._path + "fileformat", enum_.value)

	def set_file_name(self, value):
		self._daq.set(self._path + "filename", value)

	def save(self):
		# TODO wait for the node to be 0 again?
		self._daq.set(self._path + "save", 1)

	def enable_save_on_read(self):
		self._daq.set(self._path + "saveonread", 1)
		
	def disable_save_on_read(self):
		self._daq.set(self._path + "saveonread", 0)


class QuantumAnalyzer():
	def __init__(self, daq, dev_id) -> None:
		self._daq = daq
		self._path = dev_id

		self.save = Save(self._daq, self._path)

	def clear_history(self):
		self._daq.set(self._path + "clearhistory", 1)

	def set_history_length(self, value):
		self._daq.set(self._path + "historylength", value)

	def set_rotation(self, value):
		self._daq.set(self._path + "rotation", value)

	def scaling_I(self, value):
		self._daq.set(self._path + "scalingi", value)

	def scaling_Q(self, value):
		self._daq.set(self._path + "scalingq", value)

	def shift_I(self, value):
		self._daq.set(self._path + "shifti", value)

	def shift_Q(self, value):
		self._daq.set(self._path + "shiftq", value)