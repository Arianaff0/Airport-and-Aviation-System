#Airport class
class Airport:
    # method which has instance variables--> ex, self._code = code
    # and parameters (self, code, city country, continent)
    def __init__(self, code, city, country, continent):
        self._code = code
        self._city = city
        self._country = country
        self._continent = continent
# repr is a method that shows how you want to display your variables in str format.
    def __repr__(self):
        return f"{self._code} ({self._city}, {self._country})"
# getters
    def getCode(self):
        return self._code

    def getCity(self):
        return self._city

    def getCountry(self):
        return self._country

    def getContinent(self):
        return self._continent
# setters
    def setCity(self, city):
        self._city = city

    def setCountry(self, country):
        self._country = country

    def setContinent(self, continent):
        self._continent = continent



