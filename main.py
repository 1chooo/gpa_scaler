# -*- coding: utf-8 -*-

from scaler.GPA import Scaler

def main() -> None:

    data_path = './assets/score.csv'
    scaler = Scaler(data_path)

    # scaler.show_ATM_graduation_threshold()
    target_semester = '1111'
    scaler.get_semester_info(target_semester)
    scaler.get_total_credits()
    scaler.get_scaler_score()
    scaler.get_original_score()
    scaler.show_ATM_graduation_threshold()
    scaler.show_GPA_scaler_mechanism()


if __name__ == '__main__':

    main()