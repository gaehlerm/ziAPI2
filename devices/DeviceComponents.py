from enum import Enum

class Save():
	def __init__(self, daq):
		self._daq = daq

	def set_fileformat(self, FileFormat):
		self._daq.set("save/fileformat", FileFormat.value())

	class FileFormat(Enum):
		matlab = 0
		csv = 1
		zview = 2
		sxm = 3
		hdf5 = 4


class System():
	def __init__(self, daq, dev_id):
		self._daq = daq
		self._path = dev_id + "/system/properties"

		self.clock = Clock(self._daq, self._path)

	def get_timebase(self):
		return self._daq.get(self._path + "/timebase")
	
	def set_software_trigger(self):
		self._daq.set(self._path + "/swtriggers/0/single", 1)

	def load_preset(self):
		self._daq.set(self._path + "/preset/load", 1)

	def wait_for_state_change(self, value, timeout):
		# TODO add a sync before the set?
		# TODO how does this node work exactly?
		self._daq.set(self._path + "/preset/busy", 1)
		

class Clock():
	def __init__(self, daq, path) -> None:
		self._daq = daq
		self._path = path + "/clocks"

	def set_sampling_rate(self, value):
		self._daq.set(self._path + "/sampleclock/freq", value)


class Status():
	def __init__(self, daq, dev_id):
		self._daq = daq
		self._path = dev_id + "/status"

	def get_current_timestamp(self):
		return self._daq.get(self._path + "/time")


class AuxIn():
	def __init__(self, daq, dev_id, n):
		self._daq = daq
		self._path = dev_id + "/auxins/" + str(n) + "/"

	def set_averaging(self,averaging_mode):
		if averaging_mode >= 16:
			raise Exception("averaging mode cannot be > 16")
		self._daq.set(self._path + "averaging", averaging_mode)

	def get_sample(self):
		return self._daq.get(self._path + "sample")


class AuxOut():
	def  __init__(self, daq, dev_id, n):
		self._daq = daq
		self._path = dev_id + "/auxouts/" + str(n) + "/"

	def set_demod_select(self, value):
		# Select the channel number of the selected signal source.
		self._daq.set(self._path + "demodselect", value)

	def set_limit_lower(self, value):
		#Lower limit for the signal at the Auxiliary Output. A smaller value will be clipped.
		self._daq.set(self._path + "limitlower", value)

	def set_limit_upper(self, value):
		#Upper limit for the signal at the Auxiliary Output. A larger value will be clipped.
		self._daq.set(self._path + "limitupper", value)

	def set_offset(self, value):
		#Add the specified offset voltage to the signal after scaling. Auxiliary Output Value = (Signal +Preoffset)*Scale + Offset
		self._daq.set(self._path + "offset", value)

	def set_output_select(self, enum_):
		#Select the signal source to be represented on the Auxiliary Output.
		self._daq.set(self._path + "outputselect", enum_.value)

	class OutputSelect(Enum):
		manual = -1
		demod_x = 0
		demod_y = 1
		demod_r = 2
		demod_theta = 3
		pid = 5
		pid_shift = 9
		pid_error = 10
		tu_filtered = 11
		tu_output = 13

	def set_preoffset(self, value):
		# Add a pre-offset to the signal before scaling is applied. Auxiliary Output Value = (Signal +Preoffset)*Scale + Offset
		self._daq.set(self._path + "preoffset", value)
		
	def set_scale(self, value):
		# Multiplication factor to scale the signal. Auxiliary Output Value = (Signal+Preoffset)*Scale + Offset
		self._daq.set(self._path + "scale", value)

	def enable_tipprotect(self):
		self._daq.set(self._path + "tipprotect/preoffset", True)

	def disable_tipprotect(self):
		self._daq.set(self._path + "tipprotect/preoffset", False)

	def set_tipprotect_polarity(self, value):
		self._daq.set(self._path + "tipprotect/polarity", value)

	def set_tipprotect_source(self, value):
		self._daq.set(self._path + "tipprotect/source", value)

	def set_tipprotect_value(self,value):
		self._daq.set(self._path + "tipprotect/value", value)

	def get_value(self):
		# Voltage present on the Auxiliary Output. Auxiliary Output Value = (Signal+Preoffset)*Scale + Offset
		self._daq.get(self._path+ "value")

#clockbase?


