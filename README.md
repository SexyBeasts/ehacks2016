# ehacks2016
Pitch Recognition/Sheet Music

#Changes addressed to the dev team
The OldRepo folder is what was effectively a massive dropbox and mishmash of files used for the first few days of development

The MirrorScore folder is the actual Flask framework that the software is based on

# What is in this repo?
A web based application that allows a user to upload a monaural(mono) channel .wav file for sheet music conversion

*app/templates* contains the **html**

*app/static* contains all other resources (**CSS/JavaScript/resources**)

**HertzReader.py** contains the analysis algorithm for the file

#How can I help this repo?

##Pertinant issues
The sheet music result page (or notes.html) generates random sheet music (currently), and does not actually recieve the decoded python list from HertzReader.py

Potential way to fix this include..
  * Making a file format for output by the server
  * Using JSON
  * Creativity
  
##Room for Improvement
The overall functionality and quality of the program would be improved with..
  * More than .wav file analysis
  * Stereo file analysis
  * An algorithm that analyzes bpm or tempo
  * Sheet music that can be printed or read from
  * Flashy transitions and animations
  
Thanks for reading!
