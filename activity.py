# -*- coding: utf-8 -*-
# :D
# Feliz Navidad!
# Ignacio Rodríguez <nachoel01@gmail.com>
# CeibalJAM! - Uruguay 
try:
	from sugar.activity import activity # Actividad
	from sugar.activity.widgets import StopButton # Boton Parar
	from sugar.activity.widgets import ActivityToolbarButton # Boton de la actividad
	from sugar.graphics.toolbutton import ToolButton # Boton 
	from sugar.graphics.toolbarbox import ToolbarBox
	sugar = True
except:
	sugar = False
	pass
import gtk,pango,gst,os
if sugar:
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
			self.vox = gtk.EventBox()
			vs = gtk.VBox()
			self.vox.add(vs)
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
			self.vox.connect('button-release-event',self.color,entry)
			self.set_canvas(self.vox)
			self.set_toolbar_box(Toolbar)
			self.show_all()
		def color(self,widget,event,entrada):
			colores = ["#FA2635","#33DA40","#FA2635","#33DA40","#FA2635","#33DA40","#FA2635","#33DA40","#FA2635","#33DA40","#FA2635","#33DA40","#FA2635","#33DA40",]
			import random
			Boton = event.button
			cc = random.choice(colores)
			if Boton == 1:
				entrada.modify_bg(gtk.STATE_NORMAL,gtk.gdk.color_parse(cc))
				self.vox.modify_bg(gtk.STATE_NORMAL,gtk.gdk.color_parse(cc))
				self.vox.show_all()
if not sugar:
	class Ceibaljam(gtk.Window):
		def __init__(self):
			gtk.Window.__init__(self)
			Toolbar = gtk.Toolbar()
			""" IMAGENES PARA LOS BOTONES """
			f = gtk.Image()
			e = gtk.Image()
			l = gtk.Image()
			i = gtk.Image()
			ii = gtk.Image()
			z = gtk.Image()
			n = gtk.Image()
			a = gtk.Image()
			aa = gtk.Image()
			aaa = gtk.Image()
			v = gtk.Image()
			d = gtk.Image()
			dd = gtk.Image()
			f.set_from_pixbuf(gtk.gdk.pixbuf_new_from_file_at_size('icons/F.svg',36,36))
			e.set_from_pixbuf(gtk.gdk.pixbuf_new_from_file_at_size('icons/E.svg',36,36))
			l.set_from_pixbuf(gtk.gdk.pixbuf_new_from_file_at_size('icons/L.svg',36,36))
			i.set_from_pixbuf(gtk.gdk.pixbuf_new_from_file_at_size('icons/I.svg',36,36))
			ii.set_from_pixbuf(gtk.gdk.pixbuf_new_from_file_at_size('icons/I.svg',36,36))
			z.set_from_pixbuf(gtk.gdk.pixbuf_new_from_file_at_size('icons/Z.svg',36,36))
			n.set_from_pixbuf(gtk.gdk.pixbuf_new_from_file_at_size('icons/N.svg',36,36))
			a.set_from_pixbuf(gtk.gdk.pixbuf_new_from_file_at_size('icons/A.svg',36,36))
			aa.set_from_pixbuf(gtk.gdk.pixbuf_new_from_file_at_size('icons/A.svg',36,36))
			aaa.set_from_pixbuf(gtk.gdk.pixbuf_new_from_file_at_size('icons/A.svg',36,36))
			v.set_from_pixbuf(gtk.gdk.pixbuf_new_from_file_at_size('icons/V.svg',36,36))
			d.set_from_pixbuf(gtk.gdk.pixbuf_new_from_file_at_size('icons/D.svg',36,36))
			dd.set_from_pixbuf(gtk.gdk.pixbuf_new_from_file_at_size('icons/D.svg',36,36))
	
			F = gtk.ToolButton()
			F.set_icon_widget(f) #  F
			Toolbar.insert(F,-1)
			F = gtk.ToolButton() 
			F.set_icon_widget(e) #  E
			Toolbar.insert(F,-1)
			F = gtk.ToolButton() #  L
			F.set_icon_widget(l)
			Toolbar.insert(F,-1) #  I
			F = gtk.ToolButton()
			F.set_icon_widget(ii)
			Toolbar.insert(F,-1)
			F = gtk.ToolButton() #   z
			F.set_icon_widget(z)
			Toolbar.insert(F,-1)
			a = gtk.SeparatorToolItem()
			a.set_expand(True)
			a.props.draw = False
			Toolbar.insert(a,-1)
		
			F = gtk.ToolButton()
			F.set_icon_widget(n)
			Toolbar.insert(F,-1)
		
			F = gtk.ToolButton()
			F.set_icon_widget(aaa)
			Toolbar.insert(F,-1)
		
			F = gtk.ToolButton()
			F.set_icon_widget(v)
			Toolbar.insert(F,-1)
		
			F = gtk.ToolButton()
			F.set_icon_widget(i)
			Toolbar.insert(F,-1)
		
			F = gtk.ToolButton()
			F.set_icon_widget(dd)
			Toolbar.insert(F,-1)
		
			F = gtk.ToolButton()
			F.set_icon_widget(aa)
			Toolbar.insert(F,-1)
			self.connect('destroy',lambda x: exit("Feliz Navidad!"))
			lugar = os.getcwd()
			Musica = gst.element_factory_make('playbin')
			Musica.set_property('uri','file://'+lugar+'/Musica.ogg')
			Musica.set_state(gst.STATE_PLAYING)		
			F = gtk.ToolButton()
			F.set_icon_widget(d)
			Toolbar.insert(F,-1)		
			self.evento = gtk.EventBox()
			box = gtk.VBox()
			self.evento.add(box)
			Imagen = gtk.Image()
			Imagen.set_from_file('Imagen.svg')
			box.pack_start(Toolbar,False,False,0)
			box.pack_start(Imagen,False,False,0)
			bs = gtk.TextBuffer()
			bs.set_text('El equipo de CeibalJAM! te desea feliz navidad y prospero año nuevo')
			entry = gtk.TextView(bs)
			fuente = pango.FontDescription('Purisa 16')
			entry.set_editable(False)
			entry.modify_font(fuente)
			self.evento.connect('button-release-event',self.color,entry)
			box.pack_end(entry,False,False,0)
			self.add(self.evento)
			self.show_all()
			self.set_title('¡Feliz navidad!')
		def color(self,widget,event,entrada):
			colores = ["#FA2635","#33DA40","#EDEDED"]
			import random
			Boton = event.button
			cc = random.choice(colores)
			if Boton == 1:
				widget.modify_bg(gtk.STATE_NORMAL,gtk.gdk.color_parse(cc))
				widget.show_all()
if __name__ == "__main__":
	if not sugar:
		programa = Ceibaljam()
		gtk.main()
	else:
		pass
