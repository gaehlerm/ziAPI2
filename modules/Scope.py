from enum import Enum

class Scope():
	def __init__(self, daq, dev_id, n):
		self._daq = daq
		self._path = dev_id + "/scope/" + str(n) + "/"


	def enable_scope_channels(self, values):
		# Activates the scope channels.
		for value in values:
			self._daq.set(self._path + "channel", value)

	def enable_averaging_type(self, m, enum_):
		# Selects between sample decimation and sample averaging. Averaging avoids aliasing, but may conceal signal peaks.
		self._daq.set(self._path + "channel/" + str(m) + "/bwlimit", enum_.value)

	class AveragingType(Enum):
		sample_averaging = 0
		sample_decimation = 1

	def set_fullscale(self, m, value):
		# Indicates the full scale value of the scope channel.
		self._daq.set(self._path + "channel/" + str(m) + "/fullscale", value)

	def set_input_selection(self, m, enum_):
		# Selects the scope input signal.
		self._daq.set(self._path + "channel/" + str(m) + "/inputselect", enum_.value)

	#TODO enum_ p.353

	def set_lower_limit(self, m, value):
		# Lower limit of the scope full scale range. For demodulator, PID, Boxcar, and AU signals the limit should be adjusted so that the signal covers the specified range to achieve optimal resolution.
		self._daq.set(self._path + "channel/" + str(m) + "/limitlower", value)

	def set_upper_limit(self, m, value):
		# Upper limit of the scope full scale range. For demodulator, PID, Boxcar, and AU signals the limit should be adjusted so that the signal covers the specified range to achieve optimal resolution.
		self._daq.set(self._path + "channel/" + str(m) + "/limitupper", value)
	
	def set_offset(self, m, value):
		# Indicates the offset value of the scope channel.
		self._daq.set(self._path + "channel/" + str(m) + "/offset", value)

	def enable_scope(self, ):
		# Enables the acquisition of scope shots
		self._daq.set(self._path + "enable", 0)

	def disable_scope(self, ):
		# Disables the acquisition of scope shots
		self._daq.set(self._path + "enable", 1)

	def set_scope_shot_length(self, value):
		# Defines the length of the recorded Scope shot in number of samples.
		self._daq.set(self._path + "enable", value)

	def set_segments_count(self, value):
		# Specifies the number of segments to be recorded in device memory. The maximum scope shot size is given by the available memory divided by the number of segments. This functionality requires the DIG option.
		self._daq.set(self._path + "segments/count", value)

	def enable_segments(self, ):
		# Enable segmented scope recording. This allows for full bandwidth recording of scope shots with a minimum dead time between individual shots. This functionality requires the DIG option.
		self._daq.set(self._path + "segments/enable", 0)

	def disable_segments(self, ):
		# Disable segmented scope recording.
		self._daq.set(self._path + "segments/enable", 1)

	def enable_single_shot_mode(self, ):
		# Puts the Scope into single shot mode
		self._daq.set(self._path + "segments/single", 0)

	def disable_single_shot_mode(self, ):
		# Puts the Scope into continuous mode
		self._daq.set(self._path + "segments/single", 1)

	def enable_streaming_for_channel(self, m):
		# Enable scope streaming for the specified channel. This allows for continuous recording of scope data on the plotter and streaming to disk. Note: scope streaming requires the DIG option.
		self._daq.set(self._path + "stream/enables/" + str(m), 0)

	def disable_streaming_for_channel(self, m):
		# Disable scope streaming for the specified channel.
		self._daq.set(self._path + "stream/enables/" + str(m), 1)

	def set_streaming_rate(self, enum_):
		# Streaming Rate of the scope channels. The streaming rate can be adjusted independent from the scope sampling rate. The maximum rate depends on the interface used for transfer. Note: scope streaming requires the DIG option.
		self._daq.set(self._path + "stream/rate", enum_.value)

	#TODO define the enum_

	def get_streaming_sample(self, ):
		# Stream the scope sample data.
		return self._daq.get(self._path + "stream/sample")
