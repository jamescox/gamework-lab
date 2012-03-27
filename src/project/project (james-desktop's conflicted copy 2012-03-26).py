import os
import shutil
import stat
import tempfile

from dulwich.errors import NotGitRepository
from dulwich.repo   import Repo

try:
    from PySide.QtCore import QUrl
    from PySide.QtGui  import QPlainTextDocumentLayout, QTextDocument
except ImportError:
    from PyQt4.QtCore import QUrl
    from PyQt4.QtGui  import QPlainTextDocumentLayout, QTextDocument


def now():
    # TODO
    return ''


class Project(object):
    
    def __init__(self, path=None):
        self.__path = path
        self.__temp = None
        
        if path is not None:
            if not os.path.exists(path):
                raise IOError('Project not found')
        
        try:
            self.__repo = Repo(self.path)
        except NotGitRepository:
            self.__repo = Repo.init(self.path)
        
        if not self.is_new:
            self.save('As opend on ' % now())
            
        self.__update_template_files()
        
        main_js = self.__main_js = QTextDocument(open(os.path.join(self.path, 'game', 'main.js')).read())
        main_js.setDocumentLayout(QPlainTextDocumentLayout(main_js))
        
        if self.is_new:
            self.save('Initial version')
        
    
    def __update_template_files(self):
        tpl_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'template'))
        prj_dir = os.path.abspath(self.path)
        
        tpl_index_html = os.path.join(tpl_dir, 'index.html')
        prj_index_html = os.path.join(prj_dir, 'index.html')
        if not os.path.exists(prj_index_html) \
        or (os.stat(tpl_index_html).st_mtime > os.stat(prj_index_html).st_mtime):
            shutil.copy(tpl_index_html, prj_index_html)
            os.chmod(prj_index_html, stat.S_IREAD)
        
        if not os.path.exists(os.path.join(prj_dir, 'game')):
            os.mkdir(os.path.join(prj_dir, 'game'))
        
        tpl_main_js = os.path.join(tpl_dir, 'game', 'main.js')
        prj_main_js = os.path.join(prj_dir, 'game', 'main.js')
        if not os.path.exists(prj_main_js):
            shutil.copy(tpl_main_js, prj_main_js)
    
    
    @property
    def main_js(self): return self.__main_js
    
    
    @property
    def game_url(self):
        return QUrl.fromLocalFile(os.path.join(os.path.abspath(self.path), 'index.html'))
    
    
    @property
    def path(self):
        if self.__path is not None:
            return unicode(self.__path)
        else:
            if self.__temp is None:
                self.__temp = tempfile.mkdtemp()
            
            return unicode(self.__temp)
    
    
    @property
    def is_new(self):
        return bool(self.__temp)
    
    
    def save(self, comment, path=None):
        self.__repo.stage(['index.html', os.path.join('game', 'main.js')])
      
        with open(os.path.join(self.path, 'game', 'main.js'), 'w') as f:
            f.write(self.__main_js.toPlainText())
            
        self.__repo.do_commit(comment)
        
        
    @property
    def current_rev(self):
        id      = self.__repo.head()
        comment = self.__repo.commit(id).message
        
        return (id, comment)
        
        
    def __del__(self):
        if self.is_new:
            shutil.rmtree(self.path)


if __name__ == '__main__':
    p = Project()
    
    print(p.current_rev)
    
    print(p.path, p.is_new)
