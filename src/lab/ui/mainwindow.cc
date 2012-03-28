#include "lab/ui/mainwindow.hh"

#include <QtGui/QMainWindow>
#include <QtGui/QWidget>

#include <QDebug>

#include "lab/project/project.hh"


using namespace lab::ui;


MainWindow::MainWindow(QWidget *widget)
    : QMainWindow(widget),
      _project(new lab::project::Project(this))
{
    setWindowTitle("main.js - Untitled - GameWork Lab");
}