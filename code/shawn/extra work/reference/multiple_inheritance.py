#
#   Playing with multiple inheritance
#   "grandparent class"        Z
#   "parent class"            A B 
#   "child class"              C
#   
#   Order of operation: C init start -> A init start -> B init start -> Z init start
#                        -> z init finish -> b init finish -> a init finish  -> c init finish 
# 
#   Good reference for multiple inheritance resolution: https://data-flair.training/blogs/python-multiple-inheritance/
#

class ParentZ:
    def __init__(self):
        print("grandparent z init start")
        super().__init__()
        print("grandparent z init ending")   

class ParentA(ParentZ):
    def __init__(self):
        print("parent a init start")
        super().__init__()
        print("parent a init ending")   

class ParentB(ParentZ):
    def __init__(self):
        print("parent b init start")
        super().__init__()
        print("parent b init ending") 

class Child(ParentA, ParentB):
    def __init__(self):

        print("Child init starting")
        super().__init__()
        print("Child init ending")

c = Child()