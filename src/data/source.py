from __future__ import annotations
from dataclasses import dataclass
import math
import pandas as pd
import numpy as np
from data.loader import DataSchema
from typing import Optional

# Helper function
def human_format(num):
    if num == 0:
        return "0"

    magnitude = int(math.log(num, 1000))
    mantissa = str(int(num / (1000 ** magnitude)))
    return mantissa + ["", "K", "M", "B", "T", "P"][magnitude]

# Create a dataclass that handles all the logic of the app which is all the pandas operations
@dataclass
class DataSource:
    _data: pd.DataFrame   

    # Filter by month
    def filter(self,
               days: Optional[list[str]]) -> DataSource:

        if days is None:
            days = self.unique_days

        filtered_data = self._data.query('`Day of Week` in @days')

        return DataSource(filtered_data)
    
    
    # Create functions to handle pandas operations needed in callback functions
    # Get Metrics for text cards
    def get_text_data(self) -> list[str]:
        # No. of Patients
        patients = self._data['Patient ID'].count()

        # Average Wait Minutes
        avg_wait_minutes = int(round(self._data['Wait Minutes'].mean(), 0))
        
        #  Avg Consultation Period %
        avg_consultation_period_pct = int(round(self._data['Consultation Period %'].mean(), 0))

        # Average Process Period
        avg_process_period_pct = int(round(self._data['Process Period %'].mean(), 0))
        
        # Financial Class
        financial_class = self._data['Financial Class'].nunique()

        return human_format(patients), avg_wait_minutes, avg_consultation_period_pct, avg_process_period_pct, financial_class


    # Effect of Weekday on Average Wait Minutes
    def get_minutes_per_day_data(self) -> pd.DataFrame:
        weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

        day_data = self._data.pivot_table(
            index=DataSchema.DAY_OF_WEEK, 
            values=[DataSchema.WAIT_MINUTES], 
            aggfunc={DataSchema.WAIT_MINUTES:'mean'}).reset_index()
        day_data[DataSchema.WAIT_MINUTES] = round(day_data[DataSchema.WAIT_MINUTES], 0)
        day_data[DataSchema.DAY_OF_WEEK] = pd.Categorical(day_data[DataSchema.DAY_OF_WEEK], categories=weekdays)
        day_data = day_data.sort_values(DataSchema.DAY_OF_WEEK).reset_index(drop=True)

        return day_data
    

    def get_patient_day_data(self) -> pd.DataFrame:
        weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

        patient_data = self._data.pivot_table(
            index=DataSchema.DAY_OF_WEEK, 
            values=[DataSchema.PATIENT_ID], 
            aggfunc={DataSchema.PATIENT_ID:'count'}).reset_index()
        patient_data[DataSchema.DAY_OF_WEEK] = pd.Categorical(patient_data[DataSchema.DAY_OF_WEEK], categories=weekdays)
        patient_data = patient_data.sort_values(DataSchema.DAY_OF_WEEK, ascending=False).reset_index(drop=True)

        return patient_data
    

    # Effect of Entry Hour on Average Wait Minutes
    def get_entry_hour_minutes(self) -> pd.DataFrame:

        entry_data = self._data.pivot_table(
            index=DataSchema.ENTRY_HOUR,
            values=DataSchema.WAIT_MINUTES,
            columns=DataSchema.DAY_OF_WEEK,
            aggfunc='mean')
        entry_data = entry_data[1:]

        return entry_data
    

    # Get pivot table that shows number of patients and average wait minutes per entry hour
    def get_combo_chart_data(self) -> pd.DataFrame:
        combo_data = self._data.pivot_table(
            index=DataSchema.ENTRY_HOUR,
            values=[DataSchema.WAIT_MINUTES, DataSchema.PATIENT_ID],
            aggfunc={DataSchema.WAIT_MINUTES:'mean', DataSchema.PATIENT_ID:'count'})
        combo_data = combo_data[1:].reset_index()

        return combo_data
    

    # Effect of Weekday on Average Wait Minutes
    def get_day_wait_data(self) -> pd.DataFrame:
        weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

        wait_data = self._data.pivot_table(
            index=DataSchema.DAY_OF_WEEK, 
            values=[DataSchema.WAIT_MINUTES, DataSchema.PATIENT_ID], 
            aggfunc={DataSchema.WAIT_MINUTES:'mean', DataSchema.PATIENT_ID:'count'}).reset_index()
        wait_data[DataSchema.WAIT_MINUTES] = round(wait_data[DataSchema.WAIT_MINUTES], 0)
        wait_data[DataSchema.DAY_OF_WEEK] = pd.Categorical(wait_data[DataSchema.DAY_OF_WEEK], categories=weekdays)
        wait_data = wait_data.sort_values(DataSchema.DAY_OF_WEEK).reset_index(drop=True)

        return wait_data
    

    @property
    def row_count(self) -> int:
        return self._data.shape[0]


    # @property
    # def all_hours(self) -> list[str]:
    #     return self._data[DataSchema.ENTRY_HOUR].tolist()

    @property
    def all_days(self) -> list[str]:
        return self._data[DataSchema.DAY_OF_WEEK].tolist()

    # @property
    # def all_status(self) -> list[str]:
    #     return self._data[DataSchema.BOOKING_STATUS].tolist()
    
    # @property
    # def all_platforms(self) -> list[str]:
    #     return self._data[DataSchema.BOOKING_PLATFORM].tolist()


    # @property
    # def unique_hours(self) -> list[str]:
    #     return sorted(set(self.all_hours))

    @property
    def unique_days(self) -> list[str]:
        return sorted(set(self.all_days))
    
    # @property
    # def unique_status(self) -> list[str]:
    #     return sorted(set(self.all_status))
    
    # @property
    # def unique_platforms(self) -> list[str]:
    #     return sorted(set(self.all_platforms))
    
    
    
