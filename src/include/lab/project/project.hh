#ifndef __LAB__PROJECT__PROJECT_HH__
#define __LAB__PROJECT__PROJECT_HH__

#include <QtCore/QObject>

#include <QtCore/QDir>
#include <QtCore/QUrl>


namespace lab { namespace project {

class Project : public QObject
{
    Q_OBJECT
  
public:
    Project(QObject *parent=0);
    virtual ~Project();

    QUrl indexUrl() const;
    
private:
    void updateTemplateDir();
  
    QDir _base;
    bool _untitled;
};

}}

#endif // __LAB__PROJECT__PROJECT_HH__
