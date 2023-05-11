from Airport import*
# Flight class, I imported Airport because it uses Airport objects.
class Flight:
    # __init__ with instance variables and parameters
    def __init__(self, flightNo, origAirport, destAirport):
        # if the origAirport and destAirport are not airport objects, raises a Type Error.
        if not isinstance(origAirport, Airport) or not isinstance(destAirport, Airport):
            raise TypeError("The origin and destination must be Airport objects")
        # if the flightNo is a 6-characters long, containing 3 letters followed by 3 digits, raises Type Error.
        if not isinstance(flightNo, str) or len(flightNo) != 6 or not flightNo[:3].isalpha() or not flightNo[3:].isdigit():
            raise TypeError("The flight number format is incorrect")

        self._flightNo = flightNo
        self._origin = origAirport
        self._destination = destAirport

# return representation of Flight in a specific format, local is an empty str, if self.isDomesticFlight()
# then the local str is domestic. the isDomesticFlight method has more information on the 'requirements'
# for the if statement to be true.
    def __repr__(self):
        local = ""
        if self.isDomesticFlight():
            local = "domestic"
        else:
            local = "international"
        return f"Flight({self._flightNo}): {self._origin.getCity()} -> {self._destination.getCity()} [{local}]"

# method that returns True if self and other flights are considered the same flight. Essentially, if other is a
# flight object then self._destination equals other.getDestination. Otherwise, it returns False.
    def __eq__(self, other):
        if isinstance(other, Flight):
            if self._destination == other.getDestination() and self._origin == other.getOrigin():
                return True
        return False

# getters for Flight class
    def getFlightNumber(self):
        return self._flightNo

    def getOrigin(self):
        return self._origin

    def getDestination(self):
        return self._destination
# previously mentioned, the isDomesticFlight method, returns True if the flight is domestic(same country),
# returns False if the flight is international. So this method just means that the origin and destination is
# in same country(domestic) but to return False, just say "if not" this method or "else:" like itself does not return
# True or False
    def isDomesticFlight(self):
        return self._origin.getCountry() == self._destination.getCountry()
#setters
    def setOrigin(self, origin):
        self._origin = origin

    def setDestination(self, destination):
        self._destination = destination


