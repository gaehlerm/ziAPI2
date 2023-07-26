# example from the LabOne Programming manual p.41
from enum import Enum

class Save():
	def __init__(self, daq):
		self._daq = daq

	def set_fileformat(self, FileFormat):
		self._daq.set("save/fileformat", FileFormat.value())

	#figure out again how define enum_s
	class FileFormat(Enum):
		mat = 0
		csv = 1
		zview = 2
		sxm = 3
		hdf5 = 4

class System():
	def __init__(self, daq, dev_id):
		self._daq = daq
		self._path = dev_id + "/system/properties"

	def get_timebase(self):
		return self._daq.get(self._path + "/timebase")


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
		self._daq.set(self._path + "outputselect", enum_.value())

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

	def set_tipprotect_enable(self):
		self._daq.set(self._path + "tipprotect/preoffset", True)

	def set_tipprotect_disable(self):
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

	def set_autorange(self,value):
		self._daq.set(self._path + "autorange", value)

	def set_floating(self,enum_):
		# Switches the input between floating (ON) and connected grounds (OFF). This setting applies both to the voltage and the current input. It is recommended to discharge the test device before connecting or to enable this setting only after the signal source has been connected to the Signal Input in grounded mode.
		self._daq.set(self._path + "autorange", enum_.value)

	class Floating(Enum):
		GND_connected = 0
		floating = 1

	def set_max(self,enum_):
		# Gives the maximum measured input current (peak value) normalized to input range.
		self._daq.set(self._path + "max", enum_.value)

	def set_min(self, enum_):
		# Gives the minimum measured input current (peak value) normalized to input range.
		self._daq.set(self._path + "min", enum_.value)

	#what are the values here?
	def input_enable(self):
		# Enables the current input.
		self._daq.set(self._path + "on", 0)

	def input_disable(self):
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

class Sample():
	def __init__(self, daq, path):
		self._daq = daq
		self._path = path

	def subscribe(self):
		self._daq.subscribe(self._path + "sample")


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

	def enable(self, ):
		# Enables the data acquisition for the corresponding demodulator. Note: increasing number of active demodulators increases load on the physical connection to the host computer.
		self._daq.set(self._path + "enable", 1)

	def disable(self, ):
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

	class TriggerMode(Enum):
		continuous = 0
		trigger_input_0_rising = 1
		# TODO etc.


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
		self._daq.set(self._path + "mode", enum_.value())

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

