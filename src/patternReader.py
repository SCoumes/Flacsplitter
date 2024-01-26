from typing import Tuple, List, Dict
from src.objects import Track
import re

def findVariablesOrder(pattern) -> List[str]:
    """Receive a pattern and return the order in which %hh, %dd, %ss, and/or %tt are found in it. 
    @param pattern : The pattern to be read. For example "%mm : %ss - %tt" is a valid pattern.
    @return : A list containing the order in which the variables are found. For example, the return value for the example pattern above would be ["%mm", "%ss", "%tt"].
    """
    variables = ["%hh", "%mm", "%ss", "%tt"]
    found = re.findall("%\w\w", pattern)
    return [variable for variable in found if variable in variables]

def readLine(pattern : str, line : str) -> Dict[str, str]:
    """
    Reads a line of text and returns a list of matches for the given regular expression.
    @param pattern: Contains "%ss", "%tt", and/or "%mm" which need to be found in the line. For example "%mm : %ss - %tt" is a valid pattern. We further assume that each of the variables appears at most once in the pattern.
    @param line: The line of text to be read. Should match the pattern. For example "2 : 35 - TrackName" would be a valid line matching the example pattern above. 
    @return: A dict containing the matches for the variables. For example, the return value for the example pattern and line above would be {"%tt" : "TrackName", "%mm" : "2", "%ss" : 35).
    """
    variables = findVariablesOrder(pattern)
    for var in variables:
        pattern = pattern.replace(var, "(.*)")
    matches = re.findall(pattern, line)
    if not matches :
        raise Exception("No match found.")
    matching = dict()
    for i, var in enumerate(variables):
        matching.update({var : matches[0][i]})
    return matching
    
def linesToTracks(pattern, lines : List[str], totalRuntime : int) -> List[Track]:
    times = []
    names = []

    for line in lines:
        matching = readLine(pattern, line)

        time = 0
        if "%hh" in matching:
            time += int(matching["%hh"]) * 3600
        if "%mm" in matching:
            time += int(matching["%mm"]) * 60
        if "%ss" in matching:
            time += int(matching["%ss"])
        time *= 1000 # Convert to milliseconds
        times.append(time)

        if "%tt" in matching:
            name = matching["%tt"]
        else:
            name = "Unknown Title"
        names.append(name)
    times.append(totalRuntime)

    tracks = []
    for i, name in enumerate(names):
        tracks.append(Track(i+1, times[i], times[i+1], name))
    for t in tracks:
        print(t)
    return tracks

    

