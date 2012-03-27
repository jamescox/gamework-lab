#include "gameviewdock.h"

#include "game.h"


GameViewDock::GameViewDock(Game *game, QWidget *parent) :
    DockWidget(parent), m_gameView(new GameView(game, this))
{
    setWidget(m_gameView);

    setWindowTitle("Player");
}
