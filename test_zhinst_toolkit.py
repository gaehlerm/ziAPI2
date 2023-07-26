from dataclasses import dataclass
import time

from MF import *

@dataclass
class NodeLogLine:
    Operation: str
    Node: str
    Value: float | str

class NodeLogDAQ:
	def __init__(self):
		self._node_log = []
    
	def set(self, node, value):
		self._node_log.append(NodeLogLine("set", node, value))

	def get(self, node, value):
		self._node_log.append(NodeLogLine("get", node, ""))
	
	def poll(self, *args, **kwargs):
		self._node_log.append(NodeLogLine("poll", "", ""))
	
	def subscribe(self, node):
		self._node_log.append(NodeLogLine("subscribe", node, ''))

	def get_node_log(self):
		return self._node_log

def test_MF_poll():	
	daq = NodeLogDAQ()
	# Enable the demodulator output and set the transfer rate.
	# This ensure the device actually pushes data to the Data Server.
	mf = MF(daq, "/dev2006")
	demods = [0,4]
	for i in demods:
		mf.demods[i].enable()
		mf.demods[i].set_rate(10e3)
		mf.demods[i].sample.subscribe()

	time.sleep(0.001) # Subscribed data is being accumulated by the Data Server.
	data = daq.poll(0.020, 10, 0, True)

	node_log = daq.get_node_log()
	assert NodeLogLine("set", '/dev2006/demods/0/enable', 1) in node_log
	assert NodeLogLine("set", '/dev2006/demods/0/rate', 10e3) in node_log
	assert NodeLogLine("subscribe", '/dev2006/demods/0/sample', '') in node_log
	assert NodeLogLine("set", '/dev2006/demods/4/enable', 1) in node_log
	assert NodeLogLine("set", '/dev2006/demods/4/rate', 10e3) in node_log
	assert NodeLogLine("subscribe", '/dev2006/demods/4/sample', '') in node_log
	assert NodeLogLine("poll", '', '') in node_log
