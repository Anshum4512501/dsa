
class Super:
    def method(self):
        print("Super Method")
    def delegate(self):
        pass
        # self.action()


class Inheritor(Super):
    pass

class Replacer(Super):

    def method(self):
        print("Replacer method")

class Extender(Super):
    def method(self):
        print('starting Extender.method') 
        Super.method(self)
        print('ending Extender.method')
class Provider(Super):
    # Fill in a required method
    def action(self):
        print('in Provider.action')
        
if __name__ == '__main__':
    for klass in (Inheritor, Replacer, Extender):
        print('\n' + klass.__name__ + '...')
        klass().method()
        print('\nProvider...')
        x = Provider()
        x.delegate()