class Currin():
	def  __init__(self, daq, dev_id, n):
		self._daq = daq
		self._path = dev_id + "/currin/" + str(n) + "/"

	def set_autorange(self, value):
		self._daq.set(self._path + "autorange", value)

	def set_floating(self, enum_):
		# Switches the input between floating (ON) and connected grounds (OFF). This setting applies both to the voltage and the current input. It is recommended to discharge the test device before connecting or to enable this setting only after the signal source has been connected to the Signal Input in grounded mode.
		self._daq.set(self._path + "autorange", enum_.value)

	class Floating(Enum):
		GND_connected = 0
		floating = 1

	def set_max(self, enum_):
		# Gives the maximum measured input current (peak value) normalized to input range.
		self._daq.set(self._path + "max", enum_.value)

	def set_min(self, enum_):
		# Gives the minimum measured input current (peak value) normalized to input range.
		self._daq.set(self._path + "min", enum_.value)

	# what are the values here?
	def enable_input(self):
		# Enables the current input.
		self._daq.set(self._path + "on", 0)

	def disable_input(self):
		# Disables the current input.
		self._daq.set(self._path + "off", 1)

	def set_input_range(self, value):
		# Defines the gain of the current input amplifier. The range should exceed the incoming signal by roughly a factor of two including a potential DC offset. The instrument selects the next higher available range relative to a value inserted by the user. A suitable choice of this setting optimizes the accuracy and signal-to-noise ratio by ensuring that the full dynamic range of the input ADC is used.
		self._daq.set(self._path + "range", value)

	def set_rangestep_trigger(self, value):
		# Switches to the next appropriate input range such that the range fits best with the measured input current.
		self._daq.set(self._path + "rangestep_trigger", value)

	def set_scaling(self, value):
		#Applies the given scale factor to the current input.
		self._daq.set(self._path + "scaling", value)




class DIO():
	def  __init__(self, daq, dev_id, n):
		self._daq = daq
		self._path = dev_id + "/dios/" + str(n) + "/"

	def set_decimation(self, value):
		# Sets the decimation factor for DIO data streamed to the host computer.
		self._daq.set(self._path + "decimation", value)

	def set_drive(self, value):
		# When on (1), the corresponding 8-bit bus is in output mode. When off (0), it is in input mode. Bit 0 corresponds to the least significant byte. For example, the value 1 drives the least significant byte, the value 8 drives the most significant byte.
		self._daq.set(self._path + "drive", value)

	def set_internal_clock(self, ):
		# Select DIO internal clocking.
		self._daq.set(self._path + "extclk", 0)

	def set_external_clock(self, ):
		# Select DIO external clocking.
		self._daq.set(self._path + "extclk", 1)

	def set_dio_manual_mode(self, ):
		self._daq.set(self._path + "mode", 0)

	def set_dio_threshold_unit(self, ):
		self._daq.set(self._path + "mode", 3)

	def set_output(self, value):
		# Sets the value of the DIO output for those bytes where 'drive' is enabled.
		self._daq.set(self._path + "output", value)


class ExtRef():
	def  __init__(self, daq, dev_id, n):
		self._daq = daq
		self._path = dev_id + "/extrefs/" + str(n) + "/"

	def set_ADC_select(self, enum_):
		# Indicates the input signal selection for the selected demodulator.
		# TODO use the same enum_ as above?
		self._daq.set(self._path + "mode", enum_.value)

	def set_automode(self, enum_):
		# This defines the type of automatic adaptation of parameters in the PID used for Ext Ref.
		self._daq.set(self._path + "automode", enum_.value)

	class Automode(Enum):
		off = 0
		coefficients_only = 1
		low_bandwidth = 2
		high_bandwidth = 3
		all = 4

	def set_demod_select(self, value):
		# Indicates the demodulator connected to the extref channel.
		self._daq.set(self._path + "demodselect", value)

	def set_enable(self, ):
		# TODO enable and disable?
		self._daq.set(self._path + "enable")

	def get_is_locked(self, ):
		# Indicates whether the external reference is locked.
		locked = self._daq.get(self._path + "locked")
		# TODO is 0 true?
		return locked == 0

	def get_osc_locked_to_ext_source(self, ):
		# Indicates which oscillator is being locked to the external reference.
		# TODO should we change here the first index to 1?
		return self._daq.get(self._path + "oscselect")