class Impedance():
	def  __init__(self, daq, dev_id, n):
		self._daq = daq
		self._path = dev_id + "/imps/" + str(n) + "/"

	def set_AC(self, value):
		# Defines the input coupling for the Signal Inputs. AC coupling inserts a high-pass filter.
		#TODO ??
		self._daq.set(self._path + "ac", value)

	def enable_automatic_bandwidth_control(self, ):
		# Enable automatic bandwidth control. If enabled the optimum bandwidth is calculated based on the frequency and measurement data.
		#TODO disabling function? value?
		self._daq.set(self._path + "auto/bw", 0)

	def set_input_range_control_mode(self, enum_):
		# Select input range control mode.
		self._daq.set(self._path + "auto/inputrange", enum_.value())

	class InputRangeControlMode(Enum):
		manual = 0
		auto = 1
		zone = 2

	def enable_auto_output(self, ):
		# The drive voltage amplitude is controlled by the device.
		# TODO is the 0/1 here correct? 
		self._daq.set(self._path + "auto/output", 0)

	def disable_auto_output(self, ):
		# The drive voltage amplitude can be set manually.
		# TODO is the 0/1 here correct? 
		self._daq.set(self._path + "auto/output", 1)

	def enable_auto_suppress(self, ):
		# Indicates disabled periodic auto range control. A running sweeper module takes over the range control and thus disables the periodic range checks.
		# TODO again: is this a true/false node?
		self._daq.set(self._path + "auto/suppress", 0)

	def enable_DC_bias(self, ):
		# DC bias voltage applied across the device under test. Both positive and negative bias voltages are supported. In a 4-terminal measurement, the bias voltage is limited by the maximum common voltage input range of the device. In a 2-terminal measurement, the bias voltage can be larger because the voltage inputs are not connected.
		# TODO is the 0/1 here correct? 
		self._daq.set(self._path + "auto/output", 0)

	def get_active_internal_calibration(self, ):
		# Indicates if the internal calibration is applied to the measurement data.
		return self._daq.get(self._path + "calib/internal/enable")

	def enable_internal_calibration(self, ):
		# Enables the internal calibration. This ensures that the input range gains match over the full frequency range. With enabled internal calibration the device fulfills the impedance accuracy specification. The internal calibration is a prerequisite to apply a user compensation.
		# TODO 0/1?
		self._daq.set(self._path + "calib/internal/enable", 0)

	def disable_internal_calibration(self, ):
		# Disables the internal calibration.
		# TODO 0/1?
		self._daq.set(self._path + "calib/internal/enable", 1)

	def enable_calibration_smoothing(self, ):
		# Enables smoothing of the internal calibration data. This results in lower noise in the measured data.
		# TODO 0/1?
		self._daq.set(self._path + "calib/internal/smooth", 0)

	def disable_calibration_smoothing(self, ):
		# Disables smoothing of the internal calibration data.
		# TODO 0/1?
		self._daq.set(self._path + "calib/internal/smooth", 1)

	def user_compensation_is_active(self, ):
		# Indicates that a valid user compensation is active. If active the impedance data streams deliver amplitude and phase corrected data based on the impedance user compensation.
		# TODO 0/1?
		is_active = self._daq.get(self._path + "calib/user/active", 0)
		return is_active == 0

	def enable_user_compensation(self, ):
		# Enables the user compensation of the impedance data. The user compensation is correcting parasitics and delays caused by the external setup. The user compensation is applied on top of the internal impedance calibration.
		# TODO 0/1?
		self._daq.set(self._path + "calib/user/enable", 0)

	def disable_user_compensation(self, ):
		# Disables the user compensation of the impedance data.
		# TODO 0/1?
		self._daq.set(self._path + "calib/user/enable", 1)

	def enable_compensation_smoothing(self, ):
		# Enables smoothing of the compensation data. This results in lower noise in the measured data.
		# TODO 0/1?
		self._daq.set(self._path + "calib/user/enable", 0)

	def disable_compensation_smoothing(self, ):
		# Disables smoothing of the compensation data.
		# TODO 0/1?
		self._daq.set(self._path + "calib/user/enable", 1)

	def enable_compensation_indication(self, ):
		# Enables the indication of strong compensation in the plots. A strong compensation diminishes the measurement accuracy of the parameter.
		# TODO 0/1?
		self._daq.set(self._path + "confidence/compensation/enable", 0)

	def disable_compensation_indication(self, ):
		# Disables the indication of strong compensation in the plots.
		# TODO 0/1?
		self._daq.set(self._path + "confidence/compensation/enable", 1)

	def set_compensation_ratio_warning(self, value):
		# Strength of the compensation that will trigger the strong compensation warning.
		self._daq.set(self._path + "confidence/compensation/ratio", value)

	def enable_confidence_indicators(self, ):
		# Enables all confidence indicators to check the reliability of the measured data. To enable individual indicators, open the advanced tab.
		# TODO 0/1?
		self._daq.set(self._path + "confidence/enable", 0)

	def disable_confidence_indicators(self, ):
		# Disables all confidence indicators to check the reliability of the measured data. To enable individual indicators, open the advanced tab.
		# TODO 0/1?
		self._daq.set(self._path + "confidence/enable", 1)

	def enable_frequency_limit_detection(self, ):
		# Enables the frequency limit detection based on the used current input range. Only relevant when Range Control is set to Manual.
		# TODO 0/1?
		self._daq.set(self._path + "confidence/freqlimit/enable", 0)

	def disable_frequency_limit_detection(self, ):
		# Disables the frequency limit detection.
		# TODO 0/1?
		self._daq.set(self._path + "confidence/freqlimit/enable", 1)

	def enable_low_DUT2T_warning(self, ):
		# Enables a warning when measuring a low impedance (100k) with a 2 point contact.
		# TODO 0/1?
		self._daq.set(self._path + "confidence/lowdut2t/enable", 0)

	def disable_low_DUT2T_warning(self, ):
		# Disables the low TUD2T warning
		# TODO 0/1?
		self._daq.set(self._path + "confidence/lowdut2t/enable", 1)

	def low_DUT2T_ratio(self, value):
		# When measuring with 2 point contacts, too low impedance of DUT will trigger the Low DUT 2T warning.
		# TODO rework text?
		self._daq.set(self._path + "confidence/lowdut2t/ratio", value)

	def enable_detecting_one_period_measurements(self, ):
		# Enables the detection of unreliable data points where data sample loss leads to an invalid oneperiod average. Try reducing the data transfer rate.
		# TODO 0/1?
		self._daq.set(self._path + "confidence/oneperiod/enable", 0)

	def disable_detecting_one_period_measurements(self, ):
		# Disables the detection of unreliable data points.
		# TODO 0/1?
		self._daq.set(self._path + "confidence/oneperiod/enable", 1)

	def enable_open_terminal_detection(self, ):
		# Enables the open terminal detection for 4-terminal measurements.
		# TODO 0/1?
		self._daq.set(self._path + "confidence/opendetect/enable", 0)

	def disable_open_terminal_detection(self, ):
		# Disables the open terminal detection for 4-terminal measurements.
		# TODO 0/1?
		self._daq.set(self._path + "confidence/opendetect/enable", 1)

	def set_open_terminal_detection_ratio(self, value):
		# Enables the open terminal detection for 4-terminal measurements.
		self._daq.set(self._path + "confidence/opendetect/ratio", 0)

	def enable_overflow_detection(self, ):
		# Enables the overload detection for current and voltage.
		# TODO 0/1?
		self._daq.set(self._path + "confidence/overflow/enable", 0)

	def disable_overflow_detection(self, ):
		# Disables the overload detection for current and voltage.
		# TODO 0/1?
		self._daq.set(self._path + "confidence/overflow/enable", 1)

	def enable_Q_factor_detection(self, ):
		# Enables the detection of negative Q or D factors. Negative Q or D factors mean the measured impedance does not correspond to the chosen Representation. This can be due to an erroneous compensation, a bad choice of the Representation, or noise.
		# TODO 0/1?
		self._daq.set(self._path + "confidence/qfactor/enable", 0)

	def disable_Q_factor_detection(self, ):
		# Disables the detection of negative Q or D factors.
		# TODO 0/1?
		self._daq.set(self._path + "confidence/qfactor/enable", 1)

	def enable_suppression_confidence_indicator(self, ):
		# The Suppression Confidence Indicator indicates if one of the two parameters of a circuit representation cannot be calculated reliably from the measured impedance. This is the case if a small variation in one (dominant) representation parameter creates a strong variation of the other (suppressed) representation parameter. Such an error amplification indicates that the measurement of the secondary parameter is unreliable.
		# TODO 0/1?
		self._daq.set(self._path + "confidence/suppression/enable", 0)

	def disable_suppression_confidence_indicator(self, ):
		# Disable the Suppression Confidence Indicator.
		# TODO 0/1?
		self._daq.set(self._path + "confidence/suppression/enable", 1)

	def set_suppression_confidence_ratio(self, value):
		# Error amplification limit for which a secondary parameter is marked unreliable. Larger gain values mean larger warning tolerances. A gain value between 10 and 100 is best.
		# TODO 0/1?
		self._daq.set(self._path + "confidence/suppression/ratio", value)

	def enable_underflow_detection(self, ):
		# Enables the underflow detection for current and voltage.
		# TODO 0/1?
		self._daq.set(self._path + "confidence/underflow/enable", 0)

	def disable_underflow_detection(self, ):
		# Disables the underflow detection for current and voltage.
		# TODO 0/1?
		self._daq.set(self._path + "confidence/underflow/enable", 1)

	def set_underflow_ratio(self, value):
		# The underflow condition is met if the measured amplitude is lower than the specified ratio relative to full scale.
		self._daq.set(self._path + "confidence/underflow/ratio", value)
	
	def select_demod(self, value):
		# Demodulator used for current demodulation.
		# correct for the 0 index?
		self._daq.set(self._path + "current/demodselect", value)

	def select_input(self, enum_):
		# Demodulator used for current demodulation.
		self._daq.set(self._path + "current/inputselect", enum_.value())

	class InputSelect(Enum):
		current_input0 = 0
		auxiliary_input0 = 8
		auxiliary_input1 = 9 

	def enable_invert_signal(self, ):
		# If enabled, the current input signal is inverted. This is useful to switch the polarity of an input signal which can be caused by additional current amplifiers.
		self._daq.set(self._path + "current/invert", 0)

	def disable_invert_signal(self, ):
		# Disable the current input signal invertion.
		self._daq.set(self._path + "current/invert", 1)

	def enable_using_PID_value(self, ):
		# If enabled, the PID value is used for the impedance calculation instead of the measured value at the current input.
		self._daq.set(self._path + "current/pid/enable", 0)

	def disable_using_PID_value(self, ):
		# Use the measured value at the current input for impedance calculation.
		self._daq.set(self._path + "current/pid/enable", 1)

	def set_input_current_range(self, value):
		# Input current range used for the impedance measurement. Small current input ranges have a reduced bandwidth. In the Range Control modes 'Auto' and 'Impedance', the current range is switched automatically to a higher range if the frequency is too high.
		self._daq.set(self._path + "current/range", value)

	def set_current_scaling(self, value):
		# The scaling factor will be applied to the current measurement done with an Aux In input.
		self._daq.set(self._path + "current/scaling", value)

	def set_demod_harmonic(self, value):
		# Multiplies the demodulator’s reference frequency with the integer factor defined by this field.
		self._daq.set(self._path + "demod/harmonic", value)

	def set_demod_filter_order(self, value):
		# Selects the filter roll off between 6 dB/oct and 48 dB/oct of the current demodulator.
		# TODO use the same functions as for the Demod filter?
		self._daq.set(self._path + "demod/order", value)

	def set_oscillator_select(self, value):
		# Oscillator used to generate the frequency of the excitation voltage on the Hcur (+V) connector.
		# TODO use the same functions as for the Demod?
		self._daq.set(self._path + "demod/oscselect", value)

	def set_demod_rate(self, value):
		# Impedance data streaming rate. The same data rate is applied to the demodulators that are used for the impedance measurement.
		self._daq.set(self._path + "demod/rate", value)

	def enable_demod_sinc(self, ):
		# Enables the sinc filter.
		self._daq.set(self._path + "demod/rate", 0)

	def disable_demod_sinc(self, ):
		# Disables the sinc filter.
		self._daq.set(self._path + "demod/rate", 1)

	def set_demod_timeconstant(self, value):
		# Defines low pass filter time constant.
		self._daq.set(self._path + "demod/timeconstant", value)

	def enable_discard(self, ):
		# Enables discarding impedance samples outside the indicated range.
		self._daq.set(self._path + "discard/enable", 0)

	def disable_discard(self, ):
		# Disables discarding impedance samples outside the indicated range.
		self._daq.set(self._path + "discard/enable", 1)

	def set_discard_lower_limit(self, value):
		# Threshold for abs(Z) below which the impedance samples are discarded.
		self._daq.set(self._path + "discard/limitlower", value)

	def set_discard_upper_limit(self, value):
		# Threshold for abs(Z) above which the impedance samples are discarded.
		self._daq.set(self._path + "discard/limitupper", value)

	def enable_demod_data(self, ):
		# Enable impedance calculation for demodulator data.
		self._daq.set(self._path + "enable", 0)

	def disable_demod_data(self, ):
		# Disable impedance calculation for demodulator data.
		self._daq.set(self._path + "enable", 1)

	def set_frequency_control(self, value):
		# Frequency control for the oscillator used for impedance measurement.
		self._daq.set(self._path + "freq", value)

	def set_interpolation_type(self, enum_):
		# Select the interpolation method of the compensation data. The interpolation method is particularly important if the derivative changes strongly e.g at cut-off frequencies.
		self._daq.set(self._path + "inerpolation", enum_.value)

	class Interpolation(enum_):
		linear = 0
		pchip = 1

	def set_max_bandwidth(self, value):
		# Limit of the maximum bandwidth used on the demodulator filter. Values above 1 kHz can heavily diminish measurement accuracy in the high-frequency region where the amplitude is no more constant over frequency.
		self._daq.set(self._path + "max_bandwidth", value)

	def set_impedance_measurement_mode(self, enum_):
		# Select impedance measurement mode. 
		self._daq.set(self._path + "inerpolation", enum_.value)

	class Interpolation(Enum):
		# TODO find better names
		_4_terminal = 0
		_2_terminal = 1

	def set_model(self, enum_):
		# Representation of the complex impedance value Z by two real values accessible as Parameter 1 and Parameter 2 on all user interface displays. 
		self._daq.set(self._path + "model", enum_.value())

	class Interpolation(Enum):
		# TODO find better names
		r_c_parallel = 0 
		r_c_series = 1 
		r_l_series = 2
		g_b_parallel = 3 
		d_c_series = 4
		q_c_series = 5 
		d_l_series = 6 
		q_l_series = 7 
		r_l_parallel = 8 
		d_c_parallel = 9 

	def set_omega_suppression(self, value):
		# Suppression of the omega and 2-omega components. Small omega suppression can diminish measurements of very low or high impedance because the DC component can become dominant. Large omega suppression will have a significant impact on sweep time especially for low filter orders.
		self._daq.set(self._path + "omegasuppression", value)

	def enable_one_period_averaging(self, ):
		# Enables one-period averaging for low frequency impedance measurements. The LED is green when active.
		# TODO .../active node is redundant?
		self._daq.set(self._path + "oneperiod/enable", 0)

	def disable_one_period_averaging(self, ):
		# Disables one-period averaging for low frequency impedance measurements.
		self._daq.set(self._path + "oneperiod/enable", 1)

	def set_output_amplitude(self, value):
		# Drive amplitude on the Signal Output.
		self._daq.set(self._path + "output/amplitude", value)

	def set_output_demod(self, value):
		# Demodulator unit used to generate the excitation voltage on the Signal Output.
		self._daq.set(self._path + "output/demod", value)

	def enable_output(self, ):
		# Enables the Signal Output corresponding to the blue LED indicator on the instrument front panel.
		self._daq.set(self._path + "output/on", 0)

	def disable_output(self, ):
		# Disables the Signal Output.
		self._daq.set(self._path + "output/on", 1)

	def set_output_range(self, value):
		# Selects the output voltage range.
		self._daq.set(self._path + "output/range", value)

	def set_output_select(self, enum_):
		# Selects the output channel that the excitation voltage drives.
		self._daq.set(self._path + "output/select", enum_.value())

	class OutputSelect(Enum):
		# TODO what is this enum_ supposed to do??
		# TODO use index 1 or 0?
		signal_output1 = 0 

	def get_samples(self, ):
		# Streaming node containing the impedance measurement sample data.
		return self._daq.get(self._path + "sample")

	def get_voltage_demod_select(self, ):
		# Demodulator used for voltage measurement in case of a four-terminal impedance measurement.
		return self._daq.get(self._path + "voltage/demodselect")

	def set_voltage_input_select(self, enum_):
		# Select the voltage input used for a four-terminal impedance measurement.
		self._daq.set(self._path + "voltage/inputselect", enum_.value())

	class OutputSelect(Enum):
		#TODO index?
		signal_input1 = 0
		auxiliary_input1 = 8 
		auxiliary_input2 = 9 

	def enable_voltage_invert(self, ):
		# If enabled, the voltage input signal is inverted.
		self._daq.set(self._path + "voltage/invert", 0)

	def disable_voltage_invert(self, ):
		# The voltage input signal is not inverted.
		self._daq.set(self._path + "voltage/invert", 1)

	def set_voltage_range(self, value):
		# Input voltage range for the impedance measurement.
		self._daq.set(self._path + "voltage/range", value)

	def set_voltage_scaling(self, value):
		# The scaling factor will be applied to the voltage measurement done with an Aux In input.
		self._daq.set(self._path + "voltage/scaling", value)


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
		self._daq.set(self._path + "freqdevenable", enum_.value())

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


