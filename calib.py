#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 6.2
#  in conjunction with Tcl version 8.6
#    Aug 30, 2021 04:41:16 PM CEST  platform: Windows NT

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1

import sys
import calib_support
sys.path.insert(0, "C:\Users\G702234\OneDrive - Sagemcom Broadband SAS\Documents\Tools_DB\LaboTools_V1.r4033")
import producttype


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    calib_support.set_Tk_var()
    top = importer (root)
    calib_support.init(root, top)
    root.mainloop()

w = None
def create_import(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_import(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = Toplevel (root)
    calib_support.set_Tk_var()
    top = importer (w)
    calib_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_import():
    global w
    w.destroy()
    w = None

class importer:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#f5f5f5'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#f5f5f5' # X11 color: 'gray85'
        _ana1color = '#f5f5f5' # X11 color: 'gray85'
        _ana2color = '#f5f5f5' # X11 color: 'gray85'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("1265x770+-8+-8")
        top.minsize(120, 1)
        top.maxsize(1265, 770)
        top.resizable(0,  0)
        top.title("Searcher")
        top.configure(background="#f5f5f5")
        top.configure(highlightbackground="#f5f5f5")
        top.configure(highlightcolor="black")

        ###########################################################################################
        ### FRAME DATA IMPORTATION
        ###########################################################################################
        self.frameImport = Frame(top)
        self.frameImport.place(x=10, y=10, height=254, width=1246)
        self.frameImport.configure(relief='groove')
        self.frameImport.configure(borderwidth="2")
        self.frameImport.configure(relief="groove")
        self.frameImport.configure(background="#ffffff")
        self.frameImport.configure(highlightbackground="#000000")
        self.frameImport.configure(highlightcolor="black")

        # Label adresse dossier CAL
        ###########################################################################################
        self.LabelPathImp = Label(self.frameImport)
        self.LabelPathImp.place(x=40, y=40, height=19, width=90)
        self.LabelPathImp.configure(activebackground="#f9f9f9")
        self.LabelPathImp.configure(activeforeground="black")
        self.LabelPathImp.configure(background="#d9d9d9")
        self.LabelPathImp.configure(cursor="fleur")
        self.LabelPathImp.configure(disabledforeground="#a3a3a3")
        self.LabelPathImp.configure(foreground="#000000")
        self.LabelPathImp.configure(highlightbackground="#d9d9d9")
        self.LabelPathImp.configure(highlightcolor="black")
        self.LabelPathImp.configure(text='''Path to search:''')

        # Txt adresse dossier CAL
        self.txtPathImport = Entry(self.frameImport)
        self.txtPathImport.place(x=140, y=40, height=31, width=450)
        self.txtPathImport.configure(background="white")
        self.txtPathImport.configure(disabledforeground="#a3a3a3")
        self.txtPathImport.configure(font="TkFixedFont")
        self.txtPathImport.configure(foreground="#000000")
        self.txtPathImport.configure(highlightbackground="#d9d9d9")
        self.txtPathImport.configure(highlightcolor="black")
        self.txtPathImport.configure(insertbackground="black")
        self.txtPathImport.configure(selectbackground="#c4c4c4")
        self.txtPathImport.configure(selectforeground="black")
        self.txtPathImport.configure(textvariable=calib_support.ImportPath)

        # Btn chercher adresse dossier CAL
        self.btnSearchPath = Button(self.frameImport)
        self.btnSearchPath.place(x=600, y=40, height=27, width=38)
        self.btnSearchPath.configure(activebackground="#d9d9d9")
        self.btnSearchPath.configure(activeforeground="black")
        self.btnSearchPath.configure(background="#d9d9d9")
        self.btnSearchPath.configure(command=calib_support.OnBtnSearchPath)
        self.btnSearchPath.configure(disabledforeground="#a3a3a3")
        self.btnSearchPath.configure(foreground="#000000")
        self.btnSearchPath.configure(highlightbackground="#d9d9d9")
        self.btnSearchPath.configure(highlightcolor="black")
        self.btnSearchPath.configure(pady="0")
        self.btnSearchPath.configure(text='''...''')

        # Label température
        ###########################################################################################
        self.LabelTemp = Label(self.frameImport)
        self.LabelTemp.place(x=40, y=80, height=21, width=90)
        self.LabelTemp.configure(background="#d9d9d9")
        self.LabelTemp.configure(disabledforeground="#a3a3a3")
        self.LabelTemp.configure(foreground="#000000")
        self.LabelTemp.configure(text='''Températures''')

        # Txt température
        self.txtTemp = Entry(self.frameImport)
        self.txtTemp.place(x=140, y=80, height=31, width=450)
        self.txtTemp.configure(background="white")
        self.txtTemp.configure(disabledforeground="#a3a3a3")
        self.txtTemp.configure(font="TkFixedFont")
        self.txtTemp.configure(foreground="#000000")
        self.txtTemp.configure(highlightbackground="#d9d9d9")
        self.txtTemp.configure(highlightcolor="black")
        self.txtTemp.configure(insertbackground="black")
        self.txtTemp.configure(selectbackground="#c4c4c4")
        self.txtTemp.configure(selectforeground="black")
        self.txtTemp.configure(textvariable=calib_support.Temp)

        # Label séquence complète
        ##########################################################################################
        self.LabelSeq = Label(self.frameImport)
        self.LabelSeq.place(x=40, y=120, height=21, width=90)
        self.LabelSeq.configure(background="#d9d9d9")
        self.LabelSeq.configure(disabledforeground="#a3a3a3")
        self.LabelSeq.configure(foreground="#000000")
        self.LabelSeq.configure(text='''Séquence''')

        # Txt Seq
        self.txtSeq = Entry(self.frameImport)
        self.txtSeq.place(x=140, y=120, height=31, width=450)
        self.txtSeq.configure(background="white")
        self.txtSeq.configure(disabledforeground="#a3a3a3")
        self.txtSeq.configure(font="TkFixedFont")
        self.txtSeq.configure(foreground="#000000")
        self.txtSeq.configure(highlightbackground="#d9d9d9")
        self.txtSeq.configure(highlightcolor="black")
        self.txtSeq.configure(insertbackground="black")
        self.txtSeq.configure(selectbackground="#c4c4c4")
        self.txtSeq.configure(selectforeground="black")
        self.txtSeq.configure(textvariable=calib_support.Seq)


        # Choix de la séquence Manu\Auto
        ###########################################################################################
        self.choixSeq = Checkbutton(self.frameImport, text = 'Manuelle', variable = calib_support.ModeSeq, onvalue=True, offvalue = False)
        self.choixSeq.place(x=600, y=120)
        self.choixSeq.configure(background="white")
        self.choixSeq.configure(disabledforeground="#a3a3a3")
        self.choixSeq.configure(font="TkFixedFont")
        self.choixSeq.configure(foreground="#000000")
        self.choixSeq.configure(highlightbackground="#d9d9d9")
        self.choixSeq.configure(highlightcolor="black")

        # Label Producttype
        ###########################################################################################
        self.LabelProduct = Label(self.frameImport)
        self.LabelProduct.place(x=40, y=160, height=21, width=90)
        self.LabelProduct.configure(background="#d9d9d9")
        self.LabelProduct.configure(disabledforeground="#a3a3a3")
        self.LabelProduct.configure(foreground="#000000")
        self.LabelProduct.configure(text='''Producttype''')

        # Choix du producttype
        self.productComboBox = ttk.Combobox(self.frameImport)
        self.productComboBox.place(x = 140, y = 160, width=450)
        self.productComboBox.configure(textvariable=calib_support.ProductComboValue, values=producttype.ProductList)

        # Choix Filtrer debit qui ne sont pas dans la sequence
        ###########################################################################################
        self.choixSeq = Checkbutton(self.frameImport, text = 'Filtrer debit', variable = calib_support.FiltreDebit, onvalue=True, offvalue = False)
        self.choixSeq.place(x=600, y=160)
        self.choixSeq.configure(background="white")
        self.choixSeq.configure(disabledforeground="#a3a3a3")
        self.choixSeq.configure(font="TkFixedFont")
        self.choixSeq.configure(foreground="#000000")
        self.choixSeq.configure(highlightbackground="#d9d9d9")
        self.choixSeq.configure(highlightcolor="black")

        # TextBox
        self.txtBoxImport = Message(self.frameImport, width = 60, textvariable = calib_support.TxtImport)
        self.txtBoxImport.place(x=750, y=20)

        # Btn Import
        ###########################################################################################
        self.btnImport = Button(self.frameImport)
        self.btnImport.place(x=150, y=200, height=24, width=47)
        self.btnImport.configure(activebackground="#d9d9d9")
        self.btnImport.configure(activeforeground="black")
        self.btnImport.configure(background="#d9d9d9")
        self.btnImport.configure(disabledforeground="#a3a3a3")
        self.btnImport.configure(foreground="#000000")
        self.btnImport.configure(highlightbackground="#d9d9d9")
        self.btnImport.configure(highlightcolor="black")
        self.btnImport.configure(pady="0")
        self.btnImport.configure(text='''Import''')
        self.btnImport.bind('<Button-1>',lambda e:calib_support.OnBtnImp(e))


        self.style.configure('Treeview',  font="TkDefaultFont")
        self.Scrolledtreeview1 = ScrolledTreeView(self.frameImport)
        self.Scrolledtreeview1.place(x=0, y=0, height=1, width=1)
        # build_treeview_support starting.
        self.Scrolledtreeview1.heading("#0",anchor="center")
        self.Scrolledtreeview1.column("#0",width="200")
        self.Scrolledtreeview1.column("#0",minwidth="20")
        self.Scrolledtreeview1.column("#0",stretch="1")
        self.Scrolledtreeview1.column("#0",anchor="w")
        self.Scrolledtreeview1.bind('<Button-1>',lambda e:calib_support.OnTreeviewClick(e))

        ###########################################################################################
        ### FRAME GEN MODEL
        ###########################################################################################
        self.frameGenerate = Frame(top)
        self.frameGenerate.place(x=10, y=270, height=360, width=1246)
        self.frameGenerate.configure(relief='groove')
        self.frameGenerate.configure(borderwidth="2")
        self.frameGenerate.configure(relief="groove")
        self.frameGenerate.configure(background="#ffffff")
        self.frameGenerate.configure(highlightbackground="#ffffff")
        self.frameGenerate.configure(highlightcolor="black")

        # Label adresse dossier CAL
        ###########################################################################################
        self.LabelPathGen = Label(self.frameGenerate)
        self.LabelPathGen.place(x=40, y=40, height=19, width=90)
        self.LabelPathGen.configure(activebackground="#f9f9f9")
        self.LabelPathGen.configure(activeforeground="black")
        self.LabelPathGen.configure(background="#d9d9d9")
        self.LabelPathGen.configure(cursor="fleur")
        self.LabelPathGen.configure(disabledforeground="#a3a3a3")
        self.LabelPathGen.configure(foreground="#000000")
        self.LabelPathGen.configure(highlightbackground="#d9d9d9")
        self.LabelPathGen.configure(highlightcolor="black")
        self.LabelPathGen.configure(text='''Path to search:''')

        # Txt adresse dossier CAL
        self.txtPathGen = Entry(self.frameGenerate)
        self.txtPathGen.place(x=140, y=40, height=31, width=450)
        self.txtPathGen.configure(background="white")
        self.txtPathGen.configure(disabledforeground="#a3a3a3")
        self.txtPathGen.configure(font="TkFixedFont")
        self.txtPathGen.configure(foreground="#000000")
        self.txtPathGen.configure(highlightbackground="#d9d9d9")
        self.txtPathGen.configure(highlightcolor="black")
        self.txtPathGen.configure(insertbackground="black")
        self.txtPathGen.configure(selectbackground="#c4c4c4")
        self.txtPathGen.configure(selectforeground="black")
        self.txtPathGen.configure(textvariable=calib_support.GenPath)

        # Btn chercher adresse dossier CAL
        self.btnSearchPathGen = Button(self.frameGenerate)
        self.btnSearchPathGen.place(x=600, y=40, height=27, width=38)
        self.btnSearchPathGen.configure(activebackground="#d9d9d9")
        self.btnSearchPathGen.configure(activeforeground="black")
        self.btnSearchPathGen.configure(background="#d9d9d9")
        self.btnSearchPathGen.configure(command=calib_support.OnBtnSearchPath)
        self.btnSearchPathGen.configure(disabledforeground="#a3a3a3")
        self.btnSearchPathGen.configure(foreground="#000000")
        self.btnSearchPathGen.configure(highlightbackground="#d9d9d9")
        self.btnSearchPathGen.configure(highlightcolor="black")
        self.btnSearchPathGen.configure(pady="0")
        self.btnSearchPathGen.configure(text='''...''')

        # Label Mesures
        ###########################################################################################
        self.LabelMes = Label(self.frameGenerate)
        self.LabelMes.place(x=40, y=80, height=21, width=90)
        self.LabelMes.configure(background="#d9d9d9")
        self.LabelMes.configure(disabledforeground="#a3a3a3")
        self.LabelMes.configure(foreground="#000000")
        self.LabelMes.configure(text='''Débits Mesurés''')

        # Txt Mesures
        self.txtMes = Entry(self.frameGenerate)
        self.txtMes.place(x=140, y=80, height=31, width=450)
        self.txtMes.configure(background="white")
        self.txtMes.configure(disabledforeground="#a3a3a3")
        self.txtMes.configure(font="TkFixedFont")
        self.txtMes.configure(foreground="#000000")
        self.txtMes.configure(highlightbackground="#d9d9d9")
        self.txtMes.configure(highlightcolor="black")
        self.txtMes.configure(insertbackground="black")
        self.txtMes.configure(selectbackground="#c4c4c4")
        self.txtMes.configure(selectforeground="black")
        self.txtMes.configure(textvariable=calib_support.Mes)

        # Temp de réf
        ###########################################################################################
        self.LabelTempRef = Label(self.frameGenerate)
        self.LabelTempRef.place(x=40, y=120, height=21, width=90)
        self.LabelTempRef.configure(background="#d9d9d9")
        self.LabelTempRef.configure(disabledforeground="#a3a3a3")
        self.LabelTempRef.configure(foreground="#000000")
        self.LabelTempRef.configure(text='''Temp de réf : ''')

        # Txt Mesures
        self.txtTempRef = Entry(self.frameGenerate)
        self.txtTempRef.place(x=140, y=120, height=31, width=450)
        self.txtTempRef.configure(background="white")
        self.txtTempRef.configure(disabledforeground="#a3a3a3")
        self.txtTempRef.configure(font="TkFixedFont")
        self.txtTempRef.configure(foreground="#000000")
        self.txtTempRef.configure(highlightbackground="#d9d9d9")
        self.txtTempRef.configure(highlightcolor="black")
        self.txtTempRef.configure(insertbackground="black")
        self.txtTempRef.configure(selectbackground="#c4c4c4")
        self.txtTempRef.configure(selectforeground="black")
        self.txtTempRef.configure(textvariable=calib_support.TempRef)


        # Ratio
        ###########################################################################################
        self.LabelRatio = Label(self.frameGenerate)
        self.LabelRatio.place(x=40, y=160, height=21, width=90)
        self.LabelRatio.configure(background="#d9d9d9")
        self.LabelRatio.configure(disabledforeground="#a3a3a3")
        self.LabelRatio.configure(foreground="#000000")
        self.LabelRatio.configure(text='''Ratio : ''')

        # Txt Ratio
        self.txtRatio = Entry(self.frameGenerate)
        self.txtRatio.place(x=140, y=160, height=31, width=450)
        self.txtRatio.configure(background="white")
        self.txtRatio.configure(disabledforeground="#a3a3a3")
        self.txtRatio.configure(font="TkFixedFont")
        self.txtRatio.configure(foreground="#000000")
        self.txtRatio.configure(highlightbackground="#d9d9d9")
        self.txtRatio.configure(highlightcolor="black")
        self.txtRatio.configure(insertbackground="black")
        self.txtRatio.configure(selectbackground="#c4c4c4")
        self.txtRatio.configure(selectforeground="black")
        self.txtRatio.configure(textvariable=calib_support.Ratio)


        # DN
        ###########################################################################################
        self.LabelDN = Label(self.frameGenerate)
        self.LabelDN.place(x=40, y=200, height=21, width=90)
        self.LabelDN.configure(background="#d9d9d9")
        self.LabelDN.configure(disabledforeground="#a3a3a3")
        self.LabelDN.configure(foreground="#000000")
        self.LabelDN.configure(text='''Choix DN : ''')


        # Combo DN
        self.listDN = ttk.Combobox(self.frameGenerate, values = ['DN15', 'DN20'], textvariable=calib_support.DN)
        self.listDN.place(x=140, y=200, height=31, width=450)
        self.listDN.current(0)
        self.listDN.bind("<<ComboboxSelected>>", calib_support.callbackFunc)
        self.listDN.configure(background="white")
        self.listDN.configure(font="TkFixedFont")
        self.listDN.configure(foreground="#000000")
        self.listDN.configure(textvariable=calib_support.DN)


        #  Validation ratio
        self.ValidationRatio = Label(self.frameGenerate)
        self.ValidationRatio.place(x=40, y=240, height=21, width=90)
        self.ValidationRatio.configure(background="#d9d9d9")
        self.ValidationRatio.configure(disabledforeground="#a3a3a3")
        self.ValidationRatio.configure(foreground="#000000")
        self.ValidationRatio.configure(text='''Validation Ratio : ''')

        self.txtValRatio = Entry(self.frameGenerate)
        self.txtValRatio.place(x=140, y=240, height=31, width=450)
        self.txtValRatio.configure(background="white")
        self.txtValRatio.configure(disabledforeground="#a3a3a3")
        self.txtValRatio.configure(font="TkFixedFont")
        self.txtValRatio.configure(foreground="#000000")
        self.txtValRatio.configure(highlightbackground="#d9d9d9")
        self.txtValRatio.configure(highlightcolor="black")
        self.txtValRatio.configure(insertbackground="black")
        self.txtValRatio.configure(selectbackground="#c4c4c4")
        self.txtValRatio.configure(selectforeground="black")
        self.txtValRatio.configure(textvariable=calib_support.ValRatio)

        # Button generate
        ###########################################################################################
        self.btnGenerate = Button(self.frameGenerate)
        self.btnGenerate.place(x=150, y=280, height=24, width=47)
        self.btnGenerate.configure(activebackground="#d9d9d9")
        self.btnGenerate.configure(activeforeground="black")
        self.btnGenerate.configure(background="#d9d9d9")
        self.btnGenerate.configure(disabledforeground="#a3a3a3")
        self.btnGenerate.configure(foreground="#000000")
        self.btnGenerate.configure(highlightbackground="#d9d9d9")
        self.btnGenerate.configure(highlightcolor="black")
        self.btnGenerate.configure(pady="0")
        self.btnGenerate.configure(text='''Generate''')
        self.btnGenerate.bind('<Button-1>',lambda e:calib_support.onBtnGen(e))

        ###########################################################################################
        ### EXIT
        self.btnExit_1 = Button(top)
        self.btnExit_1.place(x=1150, y=700, height=37, width=79)
        self.btnExit_1.configure(activebackground="#d9d9d9")
        self.btnExit_1.configure(activeforeground="black")
        self.btnExit_1.configure(background="#d9d9d9")
        self.btnExit_1.configure(disabledforeground="#a3a3a3")
        self.btnExit_1.configure(foreground="#000000")
        self.btnExit_1.configure(highlightbackground="#d9d9d9")
        self.btnExit_1.configure(highlightcolor="black")
        self.btnExit_1.configure(pady="0")
        self.btnExit_1.configure(text='''Exit''')
        self.btnExit_1.bind('<Button-1>',lambda e:calib_support.OnBtnExit(e))

# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''
    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))
        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')
        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)
        # Copy geometry methods of master  (taken from ScrolledText.py)
        if py3:
            methods = Pack.__dict__.keys() | Grid.__dict__.keys() \
                  | Place.__dict__.keys()
        else:
            methods = Pack.__dict__.keys() + Grid.__dict__.keys() \
                  + Place.__dict__.keys()
        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)

