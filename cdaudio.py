#!/usr/bin/python

import sys
from optparse import OptionParser
import TKinter as gui

sys.path.append('python-audio-tools')

import audiotools
import audiotools.accuraterip

cd = audiotools.CDDA("/dev/cdrom")

print dir(cd)
meta = cd.metadata_lookup()

print dir(cd[1])

names=[]
for i, track in enumerate(cd):
	md = meta[0][i]
	#print track.offset(), track.length(), md.track_number, md.track_name,
	#print md.artist_name, md.album_name
	filename = '{1} - {0} - {2}.mp3'.format(md.track_number, md.artist_name, md.track_name)
	names.append(filename)


GUI=gui.Tk()
label=gui.Label(GUI, meta[0][0].album_name)
label.pack()
checked=[]

for name in names:
	checked.append(gui.Variable())
	c=gui.Checkbutton(GUI, text=name, variable=checked[-1])

GUI.mainloop()

def update(current, total):
	print '\r', current, total


format=audiotools.TYPE_MAP['mp3']
quali = 'standard'

track = cd[1]
ripper = audiotools.accuraterip.AccurateRipReader(track)

md=meta[0][i]

options = OptionParser()
msg = audiotools.Messenger('cdaudio', options)
prog = audiotools.SingleProgressDisplay(msg, filename)
riprog=audiotools.PCMReaderProgress(ripper, track.length()*(44100/75), update) #prog.update)

format.from_pcm(filename, riprog, quali, total_pcm_frames=track.length()*(44100/75))

print 'done!'
