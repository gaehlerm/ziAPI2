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
	ghf.system.get_timebase()
	ghf.status.get_current_timestamp()

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

