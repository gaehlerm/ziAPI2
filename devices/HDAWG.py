from ziAPI2 import *

from modules.Sweeper import Sweeper 
from modules.Precompensation import Precompensation
from devices.DeviceComponents import *


class HDAWG():
    	#add some docstring?

    def __init__(self, daq, dev_id):
        # TODO: just copied from the GHF. Should be adapted to HD.

        # self._options = daq.get() #what is the node for the device options?

        # not yet implemented:
        # self.about = About(daq) # classes sorted by the order in the programming manual
        # self.zi = Zi(daq)
        # self.config = Config(daq)
        # self.debug = Debug(daq)
        self.system = System(daq, dev_id)
        self.status = Status(daq, dev_id)

        # is devices a list of Device?
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

        # add all modules
        self.precompensation = Precompensation(daq, dev_id)
        self.sweeper = Sweeper(daq, dev_id)

        # self.signal_input_1 = SignalInput(daq, dev_id, 0)
        # self.signal_input_2 = SignalInput(daq, dev_id, 1)
        #add all other modules
