from dataclasses import dataclass

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

	def get(self, node):
		self._node_log.append(NodeLogLine("get", node, ""))
    
	def get_as_event(self, node):
		self._node_log.append(NodeLogLine("get_as_event", node, ""))
	
	def poll(self, *args, **kwargs):
		self._node_log.append(NodeLogLine("poll", "", ""))
	
	def subscribe(self, node):
		self._node_log.append(NodeLogLine("subscribe", node, ''))

	def get_node_log(self):
		return self._node_log
