
#import and tidy data
    #after this we will prob have a better idea for EDV and ML applications

#FOR EDA/EDV FIGURES
    #age groups
    #race
    #sex
    #income (if available in data)


#ML APPLICATIONS
    #

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#INTRODUCTION
    #talk about covid and stuff. significance blah blah blah

#DATA COLLECTION

#data from
china_data = pd.read_csv("COVID19_open_line_list[1].csv")

#Shows number of cases from locations around the world from 1/22/20 - 11/15/20
world_cases_time_data = pd.read_csv("time_series_covid_19_confirmed[1].csv")

#Shows number of cases from locations around the USA from 1/22/20 - 11/15/20
US_cases_time_data = pd.read_csv("time_series_covid_19_confirmed_US[1].csv")

#Shows number of deaths from locations around the world from 1/22/20 - 11/15/20
world_death_time_data = pd.read_csv("time_series_covid_19_deaths[1].csv")

#Shows number of deaths from locations around the USA from 1/22/20 - 11/15/20
US_death_time_data = pd.read_csv("time_series_covid_19_deaths_US[1].csv")

#Shows number of recovered cases from locations around the world from 1/22/20 - 11/15/20
world_recover_data = pd.read_csv("time_series_covid_19_recovered[1].csv")

print(china_data.head(20))


#DATA PROCESSING
    #theres a bunch of useless columns, so we should get rid of them here.


#EXPLORATORY DATA ANALYSIS
    #not sure what EDA even means

#DATA VISUALIZATION
    #hello

#MODEL CREATION AND ANALYSIS

#CONCLUSION AND INTERPRETATION