
Class queue:

 def_init_(self):
   self.queue = list()

  def addtoq(self,dataval):
# Insert method to add element 
    if dataval not in self.queue:
      self.queue.insert(0,dataval)  
      return True

    return False

  def Size(self):
     return len(Self.queue)

TheQueue = Queue()
TheQueue.addtoq("Mon")
TheQueue.addtoq("Tue")
TheQueue.addtoq("Wed")
Print(TheQueue.Size())    
   