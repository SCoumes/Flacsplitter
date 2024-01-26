import sys
import os
import time
import numpy as np
import soundfile as sf
from typing import Tuple

from src.objects import Track
from src import patternReader

def extractTrack(data : np.ndarray, sr : int, track : Track) -> np.ndarray:
    """
    Extracts the audio data for a given track.
    @param data : The audio data.
    @param sr : The sample rate of the audio data.
    @param track : The track to extract.
    @return : A tuple containing the extracted audio data and the sample rate of the extracted data.
    """
    start: int = int(track.beginning / 1000 * sr)
    end: int = int(track.end / 1000 * sr)
    return data[start:end]

def splitTracks(pattern : str, timeCodes : str, mainFileLocation : str) -> None:
    """Split the audio file into tracks and write them to disk.
    @param pattern : The pattern to be read. For example "%mm : %ss - %tt" is a valid pattern.
    @param timeCodes : The time codes for the tracks as a single string with one track per line. For example, "2 : 35 - TrackName" would be a valid line matching the example pattern above.
    @param mainFileLocation : The location of the main file to split. For example "C:/Users/Me/Music/Album.flac".
    @return : None
    """
    data: np.ndarray
    sr: int
    data, sr = sf.read(mainFileLocation)

    lines = timeCodes.splitlines()
    totalRuntime = int(len(data) * 1000 / sr)
    tracks = patternReader.linesToTracks(pattern, lines, totalRuntime)

    for track in tracks:
        trackData = extractTrack(data, sr, track)
        fileName = track.getPaddedNumber() + " - " + track.name + ".flac"
        filePath = os.path.join(os.path.dirname(mainFileLocation), fileName)
        sf.write(filePath, trackData, sr)
