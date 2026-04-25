from oops.demoA import A
from oops.demoB import B

class C(B, A):

    def __init__(self,n1,n2,msg):
        A.__init__(n1,n2)
        #B.__init__(msg)
        super().__init__(self,msg)

    def final(self):
        print('Done')