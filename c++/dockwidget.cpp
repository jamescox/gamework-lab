#include "dockwidget.h"

#include <QDebug>


DockWidget::DockWidget(QWidget *parent) :
    QDockWidget(parent), m_showHideAction(new QAction(this))
{
    updateActionText();
}

QAction * DockWidget::showHideAction() const
{
    return m_showHideAction;
}

void DockWidget::updateActionText()
{
    if (isVisible()) {
        m_showHideAction->setText(QString("Hide &") + windowTitle());
    } else {
        m_showHideAction->setText(QString("Show &") + windowTitle());
    }
}

void DockWidget::visibilityChanged(bool visible)
{
    qDebug() << "visibilityChanged";

    updateActionText();
}
