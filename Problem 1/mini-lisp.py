# -*- coding: utf-8 -*-
from yacc import yacc, lisp_str
import cmd

class MiniLisp(cmd.Cmd):     # See https://docs.python.org/2/library/cmd.html
    """
    MiniLisp evalúa expresiones sencillas con sabor a lisp, 
    más información en http://www.juanjoconti.com.ar
    """

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = "ml> "
        self.intro  = "Bienvenido a MiniLisp"

    def do_exit(self, args):
        """Exits from the console"""
        return -1

    def do_EOF(self, args):
        """Exit on system end of file character"""
        print "Good bye!"
        return self.do_exit(args)

    def do_help(self, args):
        print self.__doc__

    def emptyline(self):    
        """Do nothing on empty input line"""
        pass

    def default(self, line):       
        """Called on an input line when the command prefix is not recognized.
           In that case we execute the line as Python code.
        """
        result = yacc.parse(line)
        print "AST is: ", result
        import lis
        r =  lis.eval(result)
        if r is not None: print r
        '''
        s = lisp_str(result)
        if s != 'nil':
            print s
        '''

if __name__ == '__main__':
        ml = MiniLisp()
        ml.cmdloop()     # See https://docs.python.org/2/library/cmd.html

'''
(exec 'from UT import teacher; tea = teacher(); toReturn = tea.run("name")')
(exec 'from UT import teacher; tea = teacher(); toReturn = tea.run("$name")("Cannata")')
(exec 'from UT import substitute; sub = substitute (); toReturn = sub.run("name")')
(exec 'from UT import substitute; sub = substitute (); toReturn = sub.run("$name")("   ")')
(exec 'from UT import teacher; tea = teacher(); toReturn = tea.run("course")')

# you can change the list to your desire
(map* '(1 2 3 4 5) 5)
(map+ '(1 2 3 4 5) 5)
(map- '(1 2 3 4 5) 5)
(mapdiv '(1 2 3 4 5) 2)

(exec 'from emp_cust import s_dept; toReturn = [[i[0],i[1],i[2]] for i in s_dept[1::]]')

(exec 'import ListComprehension; ListComprehension.streamOps()')
'''