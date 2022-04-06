
    def set(self , key , value):
        try:
            self.db[str(key)] = value
            self.dumpdb()
            return True
        except Exception as e:
            print("[X] Error Saving Values to Database : " + str(e))
            return False

    def get(self , key):
        try:
            return self.db[key]
        except KeyError:
            print("No Value Can Be Found for " + str(key))  
            return False

    def delete(self , key):
        if not key in self.db:
            return False
        del self.db[key]
        self.dumpdb()
        return True
