from ics import Calendar
import requests

url = "https://calendar.google.com/calendar/ical/duk0c7vf58cb9s64mn5ebkgh4c%40group.calendar.google.com/public/basic.ics"

unfollowed_courses = [
    "Application de l'analyse de données, des statistiques descriptives et de l'apprentissage automatique dans l'industrie aéronautique - J. Lacaille",
    "Deep learning V.Lepetit / M. Vakalopoulou",
]

def main():
    c = Calendar(requests.get(url).text)

    def is_event_a_unfollowed_course(event):
        ev = f"{event.name} at {event.begin.naive}"
        for course in unfollowed_courses:
            if course in event.name:
                print(f"Removing {ev}")
                return False
        print(f"Keeping {ev}")
        return True

    c.events = set(filter(is_event_a_unfollowed_course, c.events))
    
    with open('calendar.ics', 'w') as my_file:
        my_file.writelines(c.serialize_iter())

if __name__ == '__main__': 
    main()