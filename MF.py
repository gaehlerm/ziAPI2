import zhinst.core
import time
from enum import Enum

from ziAPI import *

class MF():
	#add some docstring?

    def __init__(self, daq, dev_id):
        # self._options = daq.get() #what is the node for the device options?

        # self.about = About(daq) # classes sorted by the order in the programming manual
        # self.zi = Zi(daq)
        # self.config = Config(daq)
        # self.debug = Debug(daq)

        # # is devices a list of Device?
        # self.devices = Devices(daq)
        # self.mds = MDS(daq)
        self.save = Save(daq)

        # from the user manual
        self.auxin1 = AuxIn(daq, dev_id, 0)
        self.auxin2 = AuxIn(daq, dev_id, 1)

        self.auxout1 = AuxOut(daq, dev_id, 0)
        self.auxout2 = AuxOut(daq, dev_id, 1)

        #how many currins are there for the MF?
        self.currin1 = Currin(daq, dev_id, 0)
        self.currin2 = Currin(daq, dev_id, 1)

        self.scope = Scope(daq, dev_id, 0) # does scope need an indices?
        # self.sweeper = Sweeper(daq, dev_id)

        #figure out how to deal with the 0/1 index problem
        self.demods = [Demod(daq, dev_id, i) for i in range(8)]

        # self.signal_input_1 = SignalInput(daq, dev_id, 0)
        # self.signal_input_2 = SignalInput(daq, dev_id, 1)
        #add all other modules


# # example from the LabOne Programming manual p.41
# # add default values here. They are usually the same.
# daq = zhinst.core.ziDAQServer('localhost', 8004, 6)

# MF2006 = MF(daq, "dev2006")
# demod0 = MF2006.demods[0]
# demod0.enable()
# demod0.set_rate(10e3)
# #for set, subscribe and get_as_event we each need one function. This becomes a bit tedious.
# demod0.subscribe_sample()
# #demod0.get_sample_as_event()
# time.sleep(1)
# #allow keywords, set the boolean to true by default
# data = daq.poll(0.02, 10, 0, True)

# MF.options.set_fileformat()