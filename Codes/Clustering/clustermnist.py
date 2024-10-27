import pandas as pd

# Initialize an empty list to store the rows with the least cost function in each group
clustered_rows_1 = []
columns_to_keep = ['Multiplier', 'SSIM', 'Area', 'Power','Cost function']

for i in range(0,100):
    filename = "0/0_"+str(i)+".csv"
    # Load the CSV file into a DataFrame
    df = pd.read_csv(filename)

    # Sort the DataFrame by 'SSIM' column in descending order
    df_sorted = df.sort_values(by='SSIM', ascending=False)


    # Group the sorted DataFrame into chunks of 1600 rows each
    for i in range(0, len(df_sorted), 1600):
        chunk = df_sorted.iloc[i:i+1600]
        # Find the row with the minimum 'Cost function' in the current chunk
        min_cost_row = chunk.loc[chunk['Cost function'].idxmin()]
        # Append the row to the clustered_rows list
        clustered_rows_1.append(min_cost_row)

    # Convert the selected rows into a DataFrame
    selected_df = pd.DataFrame(clustered_rows_1)

    # Write the selected DataFrame to a new CSV file
    selected_df.to_csv('./clustered_data_ap_1600/0.csv', index=False)

print("Operation completed successfully. The selected rows have been written to '0.csv'.")
# Initialize an empty list to store the rows with the least cost function in each group
clustered_rows_2 = []

for i in range(0,100):
    filename = "1/1_"+str(i)+".csv"
    # Load the CSV file into a DataFrame
    df = pd.read_csv(filename)

    # Sort the DataFrame by 'SSIM' column in descending order
    df_sorted = df.sort_values(by='SSIM', ascending=False)


    # Group the sorted DataFrame into chunks of 1600 rows each
    for i in range(0, len(df_sorted), 1600):
        chunk = df_sorted.iloc[i:i+1600]
        # Find the row with the minimum 'Cost function' in the current chunk
        min_cost_row = chunk.loc[chunk['Cost function'].idxmin()]
        # Append the row to the clustered_rows list
        clustered_rows_2.append(min_cost_row)

    # Convert the selected rows into a DataFrame
    selected_df = pd.DataFrame(clustered_rows_2)

    # Write the selected DataFrame to a new CSV file
    selected_df.to_csv('./clustered_data_ap_1600/1.csv', index=False)

print("Operation completed successfully. The selected rows have been written to 'Bag.csv'.")
# Initialize an empty list to store the rows with the least cost function in each group
clustered_rows_3 = []
columns_to_keep = ['Multiplier', 'SSIM', 'Cost function']

for i in range(0,100):
    filename = "2/2_"+str(i)+".csv"
    # Load the CSV file into a DataFrame
    df = pd.read_csv(filename)

    # Sort the DataFrame by 'SSIM' column in descending order
    df_sorted = df.sort_values(by='SSIM', ascending=False)


    # Group the sorted DataFrame into chunks of 1600 rows each
    for i in range(0, len(df_sorted), 1600):
        chunk = df_sorted.iloc[i:i+1600]
        # Find the row with the minimum 'Cost function' in the current chunk
        min_cost_row = chunk.loc[chunk['Cost function'].idxmin()]
        # Append the row to the clustered_rows_3 list
        clustered_rows_3.append(min_cost_row)

    # Convert the selected rows into a DataFrame
    selected_df = pd.DataFrame(clustered_rows_3)

    # Write the selected DataFrame to a new CSV file
    selected_df.to_csv('./clustered_data_ap_1600/2.csv', index=False)

print("Operation completed successfully. The selected rows have been written to 'Coat.csv'.")
# Initialize an empty list to store the rows with the least cost function in each group
clustered_rows_4 = []
columns_to_keep = ['Multiplier', 'SSIM', 'Cost function']

for i in range(0,100):
    filename = "3/3_"+str(i)+".csv"
    # Load the CSV file into a DataFrame
    df = pd.read_csv(filename)

    # Sort the DataFrame by 'SSIM' column in descending order
    df_sorted = df.sort_values(by='SSIM', ascending=False)


    # Group the sorted DataFrame into chunks of 1600 rows each
    for i in range(0, len(df_sorted), 1600):
        chunk = df_sorted.iloc[i:i+1600]
        # Find the row with the minimum 'Cost function' in the current chunk
        min_cost_row = chunk.loc[chunk['Cost function'].idxmin()]
        # Append the row to the clustered_rows_4 list
        clustered_rows_4.append(min_cost_row)

    # Convert the selected rows into a DataFrame
    selected_df = pd.DataFrame(clustered_rows_4)

    # Write the selected DataFrame to a new CSV file
    selected_df.to_csv('./clustered_data_ap_1600/3.csv', index=False)

