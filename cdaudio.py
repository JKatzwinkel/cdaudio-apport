#!/usr/bin/python

import sys
from optparse import OptionParser
import Tkinter as gui
import time
import os.path


class Gui():
	def __init__(self, root):
		#super(Gui, self).__init__()
		self.root = root
		self.root.title('Audio CD')
		screen = (self.root.winfo_screenwidth(), self.root.winfo_screenheight())
		width  = int(screen[0] * .8)
		height  = int(screen[1] * .8)
		posX   = (screen[0] - width)/2 # Find left and up border of window
		posY   = (screen[1] - height)/2
		self.root.geometry("%sx%s+%s+%s"%(width,height,posX,posY))
		#self.titlebar=gui.Label(self.root, text="No CD").grid(row=0)
		self.frame=gui.Frame(self.root)
		self.frame.grid(row=1)
		self.bottom=gui.Frame(self.root).grid(row=2)
		self.status=gui.Label(self.bottom, text="waiting...")
		self.status.pack()
		self.items=[]

	def add_tracks(self, tracks):
		for i, filename in enumerate(tracks):
			checked = gui.IntVar()
			checked.set(1)
			c=gui.Checkbutton(self.frame, text=filename, variable=checked)
			c.grid(row=i, sticky=gui.W)
		self.status.text="album"
		#self.frame.grid(row=1)



sys.path.append('python-audio-tools')

import audiotools
import audiotools.accuraterip

cd_drive=os.path.realpath('/dev/cdrom')
def cd_ready():
	try:
		if open(cd_drive):
			return True
	except:
		return False
	return False


# wait until drive is ready
while not cd_ready():
	time.sleep(5)

cd = audiotools.CDDA("/dev/cdrom")
meta = cd.metadata_lookup()


names=[]
for i, track in enumerate(cd):
	md = meta[0][i]
	filename = '{1} - {0} - {2}.mp3'.format(md.track_number, md.artist_name, md.track_name)
	names.append(filename)


win = gui.Tk()
GUI = Gui(win)
GUI.add_tracks(names)
gui.mainloop()

#GUI=gui.Tk()
#GUI.title('Audio CD extraction')
#label=gui.Label(GUI, text=meta[0][0].album_name)
#label.pack()

#trackframe=gui.Frame(GUI)
#trackframe.pack_propagate(0)
#trackframe.width=600
#trackframe.borderwidth=2
#checked=[]

#for i, name in enumerate(names):
#	checked.append(gui.IntVar())
#	checked[-1].set(1)
#	c=gui.Checkbutton(trackframe, text=name, variable=checked[-1])
#	c.grid(row=i, sticky=gui.W)
	#c.pack(fill=gui.X, side=gui.TOP)

#trackframe.pack()
	
#statusbar=gui.Frame(GUI, bg='#b0d0ff')
#statusbar.pack_propagate(0)
#statusbar.borderwidth=1
#statusbar.width=trackframe.width
#statusbar.height=30
#statusbar.pack(fill=gui.X, side=gui.BOTTOM)

sys.exit(0)

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
