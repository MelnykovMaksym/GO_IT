from datetime import date
from GO_IT.homework_9.contacts import Contacts
from contacts import Session, engine, Base


Base.metadata.create_all(engine)

session = Session()

new_user = Contacts("Maks", "+380951447078", date(2021, 11, 5), 'saunbeam@gmail.com', 1, "blabla")
session.add(new_user)
session.commit()
session.close()

