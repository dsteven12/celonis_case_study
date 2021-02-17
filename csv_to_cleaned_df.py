import pandas as pd
import txt_to_csv as t

#QMNUM and QMTXT contains 1 NULL value
#Turning into dataframe
df=pd.read_csv(t.csv_file, header=3)
header_row=list(df.columns)

def convert_col_to_dt(
    df: pd.DataFrame,
    lst: list) -> None:
    """
    Takes in a dataframe and list as parameters and converts specific columns in that dataframe to a datetime
    """
    for col in lst:
        df[col] = pd.to_datetime(df[col], errors='coerce')

def drop_columns(
    df: pd.DataFrame, 
    index1: int, 
    index2: int) -> pd.DataFrame:
    """ 
    Takes in a dataframe and indexes to target specific columns to drop
    """
    return df.drop(df.loc[:, header_row[index1]: header_row[index2]].columns, axis=1)

def drop_rows(
    df: pd.DataFrame,
    needed_index: int) -> pd.DataFrame:
    """
    Takes in a dataframe and index to target specific rows to drop
    """
    return df.drop([df.index[needed_index]])

# Gets rid of first two null columns and last null column
df1=drop_columns(df, 0, 1)
df1=drop_columns(df1, 22, 22)

# Drops first and last null records
df2=drop_rows(df1, 0)
df2=drop_rows(df2, -1)

# Strip header names of whitespace
df3=df2.rename(columns=lambda x: x.strip())

# Converting strings into Datetime. Hard_coded for now since strings weren't formatted for conversion.
datetime_conversion_list = [
    "ERDAT",
    "AEDAT",
    "MZEIT",
    "QMDAT",
    "QMNAM",
    "STRMN",
    "STRUR",
    "LTRMN",
    "LTRUR",
]

# Converts columns from above to datetime columns.
convert_col_to_dt(df3, datetime_conversion_list)

#Changes Schema of DataFrame
df3=df3.astype(
    {
        "MANDT":"int64",
        # "QMNUM":"string",
        # "QMART":"category",
        # "QMTXT":"string",
        # "ARTPR":"category",
        # "PRIOK":"string", #look into further won't accept int
        # "ERNAM":"string",
        # "AENAM":"string",
        # "QMNAM":"string",
        # "WAERS":"category",
        # "AUFNR":"string", #look into further won't accept int
        # "VERID":"string", #look into further won't accept int
    }
)

# Update File Name
updated_file = t.root_path + "cleaned_data/" + "cleaned_" + t.file_name + ".csv"

# Save CSV file
df3.to_csv(updated_file, index=False, header=True, na_rep='None')