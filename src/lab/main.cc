#include <QtGui/QApplication>
#include <QtGui/QMainWindow>

#include "lab/ui/mainwindow.hh"


using namespace lab::ui;


int main(int argc, char **argv)
{
    QApplication app(argc, argv);

    MainWindow mainWindow;

    mainWindow.show();

    return app.exec();
}
