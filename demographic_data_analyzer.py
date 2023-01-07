import pandas as pd

def calculate_demographic_data(print_data = True):
  # Read data from file
  df = pd.read_csv('adult.data.csv')

  # How many of each race are represented in this dataset?
  race_count = df.race.value_counts()

  # What is the average age of men?
  people_age_sex = df[['age','sex']]
  men_age_sex = people_age_sex.loc[people_age_sex['sex'] == 'Male']
  average_age_men = men_age_sex.age.mean().round(1)

  # What is the percentage of people who have a Bachelors degree?
  edu_values = df.education.value_counts()
  percentage_bachelors = ((edu_values['Bachelors'] / edu_values.sum())) * 100
  percentage_bachelors = percentage_bachelors.round(1)

  # What percentage of the people with AND without `education` equal to `Bachelors`, `Masters`, or `Doctorate` also have a `salary` of `>50K` (Note: Every row of data has salary of either '>50K' or '<=50K')?
  salary_edu = df[['education','salary']]
  total = salary_edu.index[:].size
  higher_income = salary_edu.loc[salary_edu['salary'] == '>50K']
  total_higher_income = higher_income.index[:].size
  lower_income = salary_edu.loc[salary_edu['salary'] == '<=50K']
  total_lower_income = lower_income.index[:].size

  higher_ed = salary_edu.loc[salary_edu['education'] == 'Bachelors'].index[:].size
  higher_ed += salary_edu.loc[salary_edu['education'] == 'Masters'].index[:].size
  higher_ed += salary_edu.loc[salary_edu['education'] == 'Doctorate'].index[:].size

  lower_ed = total - higher_ed
  
  higher_education = (higher_ed / total) * 100
  lower_education = (lower_ed / total) * 100
  # with and without `Bachelors`, `Masters`, or `Doctorate`
  higher_education = round(higher_education,1)
  lower_education = round(lower_education,1)

  higher_income_higher_ed = higher_income.loc[higher_income['education'] == 'Bachelors'].index[:].size
  higher_income_higher_ed += higher_income.loc[higher_income['education'] == 'Masters'].index[:].size
  higher_income_higher_ed += higher_income.loc[higher_income['education'] == 'Doctorate'].index[:].size

  higher_income_lower_ed = higher_income.index[:].size - higher_income_higher_ed
  
  higher_education_rich  = higher_income_higher_ed / higher_ed * 100
  lower_education_rich = higher_income_lower_ed / lower_ed * 100
  # percentage with salary >50K
  higher_education_rich = round(higher_education_rich,1)
  lower_education_rich = round(lower_education_rich,1)

  # What is the minumum number of hours a person works per week (hours-per-week feature)?
  # What percentage of the people who work the minumum number of hours per week have a salary of >50K?
  min_work_hours = df[['hours-per-week']].min().values[0]
  work_hours = df[['hours-per-week','salary']]
  num_min_workers = work_hours.loc[work_hours['hours-per-week'] == min_work_hours]
  num_min_workers = num_min_workers.index[:].size

  num_min_rich_workers = work_hours.loc[work_hours['salary'] == ">50K"]
  num_min_rich_workers = num_min_rich_workers.loc[num_min_rich_workers['hours-per-week'] == min_work_hours]
  num_min_rich_workers = num_min_rich_workers.index[:].size

  rich_percentage = (num_min_rich_workers / num_min_workers ) * 100
  # Identify the most popular occupation for those who earn >50K in India. 
  world_plus50K = df[['native-country', 'occupation','salary']]
  
  world_plus50K = world_plus50K.loc[world_plus50K['salary'] == '>50K']
  
  india_plus50K = world_plus50K.loc[world_plus50K['native-country'] == 'India']
  
  desc_india_plus50K_occupation = india_plus50K.occupation.describe()
  
  top_IN_occupation = desc_india_plus50K_occupation.top


  # DO NOT MODIFY BELOW THIS LINE

  if print_data:
    print("Number of each race:\n", race_count)
    print("Average age of men:", average_age_men)
    print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
    print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
    print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
    print(f"Min work time: {min_work_hours} hours/week")
    print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
    print("Top occupations in India:", top_IN_occupation)

  return {'race_count': race_count, 'average_age_men': average_age_men, 'percentage_bachelors': percentage_bachelors, 'higher_education_rich': higher_education_rich, 'lower_education_rich': lower_education_rich, 'min_work_hours': min_work_hours, 'rich_percentage': rich_percentage, 'top_IN_occupation': top_IN_occupation}