class Features():
	def  __init__(self, daq, dev_id):
		self._daq = daq
		self._path = dev_id + "/features/"

	def set_feature_code(self, value):
		# Node providing a mechanism to write feature codes.
		self._daq.set(self._path + "code", value)

	def get_device_type(self, ):
		# Returns the device type.
		return self._daq.get(self._path + "devtype")

	def get_options(self, ):
		# Returns enabled options.
		return self._daq.get(self._path + "options")

	def get_serial(self, ):
		# Returns the device serial number.
		return self._daq.get(self._path + "serial")



class Modulation():
	def  __init__(self, daq, dev_id, n):
		self._daq = daq
		self._path = dev_id + "/mods/" + str(n) + "/"

	def set_carrier_amplitude(self, value):
		# Set the carrier amplitude.
		self._daq.set(self._path + "carrier/amplitude", value)

	def enable_carrier(self, ):
		# Enable the modulation.
		self._daq.set(self._path + "carrier/enable", 0)

	def disable_carrier(self, ):
		# Disable the modulation.
		self._daq.set(self._path + "carrier/enable", 1)

	def set_carrier_harmonic(self, value):
		# Set the harmonic of the carrier frequency. 1 = Fundamental
		self._daq.set(self._path + "carrier/hermonic", value)

	def set_carrier_input_select(self, enum_):
		# Select Signal Input for the carrier demodulation 
		self._daq.set(self._path + "voltage/inputselect", enum_.value)

	class InputSelect(Enum):
		#TODO is this enum_ redundant?
		signal_input_1 = 0

	def set_carrier_filter_order(self, enum_):
		# Filter order used for carrier demodulation.
		#TODO the enum_ is redundant. What to do?
		self._daq.set(self._path + "carrier/order", enum_.value)

	def set_carrier_osc_select(self, value):
		# Select the oscillator for the carrier signal.
		#TODO index problem
		self._daq.set(self._path + "carrier/oscselect", value)

	def set_carrier_phase_shift(self, value):
		# Phase shift applied to the reference input of the carrier demodulator and also to the carrier signal on the Signal Outputs
		self._daq.set(self._path + "carrier/phaseshift", value)

	def set_carrier_time_constant(self, value):
		# Sets the integration time constant or in other words, the cutoff frequency of the low-pass filter for the carrier demodulation.
		self._daq.set(self._path + "carrier/timeconstant", value)

	def enable_modulation(self, ):
		# Enables the modulation.
		self._daq.set(self._path + "enable", 0)

	def disable_modulation(self, ):
		# Disables the modulation.
		self._daq.set(self._path + "enable", 1)

	def set_frequency_peak_deviation(self, value):
		# FM mode peak deviation value.
		self._daq.set(self._path + "freqdev", value)

	def set_frequency_deviation_mode(self, enum_):
		# In FM mode, choose to work with either modulation index or peak deviation. The modulation index equals peak deviation divided by modulation frequency. 
		self._daq.set(self._path + "freqdevenable", enum_.value)

	class FrequencyDeviationMode(Enum):
		modulation_index = 0
		peak_eviation = 1

	def set_modulation_index(self, value):
		# FM modulation index: The modulation index equals peak deviation divided by modulation frequency.
		self._daq.set(self._path + "index", value)

	def set_modulation_mode(self, enum_):
		# Select the modulation mode. 
		self._daq.set(self._path + "index", enum_.value)

	class FM_Mode(Enum):
		am = 0
		fm = 1
		manual = 2

	def set_frequency_peak_deviation(self, enum_):
		# Select Signal Output.
		self._daq.set(self._path + "output", enum_.value)

	class Output(Enum):
		none = 0
		signal_output_1 = 1

	def set_sideband_amplitude(self, m, value):
		#TODO make sidebands a class? How many sidebands are there? I think all nods should be known beforehand?
		# Set the amplitude of the sideband components.
		self._daq.set(self._path + "sidebands/" + str(m) + "/amplitude", value)

	def enable_sideband(self, m):
		# Enable the signal generation for the respective sideband.
		self._daq.set(self._path + "sidebands/" + str(m) + "/enable", 0)

	def disable_sideband(self, m):
		# Disable the signal generation for the respective sideband.
		self._daq.set(self._path + "sidebands/" + str(m) + "/enable", 1)

	def set_sideband_amplitude(self, m, value):
		#Set harmonic of the sideband frequencies. 1 = fundamental
		self._daq.set(self._path + "sidebands/" + str(m) + "/harmonic", value)

	def set_input(self, m, value):
		#Select Signal Input for the sideband demodulation
		#TODO I think this enum_ is redundant. -> move it out of the classes
		self._daq.set(self._path + "sidebands/" + str(m) + "/harmonic", value)

	def set_sideband_mode(self, m, enum_):
		#Enabling of the first sideband and selection of the position of the sideband relative to the carrier frequency for manual mode.
		self._daq.set(self._path + "sidebands/" + str(m) + "/mode", enum_.value)

	class SelectSideband(Enum):
		off = 0
		upper = 1
		lower = 2

	def set_filter_order(self, m, enum_):
		#Filter order used for sideband demodulation
		#TODO this enum_ is redundant. -> move it out of the classes
		self._daq.set(self._path + "sidebands/" + str(m) + "/order", enum_.value)

	def set_oscselect(self, m, enum_):
		#Filter order used for sideband demodulation
		#TODO this enum_ is redundant. -> move it out of the classes
		self._daq.set(self._path + "sidebands/" + str(m) + "/order", enum_.value)

	def set_phaseshift(self, m, value):
		#Phase shift applied to the reference input of the sideband demodulator and also to the sideband signal on the Signal Outputs
		self._daq.set(self._path + "sidebands/" + str(m) + "/phaseshift", value)

	def set_time_constant(self, m, value):
		#Sets the integration time constant or in other words, the cutoff frequency of the low-pass filter for the sideband demodulation.
		self._daq.set(self._path + "sidebands/" + str(m) + "/timeconstant", value)

