import csv

class Pelicula:
    def __init__(self, showid, type, title, director, cast_members, country, date_added, release_year, rating, duration, listed_in, description):
        self._showid = showid
        self._type = type#*
        self._title = title
        self._director = director
        self._cast = cast_members.split(", ")
        self._country = country.split(", ")
        self._date_added = date_added#*
        self._release_year = release_year
        self._rating = rating#*
        self._duration = duration
        self._listed_in = listed_in.split(", ")#*
        self._description = description

    @property
    def showid(self):
        return self._showid

    @property
    def type(self):
        return self._type

    @property
    def title(self):
        return self._title

    @property
    def director(self):
        return self._director

    @property
    def cast_members(self):
        return ", ".join(self._cast)

    @property
    def country(self):
        return self._country

    @property
    def date_added(self):
        return self._date_added

    @property
    def release_year(self):
        return self._release_year

    @property
    def rating(self):
        return self._rating

    @property
    def duration(self):
        return self._duration

    @property
    def listed_in(self):
        return ", ".join(self._listed_in)

    @property
    def description(self):
        return self._description

    @showid.setter
    def showid(self, value):
        self._showid = value

    @type.setter
    def type(self, value):
        self._type = value

    @title.setter
    def title(self, value):
        self._title = value

    @director.setter
    def director(self, value):
        self._director = value

    @cast_members.setter
    def cast_members(self, value):
        self._cast = value.split(", ")

    @country.setter
    def country(self, value):
        self._country = value

    @date_added.setter
    def date_added(self, value):
        self._date_added = value

    @release_year.setter
    def release_year(self, value):
        self._release_year = value

    @rating.setter
    def rating(self, value):
        self._rating = value

    @duration.setter
    def duration(self, value):
        self._duration = value

    @listed_in.setter
    def listed_in(self, value):
        self._listed_in = value.split(", ")

    @description.setter
    def description(self, value):
        self._description = value

