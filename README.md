# GPA Scaler


[![project badge](https://img.shields.io/badge/1chooo-gpa__scaler-informational)](https://github.com/1chooo/gpa_scaler)
[![Made with Python](https://img.shields.io/badge/Python->=3.6-blue?logo=python&logoColor=white)](https://python.org "Go to Python homepage")
[![License](https://img.shields.io/badge/License-MIT-blue)](./LICENSE "Go to license section")

## A brief summary of the project

This project will be undertaken during my winter break in 2023.

The primary aim of this project is to develop a tool to scale GPA scores at my university, as the school's current search system only displays the unadjusted scores. Additionally, this project will serve as an opportunity to enhance my understanding of object-oriented programming using the Python language.

## GPA Standard in NCU


|  Range   | Rank  | Scale |
| :------: | :---: | :---: |
| 90 ~ 100 |  A+   |  4.3  |
| 85 ~ 89  |   A   |  4.0  |
| 80 ~ 84  |  A-   |  3.7  |
| 77 ~ 79  |  B+   |  3.3  |
| 73 ~ 76  |   B   |  3.0  |
| 70 ~ 72  |  B-   |  2.7  |
| 67 ~ 69  |  C+   |  2.3  |
| 63 ~ 66  |   C   |  2.0  |
| 60 ~ 62  |  C-   |  1.7  |
| 50 ~ 59  |   D   |  1.0  |
|  1 ~ 49  |   E   |  0.0  |
|    0     |   X   |  0.0  |

``` python 
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
```

## The functions of this project:

``` py
from scaler.GPA import Scaler

data_path = './assets/score.csv'
scaler = Scaler(data_path)
```
1. ### Show the GPA rule in NCU
    ``` py
    scaler.show_GPA_scaler_mechanism()
    ```
2. ### Show the graduation threshold at ATM in NCU
    ``` py
    scaler.show_ATM_graduation_threshold()
    ```

3. ### Get the information of the score
    #### Show the original score.
    ```
    scaler.get_original_score()
    ```
    #### Show the scaling score.
    ```
    scaler.get_scaler_score()
    ```
    #### Get the semester info with GPA Scaler
    ``` py
    target_semester = '1111'      # the target semester you want to check
    scaler.get_semester_info(target_semester)
    ```

## License

Released under [MIT](./LICENSE) by [@1chooo](https://github.com/1chooo).

- This software can be modified and reused without restriction.
- The original license must be included with any copies of this software.
- If a significant portion of the source code is used, please provide a link back to this repository.