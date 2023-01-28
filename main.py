# -*- coding: utf-8 -*-

from scaler.GPA import Scaler

def main() -> None:

    print("Intro to the project:")
    print("There are some functions, which do you want to do?")

    return

if __name__ == '__main__':


    data_path = './assets/score.csv'
    scaler = Scaler(data_path)

    # scaler.show_ATM_graduation_threshold()
    scaler.get_semester_info(1111)