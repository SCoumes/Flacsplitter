This software can be used to split a single .flac audio file into multiple flac files corresponding to individual tracks. 
You must provide timecodes of the begining of the tracks (presumably the first track starts at 0:00), along with their names.
This software allows some leeway in the format in which you provide the timecodes, as you can introduce your own "pattern", which will be used to read the timecodes.
A pattern is written like a line that gives a timecode and the corresponding track name, except you use: 
- %hh where you would write the number of hours, 
- %mm for minutes, 
- %ss for seconds, 
- %tt for the track name, 
- %ii wherever you want to ignore what is written.

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

# How to run
## Simple
On windows and linux you can direcly run the executable downloaded in the "release" section.

## Python
Alternatively, you can run the python code directly. On linux this would be done with
```
python3 main.py
```

Once you have installed the requirements with
```
pip install -r requirements.txt
```
# How to build
You can build you own executable by running "build.py". This requires pyinstaller.
```
pip install pyinstaller
```
# Disclaimer
This is not a polished piece of software and it is possible that you have timecodes in some format for which no pattern can be written.

# License
The code for this software is released under the MIT license. The executables are released under the GPL3 license. See LICENSE file for more.

# Acknowledgements
This software used the PyQt6 library.
The sources for this library can be found [here](https://pypi.org/project/PyQt6/#files).