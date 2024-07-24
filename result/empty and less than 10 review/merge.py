import pandas as pd

# List of CSV files to be merged
file_list = ["result\\view_mean\\shab.csv", 'result\\view_mean\\jajiga.csv', 'result\\view_mean\\otaghak.csv', 'result\\view_mean\\homsa.csv']

# Read and concatenate the files into a single DataFrame
df_list = [pd.read_csv(file, encoding='utf-8') for file in file_list]
merged_df = pd.concat(df_list, ignore_index=True)

# Optional: Remove duplicate rows if needed
merged_df = merged_df.drop_duplicates()

# Save the merged DataFrame to a new CSV file
merged_file = 'merged.csv'
merged_df.to_csv(merged_file, index=False, encoding='utf-8')

print(f'Merged file saved as {merged_file}')
