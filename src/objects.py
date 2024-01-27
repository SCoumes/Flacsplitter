# Classes for communication between functions.
from typing import Optional

class Track:
    number: int # The track number
    beginning: int # The beginning of the track in milliseconds
    end: int # The end of the track in milliseconds
    name: str # The name of the track

    def __init__(self, number: int, beginning: int, end: int, name: str):
        self.number = number
        self.beginning = beginning
        self.end = end
        self.name = name

    def getPaddedNumber(self) -> str:
        return str(self.number).zfill(2)
    
    def __str__(self) -> str:
        return "[" + str(self.number) + " " + str(self.beginning) + " " + str(self.end) + " " + self.name + "]"

class SharedMeta:
    """A class for the metadata shared by all tracks."""
    year: Optional[int]
    album: Optional[str]
    artist: Optional[str]
    genre: Optional[str]

    def __init__(self, year: Optional[int] = None, album: Optional[str] = None, artist: Optional[str] = None, genre: Optional[str] = None) -> None:
        self.year = year
        self.album = album
        self.artist = artist
        self.genre = genre
        

class PatternError(Exception):
    """An exception raised when the pattern is invalid."""
    pass