class Oscillator():
	def  __init__(self, daq, dev_id, n):
		self._daq = daq
		self._path = dev_id + "/oscs/" + str(n) + "/"

	def set_frequency(self, value):
		#Frequency control for each oscillator.
		self._daq.set(self._path + "freq", value)

	def get_frequency(self):
		return self._daq.get(self._path + "freq")

class PID():
	def  __init__(self, daq, dev_id, n):
		self._daq = daq
		self._path = dev_id + "/pid/" + str(n) + "/"

	def set_center(self, value):
		#Sets the center value for the PID output. After adding the Center value, the signal is clamped to Center + Lower Limit and Center + Upper Limit.
		self._daq.set(self._path + "center", value)

	def set_D(self, value):
		#PID derivative gain.
		self._daq.set(self._path + "D", value)

	def get_D(self, value):
		#PID derivative gain.
		return self._daq.get(self._path + "D")

	def set_oscselect(self, enum_):
		#Indicates the signal source which is connected to the chosen input demodulator channel.
		#TODO this enum_ is redundant. -> move it out of the classes
		self._daq.set(self._path + "demod/adcselect", enum_.value)

	def set_harmonic(self, value):
		#Multiplier of the for the reference frequency of the current demodulator.
		self._daq.set(self._path + "demod/harmonic", value)

	def set_oscselect(self, enum_):
		#Selects the filter roll off between 6 dB/oct and 48 dB/oct of the current demodulator.
		#TODO this enum_ is redundant. -> move it out of the classes
		self._daq.set(self._path + "demod/order", enum_.value)

	def set_characteristic_time_constant(self, value):
		#Defines the characteristic time constant (cut off) of the demodulator filter used as an input.
		self._daq.set(self._path + "demod/timeconstant", value)

	def set_D_limit_time_constant(self, value):
		#The cutoff of the low-pass filter for the D limitation given as time constant. When set to 0, the low-pass filter is disabled.
		self._daq.set(self._path + "dlimittimeconstant", value)

	def enable_PID(self, value):
		#Enable the PID controller.
		self._daq.set(self._path + "enable", 0)

	def disable_PID(self, value):
		#Disable the PID controller.
		self._daq.set(self._path + "enable", 1)

	def get_error_value(self, value):
		#Error = Set point - PID Input.
		return self._daq.get(self._path + "error")

	def set_I(self, value):
		#PID integral gain I.
		self._daq.set(self._path + "I", value)

	def get_I(self, value):
		#PID integral gain I.
		return self._daq.get(self._path + "I", value)

	def set_input(self, enum_):
		#Select input source of PID controller.
		self._daq.set(self._path + "input", enum_.value)

	class PID_Input(Enum):
		demod_x = 0
		demod_y = 1
		demod_r = 2
		demod_theta = 3
		auxin = 4
		auxout = 5

	def set_input_channel(self, value):
		#Select input channel of PID controller.
		self._daq.set(self._path + "inputchannel", value)

	def enable_keep_integral_error(self, ):
		#If enabled, the accumulated integral error is maintained upon restart of the PID. If is disabled, the integral error is set to zero when the PID is disabled.
		self._daq.set(self._path + "keepint", 0)

	def disable_keep_integral_error(self, ):
		#If disabled, , the integral error is set to zero.
		self._daq.set(self._path + "keepint", 1)

	def set_lower_limit(self, value):
		#Sets the lower limit for the PID output. After adding the Center value, the signal is clamped to Center + Lower Limit and Center + Upper Limit.
		self._daq.set(self._path + "limitlower", value)

	def set_upper_limit(self, value):
		#Sets the upper limit for the PID output. After adding the Center value, the signal is clamped to Center + Lower Limit and Center + Upper Limit.
		self._daq.set(self._path + "limitupper", value)

	def set_PID_mode(self, enum_):
		#Sets the operation mode of the PID module.
		self._daq.set(self._path + "mode", enum_.value)

	class PID_Mode(Enum):
		pid = 0
		pll = 1
		extref = 2

	def set_output(self, enum_):
		#Select output of the PID controller.
		self._daq.set(self._path + "output", enum_.value)

	class Output(Enum):
		signal_output = 0
		oscillator_frequency = 1
		demod_phase = 2 
		auxout_offset = 3
		sigout_offset = 4

	def set_output_channel(self, value):
		#Select the output channel of the driven output of PID controller.
		self._daq.set(self._path + "outputchannel", value)

	def set_P(self, value):
		#PID Proportional gain P.
		self._daq.set(self._path + "p", value)

	def get_P(self, ):
		#PID Proportional gain P.
		return self._daq.get(self._path + "p")

	def enable_phase_unwrap(self, ):
		#Enables the phase unwrapping to track phase errors past the +/-180 degree boundary and increase PLL bandwidth.
		self._daq.set(self._path + "phaseunwrap", 0)

	def disable_phase_unwrap(self, ):
		#Disables the phase unwrapping.
		self._daq.set(self._path + "phaseunwrap", 1)

	def set_PLL_automode(self, enum_):
		#This defines the type of automatic adaptation of parameters in the PID.
		self._daq.set(self._path + "pll/automode", enum_.value)

	class PLL_automode(Enum):
		no_adaption = 0 
		pid_coeffs = 1
		pid_coeffs_filter_low_bw = 2 
		pid_coeffs_filter_high_bw = 3 
		pid_all = 4 

	def get_PLL_is_locked(self, ):
		#Indicates when the PID, configured as PLL, is locked.
		return self._daq.get(self._path + "pll/locked")

	def set_PID_sampling_rate(self, value):
		# PID sampling rate and update rate of PID outputs. Needs to be set substantially higher than the targeted loop filter bandwidth.
		self._daq.set(self._path + "rate", value)

	def set_PID_setpoint(self, value):
		# PID controller setpoint.
		self._daq.set(self._path + "setpoint", value)

	def enable_setpoint_toggle(self, ):
		#Enables the setpoint toggle.
		self._daq.set(self._path + "setpointtoggle/enable", 0)

	def disable_setpoint_toggle(self, ):
		#Disables the setpoint toggle.
		self._daq.set(self._path + "setpointtoggle/enable", 1)

	def set_setpoint_rate(self, value):
		# Defines the rate of setpoint toggling. Note that possible values are logarithmically spaced with a factor of 4 between values.
		self._daq.set(self._path + "setpointtoggle/rate", value)

	def set_setpoint_used_for_toggle(self, value):
		# Defines the setpoint value used for setpoint toggle.
		self._daq.set(self._path + "setpointtoggle/setpoint", value)

	def get_error_shift(self, value):
		# Difference between the current output value Out and the Center. Shift = P*Error + I*Int(Error, dt) + D*dError/dt
		return self._daq.set(self._path + "shift")

	def get_stream_rate(self, value):
		# Current rate of the PID stream data sent to PC. Defined based on Max Rate.
		return self._daq.set(self._path + "stream/effectiverate")

	def get_stream_error(self, ):
		# PID Error = Set point - PID Input.
		return self._daq.get(self._path + "stream/error")

	def get_stream_is_overflowing(self, ):
		# Indicates the streaming fifo overflow state. True = overflow, False = OK.
		return self._daq.get(self._path + "stream/overflow") == 1

	def set_stream_rate(self, value):
		# Target Rate for PID output data sent to PC. This value defines the applied decimation for sending data to the PC. It does not affect any other place where PID data are used.
		self._daq.set(self._path + "stream/rate", value)

	def get_stream_shift(self, ):
		# Gives the difference between the current output value and the center value. Shift = P*Error + I*Int(Error, dt) + D*dError/dt
		return self._daq.get(self._path + "stream/shift")

	def get_stream_value(self, ):
		# Gives the current PID output value.
		return self._daq.get(self._path + "stream/value")

	def get_PID_value(self, ):
		# Gives the current PID output value.
		return self._daq.get(self._path + "value")


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


class Demodulator():
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

class Sweeper():
	def __init__(self, daq, dev_id) -> None:
		self._daq = daq
		self._path = dev_id + "/sweeper/"

	def set_device(self, device):
		self._daq.set(self._path + "device/", device)

	# TODO this is not how it works...
	def sweep_frequency(self):
		self._daq.set(self._path + "gridnode/",) # set the node path here... )

	def set_start_value(self, value):
		self._daq.set(self._path + "start/", value)

	def set_stop_value(self, value):
		self._daq.set(self._path + "stop/", value)

	def set_samplecount(self, value):
		self._daq.set(self._path + "samplecount/", value)

	def set_scan_mode(self, enum_):
		self._daq.set(self._path + "scan/", enum_.value())
	
	class ScanMode(Enum):
		sequential = 0
		#TODO
