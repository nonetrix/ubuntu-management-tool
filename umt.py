#set python to 3
#!/usr/bin/env python3

#imports
import gi
import os


#set Gtk to 3.0
gi.require_version('Gtk', '3.0')
#more lmport crap
from gi.repository import Gtk

#check if running in root
if os.geteuid() != 0:
	exit("please run as sudo")

#make class MyWindow and etc
class MyWindow(Gtk.Window):
	def __init__(self):
		super(MyWindow, self).__init__()
		self.init_ui()
	def init_ui(self):
        
        #set window title
		self.set_title("umt")
		self.connect("destroy", Gtk.main_quit)

        #add hbox
		hbox = Gtk.Box(spacing=6)
		self.add(hbox)

        #buttons
		button = Gtk.Button(label="update repos")
		button.connect("clicked", self.on_button_clicked)
		hbox.pack_start(button, True, True, 0)

		button2 = Gtk.Button(label="update system")
		button2.connect("clicked", self.on_button2_clicked)
		hbox.pack_start(button2, True, True, 0)

		button3 = Gtk.Button(label="clean APT")
		button3.connect("clicked", self.on_button3_clicked)
		hbox.pack_start(button3, True, True, 0)
       
		button4 = Gtk.Button(label="update snaps")
		button4.connect("clicked", self.on_button4_clicked)
		hbox.pack_start(button4, True, True, 0)

		button5 = Gtk.Button(label="clean snap")
		button5.connect("clicked", self.on_button5_clicked)
		hbox.pack_start(button5, True, True, 0)

		button6 = Gtk.Button(label="clean flatpak")
		button6.connect("clicked", self.on_button6_clicked)
		hbox.pack_start(button6, True, True, 0)


    #commands
	def on_button_clicked(self, button):
		os.system("apt update -y &")

	def on_button2_clicked(self, button):
		os.system("apt upgrade -y && apt dist-upgrade -y &")

	def on_button3_clicked(self, button):
		os.system("apt autoclean && apt autoremove -y &")

	def on_button4_clicked(self, button):
		os.system("snap refresh &")

	def on_button5_clicked(self, button):
		os.system("rm /var/lib/snapd/cache/* &")

	def on_button6_clicked(self, button):
		os.system("flatpak uninstall --unused &")

#spawn window
win = MyWindow()
win.show_all()
Gtk.main()
