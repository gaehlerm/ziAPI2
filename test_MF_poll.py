import time

from test_util import *
from MF import *
from GHF import *

def test_MF_poll():	
	# Example from the Labone Programming manual, p.43
	daq = NodeLogDAQ()
	# Enable the demodulator output and set the transfer rate.
	# This ensure the device actually pushes data to the Data Server.
	mf = MF(daq, "dev2006")
	demods = [0,4]
	for i in demods:
		mf.demods[i].enable()
		mf.demods[i].set_rate(10e3)
		mf.demods[i].sample.subscribe()

	time.sleep(0.001) # Subscribed data is being accumulated by the Data Server.
	data = daq.poll(0.020, 10, 0, True)

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
	daq.poll(6, 500, flat=True)
	
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
	# Is it a GHF sweeper or a DAQ sweeper?
	sweeper = ghf.sweeper
	
    # Specify the frequency of the oscillator should be swept.
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
	print(node_log)
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



