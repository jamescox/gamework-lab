#include "gameview.h"

#include <QVBoxLayout>
#include <QWebView>

#include "game.h"


GameView::GameView(Game *game, QWidget *parent) :
    QWidget(parent), m_game(game), m_webView(new QWebView(this))
{
    QVBoxLayout *layout = new QVBoxLayout(this);

    layout->setMargin(0);
    layout->addWidget(m_webView);

    m_webView->load(game->url());

    setLayout(layout);
}
