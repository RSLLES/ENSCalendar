from ics import Calendar
import requests

url = "https://calendar.google.com/calendar/ical/duk0c7vf58cb9s64mn5ebkgh4c%40group.calendar.google.com/public/basic.ics"

unfollowed_courses = [
    "Application de l'analyse de données, des statistiques descriptives et de l'apprentissage automatique dans l'industrie aéronautique",
    "Introduction to statistical learning",
    # "Convex optimization A.d'Aspremont",
    # "Computational optimal transport G.Peyré",
    "Analyse topologique de données",
    # "3D computer vision P.Monasse, M.Aubry",
    "Reconnaissance d'objets et vision artificielle",
    "Introduction to Probabilistic Graphical Models",
    # "Reinforcement Learning M. Pirotta",
    "Apprentissage profond et traitement du signal, introduction et applications industrielles",
    "Image denoising : the human machine competition",
    "Fondamentaux de la recherche reproductible et du logiciel libre",
    "Medical Image Analysis based on generative, geometric and biophysical models",
    "Geometric Data Analysis",
    "Introduction à l'imagerie numérique",
    "Foundations of distributed and large scale computing optimization",
    "Sub-pixel image processing",
    "Computational statistics",
    "Responsible Machine Learning",
    "Deep learning V.Lepetit / M. Vakalopoulou",
    "Advanced learning for text and graph data",
    "Introduction à l'apprentissage statistique pour les géosciences",
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