# -*- coding: utf-8 -*-
# :D
# Feliz Navidad!
# Ignacio Rodríguez <nachoel01@gmail.com>
# CeibalJAM! - Uruguay 
from sugar.activity import activity # Actividad
from sugar.activity.widgets import StopButton # Boton Parar
from sugar.activity.widgets import ActivityToolbarButton # Boton de la actividad
from sugar.graphics.toolbutton import ToolButton # Boton 
from sugar.graphics.toolbarbox import ToolbarBox
import gtk,pango,gst
class Navidad(activity.Activity):
	def __init__(self,handle):
		activity.Activity.__init__(self, handle, True)
		cs = ActivityToolbarButton(self)
		c = gtk.SeparatorToolItem()
		c.set_expand(True)
		lugar = activity.get_bundle_path()
		Musica = gst.element_factory_make('playbin')
		Musica.set_property('uri','file://'+lugar+'/Musica.ogg')
		Musica.set_state(gst.STATE_PLAYING)
		Toolbar = ToolbarBox()
		Toolbar.toolbar.insert(cs,-1)
		Toolbar.toolbar.insert(c,-1)
		F = ToolButton('F')
		Toolbar.toolbar.insert(F,-1)
		F = ToolButton('E')
		Toolbar.toolbar.insert(F,-1)
		F = ToolButton('L')
		Toolbar.toolbar.insert(F,-1)
		F = ToolButton('I')
		Toolbar.toolbar.insert(F,-1)
		F = ToolButton('Z')
		Toolbar.toolbar.insert(F,-1)
		a = gtk.SeparatorToolItem()
		a.set_expand(True)
		a.props.draw = False
		Toolbar.toolbar.insert(a,-1)
		F = ToolButton('N')
		Toolbar.toolbar.insert(F,-1)
		F = ToolButton('A')
		Toolbar.toolbar.insert(F,-1)
		F = ToolButton('V')
		Toolbar.toolbar.insert(F,-1)
		F = ToolButton('I')
		Toolbar.toolbar.insert(F,-1)
		F = ToolButton('D')
		Toolbar.toolbar.insert(F,-1)
		F = ToolButton('A')
		Toolbar.toolbar.insert(F,-1)
		F = ToolButton('D')
		Toolbar.toolbar.insert(F,-1)
		Stop = StopButton(self)
		b = gtk.SeparatorToolItem()
		b.set_expand(True)
		Toolbar.toolbar.insert(b,-1)
		Toolbar.toolbar.insert(Stop,-1)
		vs = gtk.VBox()
		Imagen = gtk.Image()
		Imagen.set_from_file('Imagen.svg')
		vs.pack_start(Imagen,True,True,0)
		bs = gtk.TextBuffer()
		bs.set_text('El equipo de CeibalJAM! te desea feliz navidad y prospero año nuevo')
		entry = gtk.TextView(bs)
		fuente = pango.FontDescription('Purisa 16')
		entry.set_editable(False)
		entry.modify_font(fuente)
		vs.pack_end(entry,False,False,0)
		self.set_canvas(vs)
		self.set_toolbar_box(Toolbar)
		self.show_all()
