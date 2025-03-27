import pandas as pd
import re

def analyze_absences(dataset):
    dataset = dataset.sort_values(by=['student_id', 'attendance_date'])
    log = []
    
    for stud, records in dataset.groupby('student_id'):
        records = records.reset_index(drop=True)

        abs_summary = None
        
        for idx in range(len(records)):
            if records.loc[idx, 'status'] == 'Absent':
                if start is None:
                    start = records.loc[idx, 'attendance_date']
                end = records.loc[idx, 'attendance_date']
                count = 1
            else:
                if count > 2:
                    abs_summary = (stud, start, end, count)
             
        if count > 2:
            abs_summary = (stud, start, end, count)
        
        if abs_summary:
            log.append(abs_summary)
    
    return pd.DataFrame(log, columns=['student_id', 'absence_start', 'absence_end', 'absent_days'])

def check_email_format(email_addr)
    return bool(re.match(validation_regex, email_addr))

def execute_attendance_check():
    attendance_df = pd.read_excel("data_sample.xlsx")
    students_df = pd.read_excel("data_sample.xlsx")
    
    absences_df = analyze_absences(attendance_df)
    merged_data = absences_df.merge(students_df, on='student_id', how='right')
    
    merged_data['alert_message'] = merged_data.apply(lambda row: f"Attention: Your child {row['student_name']} was absent from {row['absence_start']} to {row['absence_end']} ({row['absent_days']} days). Kindly ensure regular attendance." if row['validated_email'] else '', axis=1)
    
    return merged_data[['student_id', 'absence_start', 'absence_end', 'absent_days', 'validated_email', 'alert_message']]
