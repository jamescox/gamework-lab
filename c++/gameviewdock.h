#ifndef GAMEVIEWDOCK_H
#define GAMEVIEWDOCK_H

#include "dockwidget.h"

#include "gameview.h"


class GameViewDock : public DockWidget
{
    Q_OBJECT
public:
    GameViewDock(Game *game, QWidget *parent = 0);

private:
    GameView *m_gameView;
};

#endif // GAMEVIEWDOCK_H
