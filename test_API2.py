# Copyright Marco Gähler

import time

from test_util import *
from MF import *
from GHF import *
from HDAWG import *

# TODO The node paths are not always correct. This has to be fixed for the final implementation.

def test_MF_poll():	
	# Example from the Labone Programming manual, p.43
	daq = NodeLogDAQ()
	# Enable the demodulator output and set the transfer rate.
	mf = MF(daq, "dev2006")
	demods = [0,4]
	for i in demods:
		mf.demods[i].enable()
		mf.demods[i].set_rate(10e3)
		mf.demods[i].sample.subscribe()

	_ = daq.poll(0.020, 10, 0, True)

	node_log = daq.get_node_log()
	assert NodeLogLine("set", 'dev2006/demods/0/enable', 1) in node_log
	assert NodeLogLine("set", 'dev2006/demods/0/rate', 10e3) in node_log
	assert NodeLogLine("subscribe", 'dev2006/demods/0/sample', '') in node_log
	assert NodeLogLine("set", 'dev2006/demods/4/enable', 1) in node_log
	assert NodeLogLine("set", 'dev2006/demods/4/rate', 10e3) in node_log
	assert NodeLogLine("subscribe", 'dev2006/demods/4/sample', '') in node_log
	assert NodeLogLine("poll", '', '') in node_log


def test_GHF_poll():
	# example from labone API examples, GHF example_poll
	daq = NodeLogDAQ()
	ghf = GHF(daq, "dev1234")
	ghf.demods[0].enable()
	ghf.demods[0].set_rate(2000)
	ghf.demods[0].set_trigger_mode(Demod.TriggerMode.continuous)
	_ = ghf.system.get_timebase()
	_ = ghf.status.get_current_timestamp()

	ghf.demods[0].sample.subscribe()
	_ = daq.poll(6, 500, flat=True)
	
	node_log = daq.get_node_log()
	assert NodeLogLine("set", 'dev1234/demods/0/enable', 1) in node_log
	assert NodeLogLine("set", 'dev1234/demods/0/rate', 2000) in node_log
	assert NodeLogLine("set", 'dev1234/demods/0/trigger/triggeracq', 0) in node_log
	assert NodeLogLine("get", 'dev1234/system/properties/timebase', '') in node_log
	assert NodeLogLine("get", 'dev1234/status/time', '') in node_log
	assert NodeLogLine("subscribe", 'dev1234/demods/0/sample', '') in node_log
	assert NodeLogLine("poll", '', '') in node_log

def test_GHF_sweeper():
	# Example from https://github.com/zhinst/labone-api-examples/blob/release-23.06/ghfli/python/example_sweeper.py
	daq = NodeLogDAQ()
	ghf = GHF(daq, "dev1234")
	# TODO: Is it a GHF sweeper or a DAQ sweeper? Implementing it as a daq.sweeper would be difficult.
	sweeper = ghf.sweeper
	
	sweeper.sweep_parameter(ghf.oscs[0].frequency)

	sweeper.set_start_value(100)
	sweeper.set_stop_value(1000)
	sweeper.set_samplecount(50)
	sweeper.set_scan_mode(Sweeper.ScanMode.sequential)
	sweeper.set_sequence_mode(Sweeper.SequenceMode.linear)
	sweeper.set_max_bandwidth(333)

    # Now subscribe to the nodes from which data will be recorded.
	ghf.demods[0].sample.subscribe()
	
	node_log = daq.get_node_log()
	assert NodeLogLine('set', 'dev1234/sweeper/device/', 'dev1234') in node_log
	assert NodeLogLine('set', 'dev1234/sweeper/gridnode/', 'dev1234/oscs/0/frequency') in node_log
	assert NodeLogLine('set', 'dev1234/sweeper/start/', 100) in node_log
	assert NodeLogLine('set', 'dev1234/sweeper/stop/', 1000) in node_log
	assert NodeLogLine('set', 'dev1234/sweeper/samplecount/', 50) in node_log
	assert NodeLogLine('set', 'dev1234/sweeper/samplecount/', 50) in node_log
	assert NodeLogLine('set', 'dev1234/sweeper/scan/', 0) in node_log
	assert NodeLogLine('set', 'dev1234/sweeper/xmapping/', 0) in node_log
	assert NodeLogLine('set', 'dev1234/sweeper/maxbandwidth/', 333) in node_log  
	assert NodeLogLine('subscribe', 'dev1234/demods/0/sample', '') in node_log  

