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

class SerializationToBin(SerializationInterface):

    def serialization(self, *args):
        new_js = json.dumps(args, indent=2)
        return new_js

a = SerializationToBin()
print(a.serialization(data))
b = SerializationToBin()


