#!/usr/bin/env python3
import gi
import os
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MyWindow(Gtk.Window):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.init_ui()
    def init_ui(self):
        
        self.set_title("umt")
        self.connect("destroy", Gtk.main_quit)

        grid = Gtk.Grid()
        self.add(grid)

        Btn = Gtk.Button(label="update repos")
        Btn.set_size_request(30, 0)
        Btn.connect("clicked", self.on_button_clicked)

        Btn2 = Gtk.Button(label="update system")
        Btn2.set_size_request(30, 0)
        Btn2.connect("clicked", self.on_button2_clicked)

        Btn3 = Gtk.Button(label="clean APT")
        Btn3.set_size_request(30, 0)
        Btn3.connect("clicked", self.on_button3_clicked)
        
        Btn4 = Gtk.Button(label="update snaps")
        Btn4.set_size_request(30, 0)
        Btn4.connect("clicked", self.on_button4_clicked)

        Btn5 = Gtk.Button(label="clean snap")
        Btn5.set_size_request(30, 0)
        Btn5.connect("clicked", self.on_button5_clicked)

        Btn6 = Gtk.Button(label="clean flatpak")
        Btn6.set_size_request(30, 0)
        Btn6.connect("clicked", self.on_button5_clicked)

        grid.attach(Btn, 0, 10, 1, 1)
        
        grid.attach(Btn2, 0, 20, 1, 1)
        
        grid.attach(Btn3, 10, 10, 1, 1)
        
        grid.attach(Btn4, 10, 20, 1, 1)
        
        grid.attach(Btn5, 20, 10, 1, 1)
        
        grid.attach(Btn6, 20, 20, 1, 1)

    def on_button_clicked(self, widget):
        os.system("apt update &")

    def on_button2_clicked(self, widget):
        os.system("apt upgrade && apt dist-upgrade &")

    def on_button3_clicked(self, widget):
        os.system("apt autoclean && apt autoremove &")

    def on_button4_clicked(self, widget):
        os.system("snap refresh &")

    def on_button5_clicked(self, widget):
        os.system("rm /var/lib/snapd/cache/* &")
        
    def on_button6_clicked(self, widget):
        os.system("flatpak uninstall --unused &")

win = MyWindow()
win.show_all()
Gtk.main()