# -*- coding: utf-8 -*-
# :D
# Feliz Navidad!
# Ignacio Rodríguez <nachoel01@gmail.com>
# CeibalJAM! - Uruguay
import os
import gi
gi.require_version('Gtk', '3.0')
# gi.require_version('Gdk', '1.0')
gi.require_version('Gst', '1.0')
from gi.repository import Gtk
from gi.repository import Gdk
from gi.repository import GObject
from gi.repository import Gst
from gi.repository import Pango
import random
from sugar3.activity import activity # Actividad
from sugar3.activity.widgets import StopButton # Boton Parar
from sugar3.activity.widgets import ActivityToolbarButton # Boton de la actividad
from sugar3.graphics.toolbutton import ToolButton # Boton 
from sugar3.graphics.toolbarbox import ToolbarBox
from Saber import saber,color
from datetime import date 
class Navidad(activity.Activity):
	def __init__(self,handle):
		activity.Activity.__init__(self, handle, True)
		cs = ActivityToolbarButton(self)
		c = Gtk.SeparatorToolItem()
		c.set_expand(True)
		lugar = activity.get_bundle_path()
		Gst.init(None)
		self.Musica = Gst.ElementFactory.make('playbin')
		self.Musica.set_property('uri','file://'+lugar+'/Musica.ogg')
		self.Musica.set_state(Gst.State.PLAYING)
		
		self.Toolbar = ToolbarBox()
		self.Toolbar.toolbar.insert(cs,-1)
		self.F = ToolButton('F')
		self.Toolbar.toolbar.insert(self.F,-1)
		self.cambiado = False
		self.cambiadoc = False

		self.E = ToolButton('E')
		self.Toolbar.toolbar.insert(self.E,-1)

		self.L = ToolButton('L')
		self.Toolbar.toolbar.insert(self.L,-1)

		self.I = ToolButton('I')
		self.Toolbar.toolbar.insert(self.I,-1)
		self.Z = ToolButton('Z')
		self.Toolbar.toolbar.insert(self.Z,-1)



		self.N = ToolButton('N')
		self.Toolbar.toolbar.insert(self.N,-1)
		
		self.AA = ToolButton('A')
		self.Toolbar.toolbar.insert(self.AA,-1)
		
		self.V = ToolButton('V')
		self.Toolbar.toolbar.insert(self.V,-1)
		
		self.II = ToolButton('I')
		self.Toolbar.toolbar.insert(self.II,-1)

		self.D = ToolButton('D')
		self.Toolbar.toolbar.insert(self.D,-1)
		
		self.AAA = ToolButton('A')
		self.Toolbar.toolbar.insert(self.AAA,-1)

		self.DD = ToolButton('D')
		self.Toolbar.toolbar.insert(self.DD,-1)
		self.cambiar()		
		Stop = StopButton(self)
		b = Gtk.SeparatorToolItem()
		b.set_expand(True)

		self.Toolbar.toolbar.insert(Stop,-1)
		self.vox = Gtk.EventBox()
		vs = Gtk.VBox()
		self.vox.add(vs)
		Imagen = Gtk.Image()
		Imagen.set_from_file('Imagen.svg')
		bs = Gtk.TextBuffer()
		bs.set_text('El equipo de CeibalJAM! te desea feliz navidad y prospero año nuevo')
		entry = Gtk.TextView.new_with_buffer(bs)
		fuente = Pango.FontDescription('11')
		entry.set_editable(False)
		entry.modify_font(fuente)
		self.vox.connect('button-release-event',self.color,entry)
		self.color('a','b',entry)
		self.label = Gtk.Label(label=saber())
		self.label.modify_font(fuente)
		vs.pack_start(self.label,False,False,0)
		color(self.label)
		vs.pack_end(entry,False,False,0)
		self.set_canvas(self.vox)
		vs.pack_start(Imagen,True,True,0)
		self.set_toolbar_box(self.Toolbar)
		self.show_all()
		GObject.timeout_add(37500, self.sonido)
	def sonido(self):
		self.Musica.set_state(Gst.State.NULL)
		self.Musica.set_state(Gst.State.PLAYING)
		GObject.timeout_add(37500, self.sonido)
	def color(self,widget=None,event=None,entrada=None):
		colores = ["#FA2635","#33DA40"]
		cc = random.choice(colores)
		entrada.modify_bg(Gtk.StateType.NORMAL,Gdk.color_parse(cc))
		self.vox.modify_bg(Gtk.StateType.NORMAL,Gdk.color_parse(cc))
		self.vox.show_all()
		GObject.timeout_add(500, self.color,'a','b',entrada)
	def cc(self,a=None,b=None,c=None,d=None):
		if self.cambiadoc:
			self.cambiado = True
		if not self.cambiadoc:
			self.cambiado = False

	def cambiar(self,a=None,b=None):
		if not self.cambiado:	
			""" a cambiar """
			self.F.set_icon_name('Fr') # 1
			self.L.set_icon_name('Lr') # 3
			self.Z.set_icon_name('Zr') # 
			self.AA.set_icon_name('Ar') #
			self.II.set_icon_name('Ir') #
			self.AAA.set_icon_name('Ar') #
			""" VUELVEN """
			self.E.set_icon_name('E') # Feliz Navidad #
			self.I.set_icon_name('I')
			self.N.set_icon_name('N')
			self.V.set_icon_name('V')
			self.D.set_icon_name('D')
			self.DD.set_icon_name('D')
			self.cambiadoc = True
			self.Toolbar.show_all()
		if self.cambiado:	
			""" a cambiar """
			self.F.set_icon_name('F') # 1
			self.L.set_icon_name('L') # 3
			self.Z.set_icon_name('Z') # 
			self.AA.set_icon_name('A') #
			self.II.set_icon_name('I') #
			self.AAA.set_icon_name('A') #
			""" VUELVEN """
			self.E.set_icon_name('Er') # Feliz Navidad #
			self.I.set_icon_name('Ir')
			self.N.set_icon_name('Nr')
			self.V.set_icon_name('Vr')
			self.D.set_icon_name('Dr')
			self.DD.set_icon_name('Dr')
			self.cambiadoc = False
			self.Toolbar.show_all()
		GObject.timeout_add(500, self.cc)
		GObject.timeout_add(500, self.cambiar)
