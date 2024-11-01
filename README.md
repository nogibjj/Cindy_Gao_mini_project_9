[![Format](https://github.com/nogibjj/Cindy_Gao_mini_project_9/actions/workflows/format.yml/badge.svg)](https://github.com/nogibjj/Cindy_Gao_mini_project_9/actions/workflows/format.yml)
[![Install](https://github.com/nogibjj/Cindy_Gao_mini_project_9/actions/workflows/install.yml/badge.svg)](https://github.com/nogibjj/Cindy_Gao_mini_project_9/actions/workflows/install.yml)
[![Lint](https://github.com/nogibjj/Cindy_Gao_mini_project_9/actions/workflows/lint.yml/badge.svg)](https://github.com/nogibjj/Cindy_Gao_mini_project_9/actions/workflows/lint.yml)
[![Test](https://github.com/nogibjj/Cindy_Gao_mini_project_9/actions/workflows/test.yml/badge.svg)](https://github.com/nogibjj/Cindy_Gao_mini_project_9/actions/workflows/test.yml)

# Week 9: Cloud-Hosted Notebook Data Manipulation
## Purpose of the project:
* Set up a cloud-hosted Jupyter Notebook using Google Colab
* Perform data manipulation tasks on a sample dataset <br><br>
## Google Colab Url:
https://colab.research.google.com/drive/1fCvkYBdmV16EmXar1vRnTKpUr2S7WRnA#scrollTo=MG8Dnx667P3P <br><br>

## Project Structure:
CINDY_GAO_MINI_PROJECT_9
├── __pycache__
├── .devcontainer
│   ├── devcontainer.json
│   └── Dockerfile
├── .github
│   └── workflows
│       ├── format.yml
│       ├── install.yml
│       ├── lint.yml
│       └── test.yml
├── .pytest_cache
├── mylib
│   ├── __pycache__
│   ├── __init__.py
│   └── lib.py
├── .coverage
├── .gitignore
├── Change_in_Murder_Rates_by_State_in_2015.png
├── Dockerfile
├── figure.png
├── Histogram_of_Murders_2014_2015.png
├── LICENSE
├── main.ipynb
├── main.py
├── Makefile
├── README.md
├── repeat.sh
├── report.md
├── requirements.txt
├── setup.sh
├── test_lib.py
└── test_main.py


## Data visualization
__raw data:__ https://raw.githubusercontent.com/fivethirtyeight/data/master/murder_2016/murder_2015_final.csv <br><br>
__Description for the data:__
|       |   2014_murders |   2015_murders |    change |
|:------|---------------:|---------------:|----------:|
| count |        83      |        83      |  83       |
| mean  |        65.747  |        75.4819 |   9.73494 |
| std   |        79.0112 |        91.6843 |  21.8588  |
| min   |         0      |         1      | -19       |
| 25%   |        19.5    |        22.5    |  -3       |
| 50%   |        32      |        39      |   4       |
| 75%   |        82      |        94      |  14       |
| max   |       411      |       478      | 133       |<br><br>


__Histogram of Murders in 2014 and 2015:__
![Histogram](Histogram_of_Murders_2014_2015.png)<br><br>

__Change in Murder Rates by State in 2015:__
![Line Chart](Change_in_Murder_Rates_by_State_in_2015.png)







