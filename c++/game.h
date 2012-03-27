#ifndef GAME_H
#define GAME_H

#include <QObject>

#include <QDir>
#include <QUrl>

#include <QTextDocument>


class Game : public QObject
{
    Q_OBJECT
public:
    explicit Game(QObject *parent = 0);

    QUrl url() const;

    static QString templateDir();

signals:

public slots:

private:
    QDir           m_dir;

    bool           m_modified;

    QTextDocument *m_main_js;

};

#endif // GAME_H
