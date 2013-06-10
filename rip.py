#!/usr/bin/env python
import sys, os, time
import pygtk
import gtk, gobject
pygtk.require('2.0')

class GUI:
	def __init__(self):
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window.set_resizable(True)

		box = gtk.VBox(False, 3)
		box.set_border_width(20)
		self.window.add(box)
		box.show()

		self.caption = gtk.Label('Title')
		self.box.add(self.caption)
		self.caption.show()

		sep = gtk.HSeparator
		self.box.add(sep)
		sep.show()

		self.processes = []


def update(current, total):
	print '\r', current, total

class CD:
	def __init__(self):
		sys.path.append('python-audio-tools')

		import audiotools
		import audiotools.accuraterip

		cd_drive=os.path.realpath('/dev/cdrom')		

		names=[]
		for i, track in enumerate(cd):
			md = meta[0][i]
			filename = '{1} - {0} - {2}.mp3'.format(md.track_number, md.artist_name, md.track_name)
			names.append(filename)

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


if __name__ == '__main__':
	gui=GUI()
	gui.main()