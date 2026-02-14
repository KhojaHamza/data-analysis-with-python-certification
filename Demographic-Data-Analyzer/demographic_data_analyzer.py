import numpy as np
import pandas as pd
def calculate_demographic_data(print_data=True):
    df = pd.read_csv('adult.data.csv')
    
    race_count = df['race'].value_counts()
    
    average_age_men = round(float(df[df['sex']=='Male']['age'].mean()),2)
    
    percentage_bachelors =round(float((((df['education']=='Bachelors')).sum()/len(df))*100),2)
    
    higher_education_people = (df['education']=='Bachelors') | (df['education']=='Masters') | (df['education']=='Doctorate')
    higher_education_rich = (heigher_education_people & (df['salary'] =='>50K')).sum()
    higher_education_rich_percentage = round(float((higher_education_rich/higher_education_people.sum())*100),2)
    

    lower_education_people = (df['education']!='Bachelors') & (df['education']!='Masters') & (df['education']!='Doctorate')
    lower_education_rich = (lower_education_people & (df['salary'] =='>50K')).sum()
    lower_education_rich_percentage = round(float((lower_education_rich/lower_education_people.sum())*100),2)
    
    min_work_hours = int(df['hours-per-week'].min())
    
    min_work_people = (df['hours-per-week'] == min_work_hours).sum()
    rich_min_work_people = ((df['hours-per-week'] == min_work_hours) &(df['salary']=='>50K')).sum()
    rich_percentage = round(float((rich_min_work_people/ min_work_people)*100),2)
    
    country_rich = df[df['salary']=='>50K']['native-country'].value_counts()
    total_country = df['native-country'].value_counts()
    highest_earning_country = ((country_rich/total_country)*100).idxmax()
    highest_earning_country_percentage = round(float(((country_rich/total_country)*100).max()),2)
    
    rich_occupation_india = df[(df['native-country']=='India') & (df['salary']=='>50K')]['occupation'].value_counts().idxmax()
    
    # your code here
    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich_percentage': higher_education_rich_percentage,
        'lower_education_rich_percentage': lower_education_rich_percentage,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'rich_occupation_india': rich_occupation_india
    }