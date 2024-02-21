class LengthConverter:
    def __init__(self):
        self.__distance_in_meter = 0
    
    @property
    def meter(self):
        return self.__distance_in_meter
    
    @meter.setter
    def meter(self, value):
        self.__distance_in_meter = value

    @property
    def feet(self):
        return self.__distance_in_meter * 3.2808399
    
    @feet.setter
    def feet(self, value):
        self.__distance_in_meter = value / 3.2808399
    
    @property
    def inch(self):
        return self.__distance_in_meter * 39.3700787
    
    @inch.setter
    def inch(self, value):
        self.__distance_in_meter = value / 39.3700787

converter = LengthConverter()
converter.meter = 100
converter.feet = 5
print(converter.inch)

