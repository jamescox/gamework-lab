#ifndef __LAB__UI__MAINWINDOW_HH__
#define __LAB__UI__MAINWINDOW_HH__

#include <QtGui/QMainWindow>
#include <QtGui/QWidget>


namespace lab { namespace project { class Project; } }


namespace lab { namespace ui {

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *widget=0);
    
private:
    lab::project::Project *_project;
};

}}

#endif // __LAB__UI__MAINWINDOW_HH__