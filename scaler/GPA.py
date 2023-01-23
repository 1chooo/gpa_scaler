import requests
from bs4 import BeautifulSoup


class Scaler:

    pass_ = 'P'
    flunk = 'F'
    standard = 60
    weight = 0
    course = {
        "selected": 0, 
        "required": 1, 
        "elective": 2, 
        "pe"      : 3, 
        "general" : 4,
        "conduct" : 5,
        "service" : 6,
        "summer"  : 7
    }
    topic = [
        "semester",
        "type",
        "course_num",
        "course_name",
        "credits",
        "score",
    ]
    course_credit = 0


    def __init__(self, data_path) -> None:

        self.data_path = data_path
        self.__pre_solving_data()

    def __pre_solving_data(self,) -> list:
        
        self.content = open('./assets/score.csv', 'r', encoding='UTF-8')
        self.df = self.content.readlines()
        self.content.close()

        self.temp = []

        for i in range(0, len(self.df)):
            # print(self.df[i].split(","))
            self.temp.append(self.df[i].split(','))

        self.df = self.temp

        self._score_solving(self.df, 5)

        for i in range(0, len(self.df)):
            print(self.df[i])
        
        return self.df

    def _score_solving(self, df, index) -> list:

        for i in range(0, len(df)):

            
            score_str = str(df[i][index])
            score_str = score_str[0:len(score_str) - 1]
            try:

                score_float = float(score_str)
                df[i][index] = score_float
            except:

                df[i][index] = score_str
                pass
            finally:

                pass

        return df
