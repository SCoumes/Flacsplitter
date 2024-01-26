import os
import numpy as np
import soundfile as sf
from src import trackSplitter
from src import patternReader

def test_patternReader():
    match = patternReader.readLine("%mm : %ss - %tt", "2 : 35 - TrackName Hello")
    assert match["%tt"] == "TrackName Hello"
    assert match["%mm"] == "2"
    assert match["%ss"] == "35"

def test_readPattern():
    listVariables = patternReader.findVariablesOrder("%mm : %ss - %tt")
    assert listVariables == ["%mm", "%ss", "%tt"]

def test_linesToTracks():
    pattern = "%mm : %ss - %tt"
    lines = ["0 : 00 - TrackName Hello", "1 : 20 - TrackName World"]
    totalRuntime = 180000

    tracks = patternReader.linesToTracks(pattern, lines, totalRuntime)

    assert len(tracks) == 2

    assert tracks[0].number == 1
    assert tracks[0].beginning == 0
    assert tracks[0].end == 80000
    assert tracks[0].name == "TrackName Hello"

    assert tracks[1].number == 2
    assert tracks[1].beginning == 80000
    assert tracks[1].end == 180000
    assert tracks[1].name == "TrackName World"

def test_splitTracks():
    pattern = "%mm : %ss - %tt"
    timeCodes = "0 : 00 - TrackName Hello\n1 : 20 - TrackName World"

    project_root: str = os.path.abspath('.')

    mainFileLocation = os.path.join(project_root, "test", "testfiles", "specialTest.flac")
    # Create a temporary directory for test output
    tempDir = os.path.join(project_root, "test", "testfiles")

    # Create a mock FLAC file
    data = np.zeros(44100)  # Mock audio data
    sr = 44100  # Mock sample rate
    sf.write(mainFileLocation, data, sr)

    # Call the function under test
    trackSplitter.splitTracks(pattern, timeCodes, mainFileLocation)

    # Assert that the tracks are split and saved correctly
    assert os.path.exists(os.path.join(tempDir, "01 - TrackName Hello.flac"))
    assert os.path.exists(os.path.join(tempDir, "02 - TrackName World.flac"))