class Frequency():
	def __init__(self, path):
		self._path = path + "frequency"

	def get_path(self):
		return self._path

class Oscillator():
	def  __init__(self, daq, dev_id, n):
		self._daq = daq
		self._path = dev_id + "/oscs/" + str(n) + "/"
		self.frequency = Frequency(self._path)

	def set_frequency(self, value):
		#Frequency control for each oscillator.
		self._daq.set(self._path + "freq", value)

	def get_frequency(self):
		return self._daq.get(self._path + "freq")


class Sample():
	def __init__(self, daq, path):
		self._daq = daq
		self._path = path + "sample"

	def subscribe(self):
		self._daq.subscribe(self._path)


class Demod():
	def  __init__(self, daq, dev_id, n):
		self._daq = daq
		self._path = dev_id + "/demods/" + str(n) + "/"
		self.sample = Sample(daq, self._path)

	def set_ADC_select(self, enum_):
		# Selects the input signal for the demodulator.
		self._daq.set(self._path + "adcselect", enum_.value)

	class ADC_select_options(Enum):
		# should signal_input, etc. start with 1? Probably yes
		signal_input_0 = 0
		current_input_0 = 1
		trigger_input_0 = 2
		trigger_input_1 = 3
		auxiliary_output_0 = 4
		auxiliary_output_1 = 5
		auxiliary_output_2 = 6
		auxiliary_output_3 = 7
		auxiliary_input_0 = 8
		auxiliary_input_1 = 9
		demod_constant_input = 174

	def enable(self):
		# Enables the data acquisition for the corresponding demodulator. Note: increasing number of active demodulators increases load on the physical connection to the host computer.
		self._daq.set(self._path + "enable", 1)

	def disable(self):
		# Disables the data acquisition for the corresponding demodulator.
		self._daq.set(self._path + "enable", 0)

	def set_frequency(self, value):
		# Indicates the frequency used for demodulation and for output generation. The demodulation frequency is calculated with oscillator frequency times the harmonic factor. When the MOD option is used linear combinations of oscillator frequencies including the harmonic factors define the demodulation frequencies.
		self._daq.set(self._path + "freq", value)

	def set_harmonic(self, value):
		# Multiplies the demodulator’s reference frequency by an integer factor. If the demodulator is used as a phase detector in external reference mode (PLL), the effect is that the internal oscillator locks to the external frequency divided by the integer factor.
		self._daq.set(self._path + "harmonic", value)

	#TODO split this off into 8 functions? Or wite 1 function with an argument?
	def set_1st_order(self, ):
		# Selects the filter roll off to 6 dB/oct.
		self._daq.set(self._path + "order", 1)

	def set_2nd_order(self, ):
		# Selects the filter roll off to 12 dB/oct.
		self._daq.set(self._path + "order", 2)

	def set_3rd_order(self, ):
		# Selects the filter roll off to 18 dB/oct.
		self._daq.set(self._path + "order", 3)

	def set_4th_order(self, ):
		# Selects the filter roll off to 24 dB/oct.
		self._daq.set(self._path + "order", 4)

	def set_5th_order(self, ):
		# Selects the filter roll off to 30 dB/oct.
		self._daq.set(self._path + "order", 5)

	def set_6th_order(self, ):
		# Selects the filter roll off to 36 dB/oct.
		self._daq.set(self._path + "order", 6)

	def set_7th_order(self, ):
		# Selects the filter roll off to 42 dB/oct.
		self._daq.set(self._path + "order", 7)

	def set_8th_order(self, ):
		# Selects the filter roll off to 48 dB/oct.
		self._daq.set(self._path + "order", 8)

	def select_oscillator(self, value):
		#how to deal with the 0 index? Use an enum_?
		# Connects the demodulator with the supplied oscillator. Number of available oscillators depends on the installed options.
		self._daq.set(self._path + "oscselect", value)

	def set_phase_adjust(self, value):
		# ??
		# Adjust the demodulator phase automatically in order to read 0 degrees.
		self._daq.set(self._path + "phaseadjust", value)

	def set_phase_shift(self, value):
		# Phase shift applied to the reference input of the demodulator.
		self._daq.set(self._path + "phaseshift", value)

	def set_rate(self, value):
		# Defines the demodulator sampling rate, the number of samples that are sent to the host computer per second. A rate of about 7-10 higher as compared to the filter bandwidth usually provides sufficient aliasing suppression. This is also the rate of data received by LabOne Data Server and saved to the computer hard disk. This setting has no impact on the sample rate on the auxiliary outputs connectors. Note: the value inserted by the user may be approximated to the nearest value supported by the instrument.
		self._daq.set(self._path + "rate", value)

	def get_sample(self, ):
		# TODO Only get or also get_as_event, etc.?
		# Contains streamed demodulator samples with sample interval defined by the demodulator data rate.
		return self._daq.get(self._path + "sample")

	def set_sinc(self, value):
		# Enables the sinc filter. When the filter bandwidth is comparable to or larger than the demodulation frequency, the demodulator output may contain frequency components at the frequency of demodulation and its higher harmonics. The sinc is an additional filter that attenuates these unwanted components in the demodulator output.
		self._daq.set(self._path + "sinc", value)

	def set_time_constant(self, value):
		# Sets the integration time constant or in other words, the cutoff frequency of the demodulator low pass filter.
		self._daq.set(self._path + "sinc", value)

	def set_trigger_mode(self, enum_):
		# Selects the acquisition mode (i.e. triggering) or the demodulator.
		self._daq.set(self._path + "trigger/triggeracq", enum_.value)

	def set_trigger_source(self, enum_):
		self._daq.set(self._path + "trigger/source", enum_.value)

	class TriggerSource(Enum):
		software_trigger = 1024
		# TODO etc.

	# TODO some stuff here belongs to Demods
	class TriggerMode(Enum):
		continuous = 0
		trigger_input_0_rising = 1
		# TODO etc.


	def enable_triggered_acquisition(self):
		self._daq.set(self._path + "trigger/triggeracq", 1)

	def disable_triggered_acquisition(self):
		self._daq.set(self._path + "trigger/triggeracq", 0)

	def set_burst_length(self, length):
		self._daq.set(self._path + "burstlen", length)

	def set_data_rate(self, rate):
		self._daq.set(self._path + "rate", rate)

class Demodulator():
	# Demodulator vs. Demod?
	def __init__(self, daq, dev_id, index):
		self._daq = daq
		self._path = dev_id + "/demods/" + str(index) + "/"

	def enable(self):
		self._daq.set(self._path + "enable", 1)

	def disable(self):
		self._daq.set(self._path + "enable", 0)

	def subscribe_sample(self):
		self._daq.subscribe(self._path + "sample")

	def get_sample_as_event(self):
		self._daq.getAsEvent(self._path + "sample")


class DUT():
	def __init__(self, daq, path) -> None:
		self._daq = daq
		self._path = path + "dut/"

	def set_bandwidth(self, value):
		self._daq.set(self._path + "bw", value)

	def set_damping(self, value):
		self._daq.set(self._path + "damping", value)

