#include "lab/project/project.hh"

#include <QtCore/QUuid>
#include <QtCore/QDir>
#include <QtCore/QFileInfo>
#include <QtCore/QUrl>

#include <QDebug>


using namespace lab::project;


// Taken from:
//    http://john.nachtimwald.com/2010/06/08/qt-remove-directory-and-its-contents/
static bool removeDir(const QString &dirName)
{
    bool result = true;
    QDir dir(dirName);

    if (dir.exists(dirName)) {
        Q_FOREACH(QFileInfo info, dir.entryInfoList(QDir::NoDotAndDotDot | QDir::System | QDir::Hidden  | QDir::AllDirs | QDir::Files, QDir::DirsFirst)) {
            if (info.isDir()) {
                result = removeDir(info.absoluteFilePath());
            }
            else {
                result = QFile::remove(info.absoluteFilePath());
            }

            if (!result) {
                return result;
            }
        }
        result = dir.rmdir(dirName);
    }

    return result;
}


Project::Project(QObject *parent)
    : QObject(parent), _untitled(true)
{
    _base.cd(QDir::tempPath());

    QUuid uuid;
    do {
      uuid = QUuid::createUuid();
    } while (!_base.mkdir(uuid.toString().mid(1, 36)));

    _base.cd(uuid.toString().mid(1, 36));
    _base = QDir(_base.absolutePath());

    updateTemplateDir();
}

Project::~Project()
{
    if (_untitled) {
        removeDir(_base.path());
    }
}


QUrl Project::indexUrl() const
{
    return QUrl::fromLocalFile(_base.filePath("index.html"));
}


void Project::updateTemplateDir()
{
    QFileInfo gameFi(_base.filePath("game"));
    if (gameFi.isFile()) {
        _base.remove("game");
    }
    if (!gameFi.exists()) {
        _base.mkdir("game");
    }

    QFileInfo gameMainJsFi(_base.filePath("game/main.js"));
    if (!gameMainJsFi.exists()) {
        QFile(":/main.js").copy(_base.filePath("game/main.js"));
    }

    QFile(":/index.html").copy(_base.filePath("index.html"));
}