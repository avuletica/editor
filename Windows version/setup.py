# setup skripta za py2exe program, služi za automatsko traženje i dodavanje librarya te kompajlanje aplikacije
# na taj način nisu potrebne dodatne instalacije qt-a, pyqt-a ili pythona kad se program pokreće na drugom kompjuteru
from distutils.core import setup
import py2exe

#Mydata_files = [('Folder', ['D:\Ceditor project\Windows version\Resources'])]
setup(windows=[{"script":"windows.py","icon_resources": [(1, "myicon.ico")]}], \
    options={"py2exe":{"includes":["sip"], "compressed":2, "optimize":2, "bundle_files": 1}}, zipfile=None)

    # navodi koja skripta je glavna za pokretanje kao "main()" u c/c++, koje librarye želim dodati, da ih bundla (smanji broj fileova što više)
    # te da ne zippira
