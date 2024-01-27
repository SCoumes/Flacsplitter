from typing import Tuple, List, Dict
from src.objects import Track, PatternError
import re

def patternToRegex(pattern :str) -> re.Pattern:
    """
    Convert a pattern following the "in house" format to a regex object.
    @param pattern: The pattern to convert
    @return: A matching regex object
    """
    regex : str = pattern
    regex = regex.replace(" ", "\\s")
    regex = regex.replace("[", "\\[")
    regex = regex.replace("]", "\\]")
    regex = regex.replace("(", "\\(")
    regex = regex.replace(")", "\\)")
    regex = regex.replace(".","\\.")
    regex = regex.replace("?","\\?")
    regex = regex.replace("|","\\|")
    regex = regex.replace("%hh", "(?P<hh>\\d+)")
    regex = regex.replace("%mm", "(?P<mm>\\d+)")
    regex = regex.replace("%ss", "(?P<ss>\\d+)")
    regex = regex.replace("%tt", "(?P<tt>.*)")
    regex = regex.replace("%ii", ".*")
    return re.compile(regex)
    
def linesToTracks(pattern, lines : List[str], totalRuntime : int) -> List[Track]:
    times = []
    names = []

    regex : re.Pattern = patternToRegex(pattern)

    for line in lines:
        line = line.strip()
        try:
            matching = re.fullmatch(regex, line).groupdict()
        except AttributeError:
            raise PatternError(f"Pattern {pattern} does not match line {line}")

        """
        Pattern nomenclature: 
            %hh : Hours
            %mm : Minutes
            %ss : Seconds
            %tt : Track name
            %ii : Ignore
        """
        time = 0
        if "hh" in matching:
            time += int(matching["hh"]) * 3600
        if "mm" in matching:
            time += int(matching["mm"]) * 60
        if "ss" in matching:
            time += int(matching["ss"])
        time *= 1000 # Convert to milliseconds
        times.append(time)

        if "tt" in matching:
            name = matching["tt"]
        else:
            name = "Unknown Title"
        names.append(name)
    times.append(totalRuntime)

    tracks = []
    for i, name in enumerate(names):
        tracks.append(Track(i+1, times[i], times[i+1], name))
    return tracks

    

