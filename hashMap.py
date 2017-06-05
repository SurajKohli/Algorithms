# HashMap Implementation in Python

class HashMap:
    def __init__(self):
        # better if its a prime number
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    # simple modulo function
    def hashfunction(self,key,size):
        return key % size

    # rehash function implements linear probing -> Open addressing to handle collisions
    def rehash(self,oldhash,size):
        return (oldhash+1) % size

    def put(self,key,data):
        hashvalue = self.hashfunction(key, len(self.slots))

        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            # check value of HashMap
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data
            else:
                # calculate rehash
                nextslot = rehash(hashvalue,len(self.slots))
                # find next empty slot which does not have key value
                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    nextslot = rehash(nextslot,len(self.slots))

                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data

    # same linear probing logic as used in put
    def get(self,key):
      # startslot is original position
      startslot = self.hashfunction(key,len(self.slots))
      data = None
      stop = False
      found = False
      position = startslot
      while self.slots[position] != None and not found and not stop:
         # found key, return data
         if self.slots[position] == key:
           found = True
           data = self.data[position]
         else:
           position=self.rehash(position,len(self.slots))
           # returned to original position, item not found
           if position == startslot:
               stop = True
      return data

    def __getitem__(self,key):
        return self.get(key)

    def __setitem__(self,key,data):
        self.put(key,data)

# Driver program
if __name__=='__main__':
    H = HashMap()
    H[22]="suraj"
    H[3]="poga"
    print(H.slots)
    print(H.data)
