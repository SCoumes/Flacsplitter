This software can be used to split a single .flac audio file into multiple flac files corresponding to individual tracks. 
You must provide timecodes of the begining of the tracks (presumably the first track starts at 0:00), along with their names.
This software allows some leeway in the format in which you provide the timecodes, as you can introduce your own "pattern", which will be used to read the timecodes.
A pattern is written like a line that gives a timecode and the corresponding track name, except you use: 
- %hh where you would write the number of hours, 
- %mm for minutes, 
- %ss for seconds, 
- %tt for the track name, 
- %ii wherever you want to ignore what is written.

If the "Compact spaces in timecodes" checkbox is checked, repeated spaces and tabs will be compacted to a single space before the timecodes are read.

# Example
If you provide timecodes for you tracks with this text:
```
Track1 0:0.0 - Track1_Overture
Track2 1:5.45 - Track2_Requiem
```

Where the first track starts at the begining of the file and is called "Track1_Overture", and the second starts after 1 hour, 5 minutes, and 45 seconds and is called "Track2_Requiem".
Then you can use the pattern:
```
%ii %hh:%mm.%ss - %tt
```
You should put the timecodes in the large rectangle space at the bottom of the application and the pattern in the small one on top of it.
Only put one timecode per line (like in the example above).

This will create two files, next to the original one: "1 - Track1_Overture.flac" and "2 - Track2_Requiem.flac"

# Running this software
## Integration
On linux simply run the script install.sh to integrate the software. 

## Run executable
On linux and windows, you can simply run the executable file. It will create a "settings" file next to the executable. You need to choose a directory to save information the first time you launch this software.

## Python
Alternatively, you can run the python scirpt directly from the source without any compilation. 
On linux 
```
python3 main.py
```

On windows
```
python main.py
```

# Some information on configuration.
You can display different statistics about a given ping stats series by checking the proper boxes. Drag and drop the boxes to change the order of the corresponding displays.
You can also change the order of the ping stat series by drag and drop (from the main view, not the "setting" window).

## On transitivity
You can set one transitivity option per ping stat series. If A is set to have transitivity on B (through A's settings window), then whenever you ping A it will also register a ping on B.

# Bells and whistles
This is a small project I mostly did for myself. As such, it does not aim to include all possible features and might be unreliable.
If you use this software and there is a reasonable change you want, or if you want to use it but are facing issues, feel free to open an issue on github. I do not guarantee to maintain this proect in any way, but I am likely to be amenable to small requests.

# License
The code for this software is released under the MIT license. The executables are released under the GPL3 license. See LICENSE file for more.

# Acknowledgements
This software used the PyQt6 library.
The sources for this library can be found [here](https://pypi.org/project/PyQt6/#files).
PyQt6 is itself reliant on Qt6, the source of which can be found [here](https://wiki.qt.io/Building_Qt_6_from_Git#Getting_the_source_code)
I extend my sincere gratitude to these and the other free libraries I used.