print("Operation completed successfully. The selected rows have been written to '3.csv'.")
# Initialize an empty list to store the rows with the least cost function in each group
clustered_rows_5 = []
columns_to_keep = ['Multiplier', 'SSIM', 'Cost function']

for i in range(0,100):
    filename = "4/4_"+str(i)+".csv"
    # Load the CSV file into a DataFrame
    df = pd.read_csv(filename)

    # Sort the DataFrame by 'SSIM' column in descending order
    df_sorted = df.sort_values(by='SSIM', ascending=False)


    # Group the sorted DataFrame into chunks of 1600 rows each
    for i in range(0, len(df_sorted), 1600):
        chunk = df_sorted.iloc[i:i+1600]
        # Find the row with the minimum 'Cost function' in the current chunk
        min_cost_row = chunk.loc[chunk['Cost function'].idxmin()]
        # Append the row to the clustered_rows_5 list
        clustered_rows_5.append(min_cost_row)

    # Convert the selected rows into a DataFrame
    selected_df = pd.DataFrame(clustered_rows_5)

    # Write the selected DataFrame to a new CSV file
    selected_df.to_csv('./clustered_data_ap_1600/4.csv', index=False)

print("Operation completed successfully. The selected rows have been written to '4.csv'.")

# Initialize an empty list to store the rows with the least cost function in each group
clustered_rows_6 = []
columns_to_keep = ['Multiplier', 'SSIM', 'Cost function']

for i in range(0,100):
    filename = "5/5_"+str(i)+".csv"
    # Load the CSV file into a DataFrame
    df = pd.read_csv(filename)

    # Sort the DataFrame by 'SSIM' column in descending order
    df_sorted = df.sort_values(by='SSIM', ascending=False)


    # Group the sorted DataFrame into chunks of 1600 rows each
    for i in range(0, len(df_sorted), 1600):
        chunk = df_sorted.iloc[i:i+1600]
        # Find the row with the minimum 'Cost function' in the current chunk
        min_cost_row = chunk.loc[chunk['Cost function'].idxmin()]
        # Append the row to the clustered_rows_6 list
        clustered_rows_6.append(min_cost_row)

    # Convert the selected rows into a DataFrame
    selected_df = pd.DataFrame(clustered_rows_6)

    # Write the selected DataFrame to a new CSV file
    selected_df.to_csv('./clustered_data_ap_1600/5.csv', index=False)

print("Operation completed successfully. The selected rows have been written to '5.csv'.")

# Initialize an empty list to store the rows with the least cost function in each group
clustered_rows_7 = []
columns_to_keep = ['Multiplier', 'SSIM', 'Cost function']

for i in range(0,100):
    filename = "6/6_"+str(i)+".csv"
    # Load the CSV file into a DataFrame
    df = pd.read_csv(filename)

    # Sort the DataFrame by 'SSIM' column in descending order
    df_sorted = df.sort_values(by='SSIM', ascending=False)


    # Group the sorted DataFrame into chunks of 1600 rows each
    for i in range(0, len(df_sorted), 1600):
        chunk = df_sorted.iloc[i:i+1600]
        # Find the row with the minimum 'Cost function' in the current chunk
        min_cost_row = chunk.loc[chunk['Cost function'].idxmin()]
        # Append the row to the clustered_rows_7 list
        clustered_rows_7.append(min_cost_row)

    # Convert the selected rows into a DataFrame
    selected_df = pd.DataFrame(clustered_rows_7)

    # Write the selected DataFrame to a new CSV file
    selected_df.to_csv('./clustered_data_ap_1600/6.csv', index=False)

print("Operation completed successfully. The selected rows have been written to '6.csv'.")

# Initialize an empty list to store the rows with the least cost function in each group
clustered_rows_8 = []
columns_to_keep = ['Multiplier', 'SSIM', 'Cost function']

