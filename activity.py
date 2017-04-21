# -*- coding: utf-8 -*-
# :D
# Feliz Navidad!
# Ignacio Rodríguez <nachoel01@gmail.com>
# CeibalJAM! - Uruguay
import os,gobject,random,gtk,gst,pango
from sugar.activity import activity # Actividad
from sugar.activity.widgets import StopButton # Boton Parar
from sugar.activity.widgets import ActivityToolbarButton # Boton de la actividad
from sugar.graphics.toolbutton import ToolButton # Boton 
from sugar.graphics.toolbarbox import ToolbarBox
from Saber import saber,color
from datetime import date 
class Navidad(activity.Activity):
	def __init__(self,handle):
		activity.Activity.__init__(self, handle, True)
		cs = ActivityToolbarButton(self)
		c = gtk.SeparatorToolItem()
		c.set_expand(True)
		lugar = activity.get_bundle_path()
		self.Musica = gst.element_factory_make('playbin')
		self.Musica.set_property('uri','file://'+lugar+'/Musica.ogg')
		self.Musica.set_state(gst.STATE_PLAYING)
		
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
		b = gtk.SeparatorToolItem()
		b.set_expand(True)

		self.Toolbar.toolbar.insert(Stop,-1)
		self.vox = gtk.EventBox()
		vs = gtk.VBox()
		self.vox.add(vs)
		Imagen = gtk.Image()
		Imagen.set_from_file('Imagen.svg')
		bs = gtk.TextBuffer()
		bs.set_text('El equipo de CeibalJAM! te desea feliz navidad y prospero año nuevo')
		entry = gtk.TextView(bs)
		fuente = pango.FontDescription('11')
		entry.set_editable(False)
		entry.modify_font(fuente)
		self.vox.connect('button-release-event',self.color,entry)
		self.color('a','b',entry)
		self.label = gtk.Label(saber())
		self.label.modify_font(fuente)
		vs.pack_start(self.label,False,False,0)
		color(self.label)
		vs.pack_end(entry,False,False,0)
		self.set_canvas(self.vox)
		vs.pack_start(Imagen,True,True,0)
		self.set_toolbar_box(self.Toolbar)
		self.show_all()
		gobject.timeout_add(37500, self.sonido)
	def sonido(self):
		self.Musica.set_state(gst.STATE_NULL)
		self.Musica.set_state(gst.STATE_PLAYING)
		gobject.timeout_add(37500, self.sonido)
	def color(self,widget=None,event=None,entrada=None):
		colores = ["#FA2635","#33DA40"]
		cc = random.choice(colores)
		entrada.modify_bg(gtk.STATE_NORMAL,gtk.gdk.color_parse(cc))
		self.vox.modify_bg(gtk.STATE_NORMAL,gtk.gdk.color_parse(cc))
		self.vox.show_all()
		gobject.timeout_add(500, self.color,'a','b',entrada)
	def cc(self,a=None,b=None,c=None,d=None):
		if self.cambiadoc:
			self.cambiado = True
		if not self.cambiadoc:
			self.cambiado = False

	def cambiar(self,a=None,b=None):
		if not self.cambiado:	
			""" a cambiar """
			self.F.set_icon('Fr') # 1
			self.L.set_icon('Lr') # 3
			self.Z.set_icon('Zr') # 
			self.AA.set_icon('Ar') #
			self.II.set_icon('Ir') #
			self.AAA.set_icon('Ar') #
			""" VUELVEN """
			self.E.set_icon('E') # Feliz Navidad #
			self.I.set_icon('I')
			self.N.set_icon('N')
			self.V.set_icon('V')
			self.D.set_icon('D')
			self.DD.set_icon('D')
			self.cambiadoc = True
			self.Toolbar.show_all()
		if self.cambiado:	
			""" a cambiar """
			self.F.set_icon('F') # 1
			self.L.set_icon('L') # 3
			self.Z.set_icon('Z') # 
			self.AA.set_icon('A') #
			self.II.set_icon('I') #
			self.AAA.set_icon('A') #
			""" VUELVEN """
			self.E.set_icon('Er') # Feliz Navidad #
			self.I.set_icon('Ir')
			self.N.set_icon('Nr')
			self.V.set_icon('Vr')
			self.D.set_icon('Dr')
			self.DD.set_icon('Dr')
			self.cambiadoc = False
			self.Toolbar.show_all()
		gobject.timeout_add(500, self.cc)
		gobject.timeout_add(500, self.cambiar)
