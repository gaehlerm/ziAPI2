

class Exponentials():
    def __init__(self, daq, path, i) -> None:
        self._daq = daq
        self._path = path + "/exponentials/" + str(i)

    def enable(self):
        # TODO?
        self._daq.set(self._path + "/enable", 1)


class Input():
    def __init__(self, daq, path) -> None:
        self._daq = daq
        self._path = path + "input/"

    def set_source(self, value):
        self._daq.set(self._path + "source", value)


class Wave():
    def __init__(self, daq, path) -> None:
        self._daq = daq
        self._path = path + "/wave/"
        
        self.input = Input(self._daq, self._path)

class Precompensation():
	def __init__(self, daq, dev_id) -> None:
		self._daq = daq
		self._path = dev_id
		self.exponentials = [Exponentials(self._daq, self._path, i) for i in range(4)] # TODO?
		self.wave = Wave(self._daq, self._path)
    
	def get_sampling_rate(self):
		self._daq.get(self._path + "/samplingfreq") # TODO which value to return here?

