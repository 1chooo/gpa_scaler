# -*- coding: utf-8 -*-

from scaler.test import Test

def main() -> None:

    print("There are some functions, which do you want to do?")

    return

if __name__ == '__main__':

    main()

    test_data_path = './assets/test_en.csv'
    tt = Test(test_data_path)
    tt.show_data()
