import pandas as pd

class DataSchema:
    DATE = 'Date'
    FINANCIAL_CLASS = 'Financial Class'
    WAIT_MINUTES = 'Wait Minutes'
    PATIENT_ID = 'Patient ID'
    MONTH = 'Month'
    ENTRY_HOUR = 'Entry Hour'
    CONSULTATION_PERIOD = 'Consultation Period'
    PROCESS_PERIOD = 'Process Period'
    CONSULTATION_PERIOD_PCNT = 'Consultation Period %'
    PROCESS_PERIOD_PCNT = 'Process Period %'
    DAY_OF_WEEK = 'Day of Week'
    PERIODS = 'Periods'
    VALUES = 'Values'


# Create a function that loads the main dataset
def load_data(path: str) -> pd.DataFrame:
    # load the data from the csv file
    data = pd.read_csv(
        path,
        parse_dates=[DataSchema.DATE]

    )

    return data
