from ziAPI2 import *
from modules.Scope import Scope
from modules.Sweeper import Sweeper
from devices.DeviceComponents import *


class MF():
	#add some docstring?

    def __init__(self, daq, dev_id):
        # self._options = daq.get() #what is the node for the device options?

        # not yet implemented:
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

        # how many currins are there for the MF?
        self.currin1 = Currin(daq, dev_id, 0)
        self.currin2 = Currin(daq, dev_id, 1)

        #figure out how to deal with the 0/1 index problem
        self.demods = [Demod(daq, dev_id, i) for i in range(8)]

        # The modules are not really part of the device, but it's the easiest to treat them this way.
        self.scope = Scope(daq, dev_id, 0) # does scope need an indice?
        self.sweeper = Sweeper(daq, dev_id)

        # self.signal_input_1 = SignalInput(daq, dev_id, 0)
        # self.signal_input_2 = SignalInput(daq, dev_id, 1)
        #add all other modules

