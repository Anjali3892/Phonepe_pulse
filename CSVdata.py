import os
from dataextraction import *

def save_dataframe_as_csv(dataframe, folder_path, file_name):
    csv_file_path = os.path.join(folder_path, f"{file_name}.csv")
    dataframe.to_csv(csv_file_path, index=False)
    
def save_all_dataframes_as_csv():
    
    directory_path = r"D:\Data Science\Project-2"

    folder_name = "CSV"
    folder_path = os.path.join(directory_path, folder_name)

    save_dataframe_as_csv(aggregated_transaction_state(), folder_path, "aggregated_transaction_state")
    save_dataframe_as_csv(aggregated_user_state(), folder_path, "aggregated_user_state")
    save_dataframe_as_csv(map_transaction_state(), folder_path, "map_transaction_state")
    save_dataframe_as_csv(map_user_state(), folder_path, "map_user_state")
    save_dataframe_as_csv(top_transaction_state(), folder_path, "top_transaction_state")
    save_dataframe_as_csv(top_user_state(), folder_path, "top_user_state")
    save_dataframe_as_csv(top_transaction_state_pincode(), folder_path, "top_transaction_state_pincode")
    save_dataframe_as_csv(top_user_state_pincode(), folder_path, "top_user_state_pincode")
    
save_all_dataframes_as_csv()