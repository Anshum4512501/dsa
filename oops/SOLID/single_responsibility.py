from enum import Enum
class Journal:
    def __init__(self):
        self.entries = []
        self.count   = 0

    def add_entry(self,text):
        self.entries.append(f"{self.count}:{text}")
        self.count = self.count+1

    def remove_entry(self,pos):
        del self.entries[pos]

    def __str__(self):
        return "\n".join(self.entries)   

# These methods should not be there since single class must have single responsibility 
    def save(self, filename):
        file = open(filename, "w")
        file.write(str(self))
        file.close()

    def load(self, filename):
        pass

    def load_from_web(self, uri):
        pass


class PersistenceManager:
    def save_to_file(self,journal, filename):
        file = open(filename, "w")
        file.write(str(journal))
        file.close()


j = Journal()
j.add_entry("I cried today.")
j.add_entry("I ate a bug.")
print(f"Journal entries:\n{j}\n")
file = r'd:/python_basic_programs/journal.txt'
j.save(file)
# p = PersistenceManager()

# p.save_to_file(j, file)

# verify!
with open(file) as fh:
    print(fh.read())       
