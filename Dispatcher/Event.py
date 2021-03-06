class Event(object):

    def __init__(self, event_type, data=None):

        self._type = event_type
        self._data = data


class DbEvent(Event):

    def __init__(self, event_type, id, data=None):

        super(DbEvent, self).__init__(event_type, data)
        self._id = id


