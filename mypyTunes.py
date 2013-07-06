import pyItunes, os, subprocess
from pyItunes import *
#Anything that's in ALLCAPS is something that needs to be replaced by your own information
#step 1, wake pbook
wakeBash = "/usr/bin/python ENTER-YOUR-PATH-TO-YOUR-WAKEUP-ON-LAN-SCRIPT-HERE"

#step 1a, command to wake pb
os.system(wakeBash)
#print "The sleeper has awaken... "

#step 2, extract the xml from the target computer that should have iTunes with all your movies
extractBash = 'scp USERNAME@IP-ADDRESS:/Users/USERNAME/Music/iTunes/"iTunes\ Music\ Library.xml" .'
os.system(extractBash)

#step 3, parse file
pl = XMLLibraryParser("iTunes Music Library.xml")
l = Library(pl.dictionary)
flix = []

for song in l.songs:
    flix.append(song.name + " (" + song.genre + ")")

finale = ''

#step 4, sort alphabetically and list
for i in sorted(flix):
    finale += i + "\n"


#step 5, send as email
gransep = "*****************************************************"
granfinale = "Movies:\n" + gransep + "\n" + finale + "\n"
#print granfinale
emailBash = "echo '" + granfinale + "' | mail -s \"My Viewing Library\" YOUR-EMAIL-ADDRESS"
os.system(emailBash)
