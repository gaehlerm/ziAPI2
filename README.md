# ziAPI2

This is a wrapper for the Zurich Instruments python API. 

Open questions:
- How to deal with the subscribe and sweep nodes? Do I have to implement these functions for all (double) nodes or only some specific ones?
- Try the code on a real device. There are no integration tests so far, only the unit tests unsing the fake node logger.
- Implement all devices.
- Should the modules be part of the device? I think this is the easiest solution.
