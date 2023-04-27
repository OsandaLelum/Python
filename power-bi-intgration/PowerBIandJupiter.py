#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install powerbiclient')


# In[2]:


get_ipython().system('pip install powerbiclient --upgrade')


# In[3]:


from powerbiclient import QuickVisualize, get_dataset_config, Report
from powerbiclient.authentication import DeviceCodeLoginAuthentication

import pandas as pd


# In[4]:


from powerbiclient.authentication import DeviceCodeLoginAuthentication

# Define the authentication object
device_auth = DeviceCodeLoginAuthentication()

# Authenticate with Power BI using the device authentication flow
device_auth.authenticate()


# In[ ]:


from powerbiclient.authentication import DeviceCodeLoginAuthentication

# Define the authentication object
device_auth = DeviceCodeLoginAuthentication()

# Get the access token using the device authentication flow
access_token = device_auth.acquire_token()

# Print the access token
print(access_token)


# In[ ]:


df =pd.read_csv('/content/drive/MyDrive/Colab Notebooks/KidneyStones/playground-series-s3e12-publicleaderboard.csv')


# In[ ]:


# Create a Power BI report from your data
PBI_visualize = QuickVisualize(get_dataset_config(df), auth=device_auth)

# Render the new report
PBI_visualize


# In[ ]:


# Import the necessary modules
from powerbiclient import Report, QuickVisualize, get_dataset_config
from powerbiclient.authentication import DeviceCodeLoginAuthentication
import pandas as pd

# Define the authentication object
device_auth = DeviceCodeLoginAuthentication()

# Authenticate with Power BI using the device authentication flow
access_token = device_auth.get_access_token()

# Define the data to be visualized in Power BI
data = {
    'Category': ['Furniture', 'Office Supplies', 'Technology'],
    'Sales': [4425, 5355, 12345]
}

# Create a pandas DataFrame from the data
df = pd.DataFrame(data)

# Create a Power BI report from your data
PBI_visualize = QuickVisualize(get_dataset_config(df), auth=device_auth)

# Render the new report
PBI_visualize

# Alternatively, you can use an existing Power BI report
# Replace 'Report ID' with the ID of your report
#report = Report('Report ID', auth=device_auth)
#report


# In[ ]:


# Import the necessary modules
from powerbiclient import Report, QuickVisualize, get_dataset_config
from powerbiclient.authentication import DeviceCodeLoginAuthentication
import pandas as pd

# Define the authentication object
device_auth = DeviceCodeLoginAuthentication()

# Authenticate with Power BI using the device authentication flow
access_token = device_auth.get_access_token()

# Define the data to be visualized in Power BI
data = {
    'Category': ['Furniture', 'Office Supplies', 'Technology'],
    'Sales': [4425, 5355, 12345]
}

# Create a pandas DataFrame from the data
df = pd.DataFrame(data)

# Create a Power BI report from your data
PBI_visualize = QuickVisualize(get_dataset_config(df), auth=device_auth)

# Add a chart to the report
PBI_visualize.add_chart('ColumnChart', ['Category', 'Sales'])

# Add a table to the report
PBI_visualize.add_table('Table', ['Category', 'Sales'])

# Save the report to Power BI
report_name = 'My Power BI Report'
PBI_visualize.save_report(report_name)

# Alternatively, you can use an existing Power BI report
# Replace 'Report ID' with the ID of your report
report = Report('Report ID', auth=device_auth)

# Add a chart to the report
#report.add_chart('ColumnChart', ['Category', 'Sales'])

# Add a table to the report
report.add_table('Table', ['Category', 'Sales'])

# Update and save the report
report.update()
report.save()

# Render the report in the notebook
report


# In[ ]:


# Authenticate with Power BI using the device authentication flow
from powerbiclient.authentication import DeviceCodeLoginAuthentication

device_auth = DeviceCodeLoginAuthentication()

# Create a Power BI report from your data
from powerbiclient import Report

report = Report(workspace_id='<your_workspace_id>', report_id='<your_report_id>', auth=device_auth)

# Create a visualization using plotly
import plotly.express as px

fig = px.bar(df, x='Category', y='Sales', title='Sales by Category')

# Add the visualization to the report
report.visualize(fig)


# In[ ]:




