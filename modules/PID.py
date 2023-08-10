
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