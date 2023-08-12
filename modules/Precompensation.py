from enum import Enum

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

class Bounces():
	def __init__(self, daq, path, n) -> None:
		self._daq = daq
		self._path = path + "/bounces/" + str(n) + "/"
                
	def set_filter_amplitude(self, value):
		self._daq.set(self._path + "amplitude", value)
                
	def set_delay(self, value):
		self._daq.set(self._path + "delay", value)
                
	def enable_bounce_filter(self):
		self._daq.set(self._path + "enable", 1)
    
	def disable_bounce_filter(self):
		self._daq.set(self._path + "enable", 0)

class Exponentials():
	def __init__(self, daq, dev_id, n) -> None:
		self._daq = daq
		self._path = f"{dev_id}/exponentials/{n}/"

	def set_amplitude(self, value):
		self._daq.set(self._path + "amplitude", value)

	def enable_filter(self):
		self._daq.set(self._path + "enable", 1)

	def disable_filter(self):
		self._daq.set(self._path + "enable", 0)

	def set_time_constant(self, value):
		self._daq.set(self._path + "timeconstant", value)


class Highpass():
	def __init__(self, daq, dev_id, n) -> None:
		self._daq = daq
		self._path = f"{dev_id}/highpass/{n}/"

	def enable(self):
		self._daq.set(self._path + "enable", 1)
		
	def disable(self):
		self._daq.set(self._path + "enable", 0)

	def set_time_constant(self, value):
		self._daq.set(self._path + "timeconstant")

class Input():
	def __init__(self, daq, path) -> None:
		self._daq = daq
		self._path = f"{path}input/"

	def set_awg_index(self, value):
		self._daq.set(self._path + "awgindex", value)

	def set_delay(self, value):
		self._daq.set(self._path + "delay", value)

	def set_gain(self, value):
		self._daq.set(self._path + "gain", value)

	def set_input_vector(self, value):
		# TODO how to deal with ZIVectorData?
		self._daq.set(self._path + "inputvector", value)

	def set_length(self, value):
		self._daq.set(self._path + "length", value)

	def set_offset(self, value):
		self._daq.set(self._path + "offset", value)

	def set_sampling_frequency(self, value):
		self._daq.set(self._path + "samplingfreq", value)

	class Source(Enum):
		step = 0
		impulse = 1
		nodes = 2
		manual = 3

	def set_source(self, enum_):
		self._daq.set(self._path + "source", enum_.value)

	def get_status(self):
		return self._daq.set(self._path + "statusstring")
	
	def set_waveindex(self, value):
		self._daq.set(self._path + "waveindex", value)


class Output():
	def __init__(self, daq, path) -> None:
		self._daq = daq
		self._path = f"{path}output/"

	def get_backwardwave(self):
		return self._daq.get(self._path + "backwardwave")
	
	def get_forwardwave(self):
		return self._daq.get(self._path + "forwardwave")
	
	def get_initialwave(self):
		return self._daq.get(self._path + "initialwave")


class Wave():
	def __init__(self, daq, dev_id) -> None:
		self._daq = daq
		self._path = f"{dev_id}/wave/"



class Precompensation():
	def __init__(self, daq, dev_id) -> None:
		self._daq = daq
		self._path = dev_id
		self.exponentials = [Exponentials(self._daq, self._path, i) for i in range(8)]
		self.wave = Wave(self._daq, self._path)
        # TODO number of bounces and highpass?
		self.bounces = [Bounces(self._daq, self._path, i) for i in range(4)]
		self.bounces = [Highpass(self._daq, self._path, i) for i in range(4)]
		self.input = Input(self, daq, dev_id)
		self.input = Output(self, daq, dev_id)
    
	def set_FIR_coefficients(self, value):
		# TODO how to set ZiVectorData? Use set_vector?
		self._daq.set(self._path + "fir/coefficients", value)

	def enable_fir(self):
		self._daq.set(self._path + "fir/enable", 1)

	def disable_fir(self):
		self._daq.set(self._path + "fir/enable", 0)

	def enable_highpass(self):
		self._daq.set(self._path + "highpass/enable")
	
	def enable_latency_simulation(self):
		self._daq.set(self._path + "latency/enable", 1)

	def disable_latency_simulation(self):
		self._daq.set(self._path + "latency/enable", 0)

	def get_latency(self):
		return self._daq.get(self._path + "latency/value")

	def get_sampling_frequency(self):
		return self._daq.get(self._path + "samplingfreq")
	



	def get_sampling_rate(self):
		self._daq.get(self._path + "/samplingfreq") # TODO which value to return here?


