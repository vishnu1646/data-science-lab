import pandas as pd
student_marks=pd.Series({'vijaya':80,'rahul':92,'meghana':67,'radhika':95,'shreya':97})
student_age=pd.Series({'vijaya':32,'rahul':28,'meghana':30,'radhika':25,'shreya':20})
student_df=pd.DataFrame({'marks':student_marks,'age':student_age})
print(student_df)
print(student_df.sort_values(by=['marks']))
print(student_df.sort_values(by=['marks'],ascending=False))