def test_GHF_triggered_data_acquisition():
	#https://github.com/zhinst/labone-api-examples/blob/release-23.06/ghfli/python/example_triggered_data_acquisition.py
	daq = NodeLogDAQ()
	ghf = GHF(daq, "dev1234")
	d0 = ghf.demods[0]

	d0.set_trigger_source(Demod.TriggerSource.software_trigger)
	d0.enable_triggered_acquisition()
	d0.set_burst_length(256)
	d0.set_data_rate(2048)
	d0.enable()
	_ = ghf.system.get_timebase()
	d0.sample.subscribe()
	ghf.system.set_software_trigger()
	_ = daq.poll(0.020, 10, 0, True)
	daq.unsubscribe_all()

	node_log = daq.get_node_log()
	assert NodeLogLine('set', 'dev1234/demods/0/trigger/source', 1024) in node_log
	assert NodeLogLine('set', 'dev1234/demods/0/trigger/triggeracq', 1) in node_log
	assert NodeLogLine('set', 'dev1234/demods/0/burstlen', 256) in node_log
	assert NodeLogLine('set', 'dev1234/demods/0/rate', 2048) in node_log
	assert NodeLogLine('set', 'dev1234/demods/0/enable', 1) in node_log
	assert NodeLogLine('get', 'dev1234/system/properties/timebase', '') in node_log
	assert NodeLogLine('subscribe', 'dev1234/demods/0/sample', '') in node_log
	assert NodeLogLine('set', 'dev1234/system/properties/swtriggers/0/single', 1) in node_log
	assert NodeLogLine("poll", '', '') in node_log
	assert NodeLogLine("unsubscribe", '*', '') in node_log

def test_HD_Commandtable():
	# source: https://github.com/zhinst/labone-api-examples/blob/release-23.06/hdawg/python/example_awg_commandtable.ipynb
	daq = NodeLogDAQ()
	hd = HDAWG(daq, "dev8047")

	# TODO how to make a syncSetInt? call sync before wait_for_state_change?
	hd.system.load_preset()
	# TODO how does this command work exactly?
	hd.system.wait_for_state_change(0, timeout=2.0)
	
	node_log = daq.get_node_log()
	print(node_log)
	assert NodeLogLine('set', 'dev8047/system/properties/preset/load', 1) in node_log
	assert NodeLogLine('set', 'dev8047/system/properties/preset/busy', 1) in node_log

def test_HD_precompensation():
	# source: https://github.com/zhinst/labone-api-examples/blob/release-23.06/hdawg/python/example_precompensation_curve_fit.py
	daq = NodeLogDAQ()
	hd = HDAWG(daq, "dev8047")
	pre = hd.precompensation
	pre.exponentials[0].enable()
	pre.wave.input.set_source(3) # TODO use an enum here? Or what's the value 3?
	hd.system.clock.set_sampling_rate(2.4e9)
	_ = pre.get_sampling_rate()

	node_log = daq.get_node_log()
	print(node_log)
	assert NodeLogLine('set', 'dev8047/exponentials/0/enable', 1) in node_log
	assert NodeLogLine('set', 'dev8047/wave/input/source', 3) in node_log
	assert NodeLogLine('set', 'dev8047/system/properties/clocks/sampleclock/freq', 2.4e9) in node_log
	assert NodeLogLine('get', 'dev8047/samplingfreq', '') in node_log

