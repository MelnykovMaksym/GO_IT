import json
from abc import abstractmethod, ABCMeta
str_json = """{
  "name": "John",
  "age": 30,
  "isAdministrator": false,
  "courses": ["html", "css", "js"],
  "wife": null
}"""
data = json.loads(str_json)

class SerializationInterface(metaclass=ABCMeta):
    @abstractmethod
    def serialization(self):
        pass
    @abstractmethod
    def deserialization(self):
        pass

class SerializationToBin(SerializationInterface):

    def serialization(self, *args):
        return json.dumps(args, indent=2)

    def deserialization(self, *args):
        return json.loads()


a = SerializationToBin()
print(a.serialization(data))
print(a.serialization(str_json))


