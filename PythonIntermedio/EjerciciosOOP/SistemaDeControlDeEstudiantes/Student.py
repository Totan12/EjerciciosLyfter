class Student():
    def __init__(self, name:str , section:str , spanish:float , english:float , social_studies:float , science:float):
        self.name = name
        self.section = section
        self.spanish = spanish
        self.english = english
        self.social_studies = social_studies
        self.science = science

    def to_dict(self):
        return{
            "name": self.name,
            "section": self.section,
            "spanish": self.spanish,
            "english": self.english,
            "social_studies": self.social_studies,
            "science": self.science
        }
    