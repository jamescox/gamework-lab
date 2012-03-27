#include "mainwindow.h"

#include "game.h"

#include <QMenuBar>


MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent), m_gameView(new GameViewDock(new Game(this), this))
{
    addDockWidget(Qt::RightDockWidgetArea, m_gameView);
    m_gameView->show();

    menuBar()->addMenu("&View")->addAction(m_gameView->showHideAction());

}
