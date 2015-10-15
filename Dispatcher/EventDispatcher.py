#source code inspired (copied ...) from http://www.expobrain.net/2010/07/31/simple-event-dispatcher-in-python/
import pdb
class EventDispatcher( object ):

    def __init__(self):

        self._events = {}

    def __del__(self):

        self._events = None

    def hasListener(self, event_type, listener):

        if event_type in self._events.keys():
            return listener in self._events[ event_type ]
        else :
            return False

    def dispatchEvent(self,event):
        if ( event._type in self._events.keys() ):
            listeners = self._events[ event._type ]

            for listener in listeners :
                listener( event )

    def addEventListener(self,event_type, listener):
        if not self.hasListener( event_type, listener) :

            listeners = self._events.get(event_type,[])
            listeners.append( listener )
            self._events[ event_type ] = listeners

    def removeEventListener(self,event_type,listener):

        if self.hasListener(event_type,listener):
            listeners = self._events[ event_type ]

            if len( listeners ) == 1:

                del self._events[ event_type ]

            else :

                listeners.remove( listener )
                self._events[event_type] = listeners

