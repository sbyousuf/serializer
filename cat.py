# -*- coding: utf-8 -*-
# Import the necessary modules 
import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np
import os
import arabic_reshaper
from bidi import get_display
import seaborn as sns
# Initialize the lists for X and Y 
data_shab = pd.read_csv("result\\price_mean\\merged.csv") 


# Set the style for Seaborn plots
sns.set_theme(style="whitegrid")

# Create a catplot
plt.figure(figsize=(12, 6),dpi=400)
sns.catplot(data=data_shab,x="'city'", y='homsa',hue="jajiga", kind='count' )  # Replace 'City' and 'Value' with your column names
plt.show()
