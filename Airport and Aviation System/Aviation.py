# Developed by: Ariana Feng
# Date: April 07, 2023
# Desc: program that loads text files representing some of the airports and flights around the world
#       and analyzes the flights according to specifications.
# Inputs: Three text files: countries(includes country and continent name), airports(3-letter airport code, country
#         and city in which the airport is located), and flights(6 character flight code, origin airport code,
#         destination airport code).
# Outputs: Test cases include findAllCityFlights, findAllCountryFlights, findFlightBetween, findReturnFlight,
#          findFlightsAcross('Atlantic') and findFlightsAcross('Pacific'). The names are self-explanatory.

# imports from Flight class and Airport class because it creates Airport and flight objects.
from Flight import*
from Airport import*

# Aviation class
class Aviation:
    # instance variables are either an empty list or empty dictionary
    def __init__(self):
        self._allAirports = []
        self._allFlights = {}
        self._allCountries = {}
# setters
    def setAllAirports(self, airports):
        self._allAirports = airports

    def setAllFlights(self, flights):
        self._allFlights = flights

    def setAllCountries(self, countries):
        self._allCountries = countries
# getters
    def getAllAirports(self):
        return self._allAirports

    def getAllFlights(self):
        return self._allFlights

    def getAllCountries(self):
        return self._allCountries

# loadData reads the airport, flight, and countries files.
    def loadData(self, airportFile, flightFile, countriesFile):
        try:
            self._allAirports = []
            self._allFlights = {}
            self._allCountries = {}
            # Read the data from countries file
            f = open(countriesFile, "r", encoding='utf8')
            # for each line in the file, split by commas, and strips blank spaces. country is the key in the
            # allCountries dictionary and its corresponding list is continent. At the end, close the file.
            for line in f:
                countryContinentList = line.split(",")
                country = countryContinentList[0].strip()
                continent = countryContinentList[1].strip()
                self._allCountries[country] = continent
            f.close()

            # Read the data from airport file
            a = open(airportFile, "r", encoding='utf8')
            # basically same thing as other file, for each line in the file, split by commas, and strips blank spaces.
            # code, city, country, and continent are all airport objects, and you append these airport objects to the
            # allAirports list. Close file at the end.
            for line in a:
                airportList = line.split(",")
                code = airportList[0].strip()
                country = airportList[1].strip()
                city = airportList[2].strip()
                continent = self._allCountries[country]
                self._allAirports.append(Airport(code, city, country, continent))
            a.close()

            # Read the data from flight file
            b=open(flightFile, "r", encoding='utf8')
            # for each line in the file, split by commas, and strips blank spaces. For each airport object in the
            # allAirports list, if origCode is same as airport code then variable c is airport... if origCode is not a
            # key, then make the key and have a corresponding empty list. We are appending flight objects, flightNo, c, d
            # which utilizes getters from airport objects. Close file at end.
            for line in b:
                line = line.strip()
                parts = line.split(',')
                flightNo = parts[0].strip()
                origCode = parts[1].strip()
                destCode = parts[2].strip()
                for airport in self._allAirports:
                    if origCode == airport.getCode():
                        c = airport
                    if destCode == airport.getCode():
                        d = airport
                if origCode not in self._allFlights.keys():
                    self._allFlights[origCode] = []
                self._allFlights[origCode].append(Flight(flightNo, c, d))
            b.close()

# except statement return False if there are issues opening or reading these files. Otherwise, returns True.
        except:
            return False
        return True

# returns airport object that has the given code, if no object found that has the code, return -1
    def getAirportByCode(self, code):
        for airport in self._allAirports:
            # print(code,airport.getCode())
            if code == airport.getCode():
                return airport
        return -1

# for each item in the list corresponding to the key in allFlights dictionary, if city is origin or dest
# then you append that flight object to the empty flightObjects list.
    def findAllCityFlights(self, city):
        flightObjects=[]
        for list in self._allFlights.values():
            for flight in list:
                if flight.getOrigin().getCity()== city or flight.getDestination().getCity()== city:
                    flightObjects.append(flight)
        return flightObjects

