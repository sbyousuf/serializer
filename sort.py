# -*- coding: utf-8 -*-
# Import the necessary modules
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
import arabic_reshaper
from bidi import get_display
import matplotlib.font_manager as fm


# Load the data
data_shab = pd.read_csv("result\\price_median\\shab.csv", encoding='utf-8')
data_jajiga = pd.read_csv('result\\price_median\\jajiga.csv', encoding='utf-8')
data_otaghak = pd.read_csv('result\\price_median\\otaghak.csv', encoding='utf-8')
data_homsa = pd.read_csv('result\\price_median\\homsa.csv', encoding='utf-8')

# Convert to DataFrames
df_shab = pd.DataFrame(data_shab)
def_jajiga = pd.DataFrame(data_jajiga)
def_otaghak = pd.DataFrame(data_otaghak)
def_homsa = pd.DataFrame(data_homsa)

# Prepare X-axis labels
X1 = list(def_homsa.iloc[:, 0])
text_to_be_reshaped = []

for i in X1:
    unicode_text_reshaped = arabic_reshaper.reshape(i)
    unicode_text_reshaped_RTL = get_display(unicode_text_reshaped, base_dir='R')
    text_to_be_reshaped.append(unicode_text_reshaped_RTL)

# Prepare Y-axis values
Y_otaghak = list(def_otaghak.iloc[:, 1])
Y_shab = list(df_shab.iloc[:, 1])
Y_jajiga = list(def_jajiga.iloc[:, 1])
Y_homsa = list(def_homsa.iloc[:, 1])

# Set up positions for bars
X = np.arange(len(X1))

# Configure Matplotlib to use B Nazanin font
persian_font = {'fontname': 'B Nazanin'}

# Plot
plt.figure(figsize=(14, 7))  # Adjust figure size for better readability
bar_width = 0.2
opacity = 0.8

plt.bar(X, Y_homsa, color="green", label=get_display(arabic_reshaper.reshape("هومسا"), base_dir='R'), width=bar_width, edgecolor='black', alpha=opacity)
plt.bar(X + bar_width, Y_jajiga, color="darkred", label=get_display(arabic_reshaper.reshape("جاجیگا"), base_dir='R'), width=bar_width, edgecolor='black', alpha=opacity)
plt.bar(X + 2 * bar_width, Y_otaghak, color="crimson", label=get_display(arabic_reshaper.reshape("اتاقک"), base_dir='R'), width=bar_width, edgecolor='black', alpha=opacity)
plt.bar(X + 3 * bar_width, Y_shab, color="darkblue", label=get_display(arabic_reshaper.reshape("شب"), base_dir='R'), width=bar_width, edgecolor='black', alpha=opacity)

# Add titles and labels
plt.title(get_display(arabic_reshaper.reshape("میانه قیمت ها در هر شهر"), base_dir='R'), fontsize=24,**persian_font)
plt.xlabel(get_display(arabic_reshaper.reshape("شهرها"), base_dir='R'), fontsize=18,**persian_font)
plt.ylabel(get_display(arabic_reshaper.reshape("میانه قیمت ها"), base_dir='R'), fontsize=18,**persian_font)
plt.xticks(X + 1.5 * bar_width, text_to_be_reshaped, rotation=45, fontsize=15, ha='right', color="black",**persian_font)
plt.yticks(fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)  # Add grid lines for better readability

# Place legend outside the plot
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=15,prop={"family":'B Nazanin','size':15})

# Save and show plot
result_dir = "result\\price_median"
file_path = os.path.join(result_dir, "price_median.png")
plt.tight_layout()
plt.savefig(file_path, bbox_inches='tight', dpi=400)
plt.show()
