CONFIG += qt

INCLUDEPATH = include

unix:DESTDIR = ../build/unix/bin
unix:OBJECTS_DIR = ../build/unix
unix:MOC_DIR = ../build/unix
unix:RCC_DIR = ../build/unix

win32:DESTDIR = ../build/win32/bin
win32:OBJECTS_DIR = ../build/win32
win32:MOC_DIR = ../build/win32
win32:RCC_DIR = ../build/win32

HEADERS += include/lab/project/project.hh \
           include/lab/ui/mainwindow.hh

SOURCES += lab/main.cc \
           lab/project/project.cc \
           lab/ui/mainwindow.cc

RESOURCES += template.qrc