def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))
        container.bind('<Leave>', lambda e: _unbound_to_mousewheel(e, container))
        return func(cls, container, **kw)
    return wrapped

class ScrolledTreeView(AutoScroll, ttk.Treeview):
    '''A standard ttk Treeview widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        ttk.Treeview.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)

import platform
def _bound_to_mousewheel(event, widget):
    child = widget.winfo_children()[0]
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-MouseWheel>', lambda e: _on_shiftmouse(e, child))
    else:
        child.bind_all('<Button-4>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Button-5>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-Button-4>', lambda e: _on_shiftmouse(e, child))
        child.bind_all('<Shift-Button-5>', lambda e: _on_shiftmouse(e, child))

def _unbound_to_mousewheel(event, widget):
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        widget.unbind_all('<MouseWheel>')
        widget.unbind_all('<Shift-MouseWheel>')
    else:
        widget.unbind_all('<Button-4>')
        widget.unbind_all('<Button-5>')
        widget.unbind_all('<Shift-Button-4>')
        widget.unbind_all('<Shift-Button-5>')

def _on_mousewheel(event, widget):
    if platform.system() == 'Windows':
        widget.yview_scroll(-1*int(event.delta/120),'units')
    elif platform.system() == 'Darwin':
        widget.yview_scroll(-1*int(event.delta),'units')
    else:
        if event.num == 4:
            widget.yview_scroll(-1, 'units')
        elif event.num == 5:
            widget.yview_scroll(1, 'units')

def _on_shiftmouse(event, widget):
    if platform.system() == 'Windows':
        widget.xview_scroll(-1*int(event.delta/120), 'units')
    elif platform.system() == 'Darwin':
        widget.xview_scroll(-1*int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.xview_scroll(-1, 'units')
        elif event.num == 5:
            widget.xview_scroll(1, 'units')

if __name__ == '__main__':
    vp_start_gui()





