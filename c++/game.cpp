#include "game.h"

#include <QApplication>
#include <QDir>

#include <QDebug>
#include <QMessageBox>


Game::Game(QObject *parent) :
    QObject(parent)
{
}


QUrl Game::url() const
{
    QDir dir(templateDir());

    qDebug() << dir.absoluteFilePath("index.html");

    return QUrl::fromLocalFile(dir.absoluteFilePath("index.html"));
}


QString Game::templateDir()
{
    QDir dir(QApplication::applicationDirPath());

    if (dir.cd("template")) {
        return dir.absolutePath();
    } else {
        if (dir.cd("/usr/share/gamework/template")) {
            return dir.path();
        }
    }

    QMessageBox::critical(NULL, "Error", "Could not find the template directory", QMessageBox::Ok);
    ::exit(1);

    return "";
}
