# -*- coding: utf-8 -*-

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

    gpa_grade_range = [
        100, 89, 84,
        79, 76, 72,
        69, 66, 62, 
        59,
        49,
        0
    ]
    gpa_grade_rank = [
        'A+', 'A', 'A-',
        'B+', 'B', 'B-', 
        'C+', 'C', 'C-', 
        'D',
        'E',
        'X'
    ]
    gpa_grade_scale = [
        4.3, 4.0, 3.7,
        3.3, 3.0, 2.7, 
        2.3, 2.0, 1.7, 
        1.0,
        0.0,
        'X'
    ]
    
    course_credit = 0
    score = 0.0


    def __init__(self, data_path) -> None:

        self.data_path = data_path
        self.__show_project_intro()
        self.__pre_solving_data()


    def __show_project_intro(self, ) -> None:

        print("A brief summary of the project:")
        print("This project will be undertaken during my winter break in 2023.")
        # text = "The primary aim of this project is to develop a tool to scale GPA scores at my university, as the school's current search system only displays the unadjusted scores. Additionally, this project will serve as an opportunity to enhance my understanding of object-oriented programming using the Python language."
        # width = 50

        # for i in range(0, len(text), width):
        #     print(text[i:i+width])

        print('The primary aim of this project is to develop a tool')
        print('to scale GPA scores at my university, as the school\'s')
        print('current search system only displays the unadjusted scores.')
        print('Additionally, this project will serve as an opportunity ')
        print('to enhance my understanding of object-oriented programming')
        print('using the Python language.')
        print()

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
        self._gpa_scaler_mechanism()

        # self._show_df_roughly()
        
        return self.df

    def _show_df_roughly(self, ) -> None:

        for i in range(0, len(self.df)):
            print(self.df[i])

    def _decide_what_to_do(self, command) -> None:

        return

    
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

    def _gpa_scaler_mechanism(self, ) -> None:

        for i in range(0, len(self.df)):
            self.df[i].append('gpa')
            self.df[i].append('scale')

        for i in range(1, len(self.df)):
            score = self.df[i][5]
            try:
                for j in range(len(self.gpa_grade_range) - 1):
                    if score <= self.gpa_grade_range[j] and score > self.gpa_grade_range[j + 1]:
                        self.df[i][6] = self.gpa_grade_rank[j]
                        self.df[i][7] = self.gpa_grade_scale[j]
                        break
                else:
                    if score == self.gpa_grade_range[-1]:
                        self.df[i][6] = self.gpa_grade_rank[-1]
                        self.df[i][7] = self.gpa_grade_rank[-1]
            except TypeError:
                self.df[i][6] = 'NaN'
                self.df[i][7] = 'NaN'


    def show_GPA_scaler_mechanism(self, ) -> None:

        print("The GPA scaler rule in NCU:")
        print()
        print('+----------------------+')
        print("|Range    |Rank |Scale |")
        print("|---------|-----|------|")
        print("|90 ~ 100 | A+  |4.3   |")
        print("|85 ~ 89  | A   |4.0   |")
        print("|80 ~ 84  | A-  |3.7   |")
        print("|77 ~ 79  | B+  |3.3   |")
        print("|73 ~ 76  | B   |3.0   |")
        print("|70 ~ 72  | B-  |2.7   |")
        print("|67 ~ 69  | C+  |2.3   |")
        print("|63 ~ 66  | C   |2.0   |")
        print("|60 ~ 62  | C-  |1.7   |")
        print("|50 ~ 59  | D   |1.0   |")
        print("|1 ~ 49   | E   |0.0   |")
        print("|0        | X   |0.0   |")
        print('+----------------------+')
    
    def get_scaler_score(self, ) -> float:

        self.score = self._count_average_GPA(self.df)
        self._show_scaler_score(self.score)

        return self.score


    def _show_scaler_score(self, score) -> None:

        print('Your scaler score in the university:', score)

    def get_semester_info(self, semester) -> None:

        self.semester = str(semester)
        self.searching_semester = []

        self.searching_semester.append(self.df[0])
        # print(self.searching_semester)
        # print(self.df[0])
        for i in range(1, len(self.df)):

            if (self.df[i][0] == self.semester):

                self.searching_semester.append(self.df[i])
                # print(self.df[i])
        
        self._show_searching_semester_without_course_name(semester)
        # self._show_searching_semester_with_course_name(semester)

    def _show_searching_semester_without_course_name(self, semester) -> None:

        print(f'The semester you want to search is {semester}!\n')
        print('------------------------------------------------------')

        print("|{:<8} |{:<10} |{:<8}|{:<8}|gpa  |scale |".format(             
                self.searching_semester[0][1],
                self.searching_semester[0][2],
                self.searching_semester[0][4],
                self.searching_semester[0][5]))
        print('|---------|-----------|--------|--------|-----|------|')
    
        for i in range(1, len(self.searching_semester)):
            print("|{:<8} |{:<10} |{:<8}|{:<8}|{:<5}|{:<6}|".format(
                self.searching_semester[i][1],
                self.searching_semester[i][2],
                self.searching_semester[i][4],
                self.searching_semester[i][5],
                self.searching_semester[i][6],
                self.searching_semester[i][7]))
        print('------------------------------------------------------')
        print()
        search_gpa = self._count_average_GPA(self.searching_semester)
        print('Your average GPA for this semester we have gotten:', search_gpa)

    def _count_average_GPA(self, target_semester) -> float:

        current_credits = 0
        total_scale = 0.0

        for i in range(1, len(target_semester)):
            if (target_semester[i][7] != 'NaN' and target_semester[i][4] != ''):
                credits = int(target_semester[i][4])
                scale = float(target_semester[i][7])
                current_credits += credits
                total_scale += scale * credits
            
        """
        未完成：
        應該還要考量沒有修完的學分資訊，或者被當掉的學分資訊
        """
        
        # print(current_credits)
        # print(total_scale)

        return round((total_scale / current_credits), 2)

    def _show_searching_semester_with_course_name(self, semester) -> None:

        from tabulate import tabulate

        type_len_max = len(str(self.searching_semester[0][1]))
        course_num_len_max = len(str(self.searching_semester[0][2]))
        course_name_len_max = len(str(self.searching_semester[0][3]))
        credits_len_max = len(str(self.searching_semester[0][4]))
        score_len_max = len(str(self.searching_semester[0][5]))

        for i in range(1, len(self.searching_semester)):

            type_len = len(str(self.searching_semester[i][1]))
            course_num_len = len(str(self.searching_semester[i][2]))
            course_name_len = len(str(self.searching_semester[i][3]))
            credits_len = len(str(self.searching_semester[i][4]))
            score_len = len(str(self.searching_semester[i][5]))

            # print(type_len, course_num_len, course_name_len, credits_len, score_len)

            if type_len > type_len_max:
                type_len_max = type_len
            if course_num_len > course_num_len_max:
                course_num_len_max = course_num_len
            if course_name_len > course_name_len_max:
                course_name_len_max = course_name_len
            if credits_len > credits_len_max:
                credits_len_max = credits_len
            if score_len > score_len_max:
                score_len_max = score_len

        # print(type_len_max, course_num_len_max, course_name_len_max, credits_len_max, score_len_max)

        total = 0
        total += type_len_max
        total += course_num_len_max
        total += course_name_len_max
        total += credits_len_max
        total += score_len_max

        print(f'The semester you want to search is {semester}!\n')
        print('------------------------------------------------')
        print('------------------------------------------------------------')

        print("|{:<8} |{:<10} |{:<60}|{:<8}|{:<8}|gpa  |".format(             
                self.searching_semester[0][1],
                self.searching_semester[0][2],
                self.searching_semester[0][3],
                self.searching_semester[0][4],
                self.searching_semester[0][5]))
        print('|---------|-----------|--------------------------------', end='')
        print('----------------------------|--------|--------|-----|')
    
        for i in range(1, len(self.searching_semester)):
            print("|{:<8} |{:<10} |{:<60}|{:<8}|{:<8}|{:<5}|".format(
                self.searching_semester[i][1],
                self.searching_semester[i][2],
                self.searching_semester[i][3],
                self.searching_semester[i][4],
                self.searching_semester[i][5],
                self.searching_semester[i][6]))
        print('--------------------------------------------------', end='')
        print('----------------------------------------------------------')




    def show_ATM_graduation_threshold(self, ) -> None:

        print("The Department of Atmospheric Science Graduation Threshold in the NCU:")


    def get_total_credits(self, ) -> int:

        self.pass_credits = 0
        self.fail_credits = 0
        self.withdraw_credits = 0
        self.conduct_pass = 0
        self.service_pass = 0
        self.pe_pass = 0

        for i in range(1, len(self.df)):

            try:
                if self.df[i][1] == 'pe':
                    # print(type(self.df[i][4]))
                    self.pe_pass += 1
                elif self.df[i][5] >= 60.0:
                    self.pass_credits += int(self.df[i][4])
                else:
                    self.fail_credits += int(self.df[i][4])

            except TypeError:

                if self.df[i][5] == 'pass':
                    self.service_pass += 1
                    pass
                else:
                    self.withdraw_credits += int(self.df[i][4])
                pass

            except ValueError:

                self.conduct_pass += 1
                pass
            finally:

                pass

        print("pass credits:    ", self.pass_credits)
        print("fail credits:    ", self.fail_credits)
        print("withdraw credits:", self.withdraw_credits)
        print("conduct pass:    ", self.conduct_pass)
        print("service pass:    ", self.service_pass)
        print("pe pass:         ", self.pe_pass)

        return self.pass_credits

    def get_original_score(self, ) -> int:
        
        total = 0
        count = 0
        for i in range(0, len(self.df)):

            try:
                total += self.df[i][5]
                count += 1
            except:
                pass
            finally:
                pass
        
        self.average = total / count
        self.average = (round(self.average, 2))
        print('Your original score in the university:', self.average)

        return self.average