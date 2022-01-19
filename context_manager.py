'''
Context managers

class Open_File():
    def __init(self,filename,mode):
        self.filename=filename
        self.mode=mode

    def __enter__(self):
        self.file=open(self.filename,self.mode)
        return self.file

    def __exit__(self,exec_type,exec_val,traceback):
        self.file.close()


from contexlib import contextmanager

@contextmanager
def opn_file(file,mode):
    f=open(file,mode)
    yield f
    f.close()

'''

# with open('sample.txt','w') as f:
#     f.write('this is the sample file to test.')
#
# print(f.closed)

import os
from contextlib import contextmanager

@contextmanager
def change_dir(destination):
    try:
        cwd=os.getcwd()
        os.chdir(destination)
        yield
    finally:
        os.chdir(cwd)



with change_dir('../'):
    print(os.listdir())
