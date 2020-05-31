class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.entries.append(f"{self.count}: {text}")
        self.count += 1

    def __str__(self):
        return "\n".join(self.entries)

    # break SRP, things you should not do, a class with multiple responsibility
    def save(self, filename):
        file = open(filename, "w")
        file.write(str(self))
        file.close()


# rather you should have separate class to do other/secondary tasks
class PersistenceManager:
    def save(self, journal, filename):
        file = open(filename, "w")
        file.write(str(journal))
        file.close()


j = Journal()
j.add_entry("I ran today.")
j.add_entry("I ate a road.")
print(f"Journal entries:\n{j}\n")

p = PersistenceManager()
file = './solid/example.txt'
p.save(j, file)

# verify!
with open(file) as fh:
    print(fh.read())
