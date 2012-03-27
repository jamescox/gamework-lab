#ifndef DOCKWIDGET_H
#define DOCKWIDGET_H

#include <QDockWidget>

#include <QAction>


class DockWidget : public QDockWidget
{
    Q_OBJECT
public:
    explicit DockWidget(QWidget *parent = 0);

    QAction * showHideAction() const;

    virtual void visibilityChanged(bool visible);

signals:

public slots:

private:
    void updateActionText();

    QAction *m_showHideAction;
};

#endif // DOCKWIDGET_H
