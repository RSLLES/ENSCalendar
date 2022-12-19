import re
import requests
from ics import Calendar
from bs4 import BeautifulSoup

url = "https://calendar.google.com/calendar/ical/duk0c7vf58cb9s64mn5ebkgh4c%40group.calendar.google.com/public/basic.ics"

unfollowed_courses = [
    ##################
    ### Semester 1 ###
    ##################

    "Application de l'analyse de données, des statistiques descriptives et de l'apprentissage automatique dans l'industrie aéronautique",
    "Introduction to statistical learning",
    # "Convex optimization A.d'Aspremont",
    "Computational optimal transport",
    "Analyse topologique de données",
    "3D computer vision",
    "Object recognition and computer vision",
    "Introduction to Probabilistic Graphical Models",
    # "Reinforcement Learning M. Pirotta",
    "Apprentissage profond et traitement du signal, introduction et applications industrielles",
    "Image denoising : the human machine competition",
    "Fondamentaux de la recherche reproductible et du logiciel libre",
    "Medical Image Analysis based on generative, geometric and biophysical models",
    #"Geometric Data Analysis",
    "Introduction à l'imagerie numérique",
    "Foundations of distributed and large scale computing optimization",
    "Sub-pixel image processing",
    # "Computational statistics",
    "Responsible Machine Learning",
    "Deep learning V.Lepetit / M. Vakalopoulou",
    "Advanced learning for text and graph data",
    "Introduction à l'apprentissage statistique pour les géosciences",
    "Méthodes mathématiques pour les neurosciences",
    "Séminaire Turing",

    ##################
    ### Semester 2 ###
    ##################

    #"Modèles génératifs pour l'image",
    "Fondements Théoriques de l'apprentissage profond",
    "Deformable models and minimal path methods for image analysis",
    "Graphs in machine learning",
    "Audio signal Analysis, Indexing and Transformations",
    "Deep learning in practice",
    #"Biostatistics",
    "Remote sensing data",
    "Modélisation en neuroscience",
    "Deep Reinforcement learning",
    "Méthodes de séparation de sources pour l'analyse de données en astrophysique",
    "Apprentissage Profond pour la Restauratio",
    "Audio signal processing",
    "Modèles, Information et Physique Statistique",
    "Numerical PDEs for image analysis",
    #"Kernel Methods for machine Learning",
    "Géométrie et espace de formes",
    "Bayesian machine learning",
    "Nuages de points et modélisation 3D",
    "Théorie de la détection",
    "Problèmes inverses et imagerie",
    "The machine intelligence of images",
    #"Algorithms for speech and natural language processing",
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

    regex = re.compile(r"<br/?>", re.IGNORECASE)
    for ev in c.events:
        if ev.description is not None:
            ev.description = BeautifulSoup(re.sub(regex, '\n', ev.description), "html.parser").text
    
    with open('calendar.ics', 'w', encoding='utf-8') as my_file:
        my_file.writelines(c.serialize_iter())

if __name__ == '__main__': 
    main()
