class Observable( object ):

    def __init__(self):

        self._observers= []

    def register(self, observer):

        if observer not in self._observers:
            self._observers.append(observer)

    def unregister(self,observer):

        if obsever in self._observers:
            self._observers.remove(observer)

    def unregisterAll(self):

        if self._observers:
            del self._observers[:]

    def updateObservers(self):
        for observer in self._observers:
            observer.update()
