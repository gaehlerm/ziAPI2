from enum import Enum

class Impedance():
	def  __init__(self, daq, dev_id, n):
		self._daq = daq
		self._path = dev_id + "/imps/" + str(n) + "/"

	def set_AC(self, value):
		# Defines the input coupling for the Signal Inputs. AC coupling inserts a high-pass filter.
		#TODO how does this node work?
		self._daq.set(self._path + "ac", value)

	def enable_automatic_bandwidth_control(self, ):
		# Enable automatic bandwidth control. If enabled the optimum bandwidth is calculated based on the frequency and measurement data.
		#TODO disabling function? value?
		self._daq.set(self._path + "auto/bw", 0)

	def set_input_range_control_mode(self, enum_):
		# Select input range control mode.
		self._daq.set(self._path + "auto/inputrange", enum_.value)

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
		# TODO is the 0/1 here correct? And what is the node name?
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
		self._daq.set(self._path + "current/inputselect", enum_.value)

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

	class Interpolation(Enum):
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
		self._daq.set(self._path + "model", enum_.value)

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
		self._daq.set(self._path + "output/select", enum_.value)

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
		self._daq.set(self._path + "voltage/inputselect", enum_.value)

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
