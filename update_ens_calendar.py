from ics import Calendar
import requests

url = "https://calendar.google.com/calendar/ical/duk0c7vf58cb9s64mn5ebkgh4c%40group.calendar.google.com/public/basic.ics"

unfollowed_courses = [
    "Application de l'analyse de données, des statistiques descriptives et de l'apprentissage automatique dans l'industrie aéronautique - J. Lacaille",
    "Introduction to statistical learning",
    # "Convex optimization A.d'Aspremont",
    # "Computational optimal transport G.Peyré",
    "Analyse topologique de données J. Tierny, F. Chazal",
    # "3D computer vision P.Monasse, M.Aubry",
    "Reconnaissance d'objets et vision artificielle",
    "Introduction to Probabilistic Graphical Models",
    # "Reinforcement Learning M. Pirotta",
    "Apprentissage profond et traitement du signal, introduction et applications industrielles - T. Courtat",
    "Image denoising : the human machine competition JM.Morel, G.Facciolo, P.Arias",
    "Fondamentaux de la recherche reproductible et du logiciel libre - M. Colom Barco",
    "Medical Image Analysis based on generative, geometric and biophysical models - H.Delingette, X.Pennec",
    "Geometric Data Analysis - J. Feydy",
    "Introduction à l'imagerie numérique Y.Gousseau, J.Delon",
    "Foundations of distributed and large scale computing optimization - E.Chouzenoux",
    "Sub-pixel image processing",
    "Computational statistics S.Allassonnière",
    "Responsible Machine Learning - N. Vayatis, D. Abu Elyounes, T. Evgeniou, M. Garin",
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