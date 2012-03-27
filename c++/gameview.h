#ifndef GAMEVIEW_H
#define GAMEVIEW_H

#include <QWidget>

#include <QWebView>

class Game;


class GameView : public QWidget
{
    Q_OBJECT
public:
    GameView(Game *game, QWidget *parent = 0);

signals:

public slots:

private:
    Game *m_game;

    QWebView *m_webView;
};

#endif // GAMEVIEW_H
