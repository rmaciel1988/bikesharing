# import seaborn as sns
# import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as ss
import numpy as np

class Utils:
    def __init__(self, df):
        self.df = df.copy()

    def WeekDay(self, wk_num):
        if wk_num == 0:
            return "sunday"
        if wk_num == 1:
            return "monday"
        if wk_num == 2:
            return "tuesday"
        if wk_num == 3:
            return "wednesday"
        if wk_num == 4:
            return "thursday"
        if wk_num == 5:
            return "friday"
        if wk_num == 6:
            return "saturday"

    def DayWeather(self, weasit_num):
        if weasit_num == 1:
            return "clear"
        if weasit_num == 2:
            return "mist"
        if weasit_num == 3:
            return "light snow"
        if weasit_num == 4:
            return "heavy rain"

    def Holiday(self, hol_num):
        if hol_num == 0:
            return "business day"
        if hol_num == 1:
            return "holiday"

    def YearSeason(self, sea_num):
        if sea_num == 1:
            return "winter"
        if sea_num == 2:
            return "spring"
        if sea_num == 3:
            return "summer"
        if sea_num == 4:
            return "fall"

    def Month(self, month_num):
        if month_num == 1:
            return "january"
        if month_num == 2:
            return "february"
        if month_num == 3:
            return "march"
        if month_num == 4:
            return "april"
        if month_num == 5:
            return "may"
        if month_num == 6:
            return "june"
        if month_num == 7:
            return "july"
        if month_num == 8:
            return "august"
        if month_num == 9:
            return "september"
        if month_num == 10:
            return "october"
        if month_num == 11:
            return "november"
        if month_num == 12:
            return "december"

    def NameCategoricals(self):
        """'Inserts categorical values for categorical columns on bike sharing dataset
    Parameters:
    df (pandas dataframe): dataframe to have values modified
    Returns:
    df (pandas dataframe) modified dataframe
    """

        dfres = self.df
        dfres.weekday = dfres.weekday.apply(self.WeekDay)
        dfres.weathersit = dfres.weathersit.apply(self.DayWeather)
        dfres.holiday = dfres.holiday.apply(self.Holiday)
        dfres.mnth = dfres.mnth.apply(self.Month)
        dfres.season = dfres.season.apply(self.YearSeason)

        return dfres


def crammers_v(x,y):
    confusion_matrix = pd.crosstab(x, y)
    chi2 = ss.chi2_contingency(confusion_matrix)[0]
    n = confusion_matrix.sum().sum()
    phi2 = chi2/n
    r, k = confusion_matrix.shape
    phi2corr = max(0, phi2-((k-1)*(r-1))/(n-1))
    rcorr = r-((r-1)**2)/(n-1)
    kcorr = k-((k-1)**2)/(n-1)
    return np.sqrt(phi2corr/min((kcorr-1), (rcorr-1)))