# returns a flight object with flightNumer equal to flightNo. Returns -1 if not found.
    def findFlightByNo(self, flightNo):
        for list in self._allFlights.values():
            for flight in list:
                if flightNo == flight.getFlightNumber():
                    return flight
        return -1

# kinda same as findAllCityFlights, returns a list that contains all Flight objects that involve the given country
# either as the origin or the destination (or both).
    def findAllCountryFlights(self, country):
        flightObjects=[]
        for list in self._allFlights.values():
            for flight in list:
                if flight.getOrigin().getCountry()== country or flight.getDestination().getCountry()== country:
                    flightObjects.append(flight)
        return flightObjects

# checks if there is a direct flight from origAirport object to destAirport object. Enters for loop
# for each flight in the list. Returns a str.
    def findFlightBetween(self, origAirport, destAirport):
        for list in self._allFlights.values():
            for flight in list:
                if origAirport.getCode() == flight.getOrigin().getCode() and destAirport.getCode() == flight.getDestination().getCode():  #flight.getOrigin() = airport object
                    return f"Direct Flight({flight.getFlightNumber()}): {origAirport.getCode()} to {destAirport.getCode()}"
# empty lists called listOrig and listDest, connectingAirports is a set. Appended all flights with origin code to listOrig list...
# same with all flights with dest code to listDest list. For each flight in listOrig, and for each flight in listDest, if the origin code
# is the same as destination code, add that flight to connectingAirport set.
        listOrig=[]
        listDest=[]
        connectingAirports=set()
        for list in self._allFlights.values():
            for flight in list:
                if flight.getOrigin().getCode() == origAirport.getCode():
                    listOrig.append(flight)
                if flight.getDestination().getCode() == destAirport.getCode():
                    listDest.append(flight)
        for flight in listOrig:
            for flight2 in listDest:
                if flight.getDestination().getCode() == flight2.getOrigin().getCode():
                    connectingAirports.add(flight.getDestination().getCode())
# if length of set is 0, indicating no single-hope connecting flights, return -1
        if len(connectingAirports) == 0:
            return -1
        return connectingAirports

# for each flight, if there is a flight object that goes from orig to dest and dest to origin then you return
# the flight object
    def findReturnFlight(self, firstFlight):   #firstflight is original flight but flight is return flight
        for list in self._allFlights.values():
            for flight in list:
                if flight.getOrigin().getCode() == firstFlight.getDestination().getCode() and flight.getDestination().getCode() == firstFlight.getOrigin().getCode():
                    return flight
        return -1

# Method has ocean name as parameter, the three zones are lists, with its corresponding countries.
    def findFlightsAcross(self, ocean):
        redZ = ["Asia", "Australia"]
        greenZ = ["North America", "South America"]
        blueZ = ["Africa", "Europe"]
        codes = set()

# for each flight in the list, if the flight crosses the Pacific, the origin is from a greenz and dest is red, and vice versa.
        for list in self._allFlights.values():
            for flight in list:
                if ocean == "Pacific":
                    if (flight.getOrigin().getContinent() in redZ and flight.getDestination().getContinent() in greenZ) \
                            or (flight.getOrigin().getContinent() in greenZ and flight.getDestination().getContinent() in redZ):
# if the flight crosses that ocean, add the flight number to the codes set. Same for the Atlantic ocean, for loops and add to set.
                        codes.add(flight.getFlightNumber())
                elif ocean == "Atlantic":
                    if (flight.getOrigin().getContinent() in greenZ and flight.getDestination().getContinent() in blueZ) \
                            or (flight.getOrigin().getContinent() in blueZ and flight.getDestination().getContinent() in greenZ):
                        codes.add(flight.getFlightNumber())
# if there is no flight code that crosses the Pacific or Atlantic, length of set will be 0 and returns -1.
        if len(codes) == 0:
            return -1
        return codes







