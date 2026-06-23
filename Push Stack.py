
Class Stack:
  
       def_init_(self):
       self.stack = []

    def add(self,datval):
 # use list append method to add element
      if dataval not in self.stack:
             self.stack.append(dataval)
             return True
        else:
             return False
      def peek(self):
             return self.stack[-1]

AStack = Stack()
AStack.add("Mon")
AStack.add("Tue")
AStack.peek()
print(AStack.peek())
AStack.add("Wed")
AStack.add("Thu")
print(AStack.peek())         