
Class Stack:

    def_init_(self):
      self.stack = []

   def add(self,dataval):
# use list method to add element
    if dataval not in self.stack:
        self.Stack.append(dataval)
        return True
    else:
        return False
# use list pop method to remove element
   def remove(self):
     if len(self.stack) <=0:
        return("No element in the Stack")
   else:
    return self.stack.pop()

 AStack = Stack()
 Astack.add("Mon")
 AStack.add("Tue")
 AStack.add("Wed")
 AStack.add("Thu")
Print(AStack.remove())
Print(AStack.remove())     