for i in range(0,100):
    filename = "7/7_"+str(i)+".csv"
    # Load the CSV file into a DataFrame
    df = pd.read_csv(filename)

    # Sort the DataFrame by 'SSIM' column in descending order
    df_sorted = df.sort_values(by='SSIM', ascending=False)


    # Group the sorted DataFrame into chunks of 1600 rows each
    for i in range(0, len(df_sorted), 1600):
        chunk = df_sorted.iloc[i:i+1600]
        # Find the row with the minimum 'Cost function' in the current chunk
        min_cost_row = chunk.loc[chunk['Cost function'].idxmin()]
        # Append the row to the clustered_rows_8 list
        clustered_rows_8.append(min_cost_row)

    # Convert the selected rows into a DataFrame
    selected_df = pd.DataFrame(clustered_rows_8)

    # Write the selected DataFrame to a new CSV file
    selected_df.to_csv('./clustered_data_ap_1600/7.csv', index=False)

print("Operation completed successfully. The selected rows have been written to 'Sneaker.csv'.")

# Initialize an empty list to store the rows with the least cost function in each group
clustered_rows_9 = []
columns_to_keep = ['Multiplier', 'SSIM', 'Cost function']

for i in range(0,100):
    filename = "8/8_"+str(i)+".csv"
    # Load the CSV file into a DataFrame
    df = pd.read_csv(filename)

    # Sort the DataFrame by 'SSIM' column in descending order
    df_sorted = df.sort_values(by='SSIM', ascending=False)


    # Group the sorted DataFrame into chunks of 1600 rows each
    for i in range(0, len(df_sorted), 1600):
        chunk = df_sorted.iloc[i:i+1600]
        # Find the row with the minimum 'Cost function' in the current chunk
        min_cost_row = chunk.loc[chunk['Cost function'].idxmin()]
        # Append the row to the clustered_rows_9 list
        clustered_rows_9.append(min_cost_row)

    # Convert the selected rows into a DataFrame
    selected_df = pd.DataFrame(clustered_rows_9)

    # Write the selected DataFrame to a new CSV file
    selected_df.to_csv('./clustered_data_ap_1600/8.csv', index=False)

print("Operation completed successfully. The selected rows have been written to '8.csv'.")

#  Initialize an empty list to store the rows with the least cost function in each group
clustered_rows_10 = []
columns_to_keep = ['Multiplier', 'SSIM', 'Cost function']

for i in range(0,100):
    filename = "9/9_"+str(i)+".csv"
    # Load the CSV file into a DataFrame
    df = pd.read_csv(filename)

    # Sort the DataFrame by 'SSIM' column in descending order
    df_sorted = df.sort_values(by='SSIM', ascending=False)


    # Group the sorted DataFrame into chunks of 1600 rows each
    for i in range(0, len(df_sorted), 1600):
        chunk = df_sorted.iloc[i:i+1600]
        # Find the row with the minimum 'Cost function' in the current chunk
        min_cost_row = chunk.loc[chunk['Cost function'].idxmin()]
        # Append the row to the clustered_rows_10 list
        clustered_rows_10.append(min_cost_row)

    # Convert the selected rows into a DataFrame
    selected_df = pd.DataFrame(clustered_rows_10)

    # Write the selected DataFrame to a new CSV file
    selected_df.to_csv('./clustered_data_ap_1600/9.csv', index=False)

print("Operation completed successfully. The selected rows have been written to '9.csv'.")

# # Load the CSV file into a DataFrame
# file = './clustered_data_ap_1600/Trouser.csv'

# df = pd.read_csv(file)

# # Specify the column to check for duplicates (replace 'column_name' with the actual column name)
# column_name = 'Multiplier'

# # # Ensure the column exists
# # if column_name not in df.columns:
# #     print(f"Column '{column_name}' not found in the DataFrame.")
# # else:
# # Get the number of rows in the original DataFrame
# original_row_count = len(df)
# print(f"Number of rows in the original DataFrame: {original_row_count}")

# # Remove duplicate rows based on the specified column
# df_no_duplicates = df.drop_duplicates(subset=[column_name])

# # Get the number of rows in the cleaned DataFrame
# cleaned_row_count = len(df_no_duplicates)
# print(f"Number of rows in the cleaned DataFrame: {cleaned_row_count}")

# # Calculate the number of rows dropped
# rows_dropped = original_row_count - cleaned_row_count

# # Optionally, you can reset the index after removing duplicates
# df_no_duplicates = df_no_duplicates.reset_index(drop=True)

# # Select only the desired columns
# df_selected_columns = df_no_duplicates[columns_to_keep]


# # Save the DataFrame without duplicates back to a CSV file
# df_selected_columns.to_csv('./filtered_data/Trouser_filtered.csv', index=False)

# print(f"Duplicate rows based on the column '{column_name}' have been removed.")
# print(f"Number of rows dropped: {rows_dropped}")

