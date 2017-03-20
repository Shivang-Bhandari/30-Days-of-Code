    stack = []    
    queue = []

    def pushCharacter(self, c):
        self.stack.append(c)

    def popCharacter(self):
        return self.stack.pop()

    def enqueueCharacter(self, c):
        self.queue.insert(0,c)

    def dequeueCharacter(self):
        return self.queue.pop()
