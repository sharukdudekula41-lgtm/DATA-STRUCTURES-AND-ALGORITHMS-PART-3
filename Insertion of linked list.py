Class Node:
    def_init_(self,dataval=None):
     self.dataval = dataval
     self.nextval = None

Class SlinkedList:
     def_init_(self):
        self.headval = None

# Print the linked list
   def listprint(self):
      printval = self.headval
     while printval is not None:
         print(printval.dataval)
         printval = printval.nextval
     def AtBegining(self,newdata):
          NewNode = Node(newdata)

 # update the new next val to existing node
      NewNode.nextval = self.headval
      self.headval = NewNode

list = SLinkedList()
list.headval = Node("Mon")
e2= Node("Tue")
e3=Node("Wed")
list.headval.nextval = e2
e2.nextval = e3

list.AtBegining("Sun")
list.listprint()
