Class Node:

   def_init_(self,dataval=None):
       self.dataval = dataval
      self.nextval = None


 Class SLinkedList:
      def_init_(self):
         self.headval = None

list1 = SLinkedList()
list1.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
# Link first Node to second node

list1.headval.nextval = e2

# Link second to third node
e2.nextval = e3