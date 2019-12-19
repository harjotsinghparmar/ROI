#!/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd 
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt



class cohort_analysis():
    """
    Takes input as unique CustomerID and ActivityDate, 
    Activity could be anything from transactions to clicks,
    any KPI that is worth measuring 

    Attributes:
    CustomerID: unique id 
    ActivityDate: datetime of activity
    """

    def __init__(self,input_df=None,CustomerID='CustomerID',ActivityDate='ActivityDate'):

        """
        Instantiate the cohort object 
        with data attributes to be used
        """ 
        if(ActivityDate not in input_df.columns):
            raise Exception('Invalid Activity Date column name, Please provide valid column name')
        self.customer_id_column = CustomerID
        self.conversion_date_column = ActivityDate
        self.input_df = input_df
        self.cohort_table = None
        self.retention_table= None
        self.pivoted = None
        self.analyze()

    def assign_id(self,df):
        """
        helper function used to assign cohort ids
        """
        df['Cohort_ID']=np.arange(len(df))+1
        return df

    def analyze(self):
        """
        method used to create cohort and perform cohort analysis
        """
        self.input_df['Purchase_month'] = self.input_df[self.conversion_date_column].apply(lambda x: x.to_period('M'))
        if(1):
            print('Creating Cohorts')
            # create cohort based on first month, if cohort is not known 
            first_month_df = self.input_df.groupby(self.customer_id_column)[self.conversion_date_column].apply(lambda x: min(x).to_period('M'))
            merged_df = pd.merge(self.input_df,first_month_df,on=self.customer_id_column).rename(columns={self.conversion_date_column+'_y':'Cohort'})
            pivoted = merged_df.pivot_table(index=['Cohort','Purchase_month'],values=[self.customer_id_column],aggfunc={self.customer_id_column:pd.Series.nunique})
            self.pivoted=pivoted.groupby(['Cohort']).apply(self.assign_id)
            self.cohort_table = self.pivoted.pivot_table(index=['Cohort'],columns=['Cohort_ID'])
            self.retention_table =self.cohort_table[self.customer_id_column].divide(self.cohort_table[self.customer_id_column][1],axis='rows')
        return self.cohort_table


    def plot_retention(self,cmap='RdYlBu'):
        """
        Method used to plot retention rate
        """
        sns.set(style='white')
        fig,ax = plt.subplots(figsize=self.retention_table.shape)
        sns.heatmap(self.retention_table,annot=True,fmt='.0%',cmap=cmap)
        ax.xaxis.tick_top()
        ax.xaxis.set_label_position('top') 



