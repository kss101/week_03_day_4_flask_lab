from app.models.event import *

event1 = Event("24/12/2020", "Candle Mass", 6, "Chapel", "Midnight Mass, lit by candle, to usher in Christmas day")
event2 = Event("25/12/2020", "Christmas Day Lunch", 6, "Dining Room", "Traditional Christmas day feast with all the trimmings. Black tie!")
event3 = Event("31/12/2020", "Goodbye 2020!", 6, "Balcony", "Join in with a glass of bubbly and say goodbye to the worst year ever!")

events = [event1, event2, event3]


def add_new_event(event):
    events.append(event)
