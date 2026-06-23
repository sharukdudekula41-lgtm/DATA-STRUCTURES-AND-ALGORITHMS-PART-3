Class Node:
   def_init_(self,dataval=None):
     self.dataval = dataval
     self.nextval = None

Class SLinkiedList:
     def_init_(self):
         self.headval = None

  def listprint(self):
      printval = self.headval
      while printval is not None:
    print(printval.dataval)
    printval = printval.nextval

list = SLinkiedList()
list.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

# Link first Node to second node
list.headval.nextval = e2

#Link second Node to third node
e2.nextval = e3

list.listprint()