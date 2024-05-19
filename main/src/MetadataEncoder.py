from json import JSONEncoder


class MetadataEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__
