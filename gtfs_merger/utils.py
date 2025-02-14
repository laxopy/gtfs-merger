# gtfs_merger/utils.py

import pandas as pd
import os

def read_gtfs_file(file_path):
    """Reads a GTFS file into a pandas DataFrame."""
    return pd.read_csv(file_path)

def check_headers_consistency(gtfs_dfs):
    """
    Checks if headers are consistent across all GTFS DataFrames.
    Returns a list of files with inconsistent headers.
    """
    inconsistent_files = []
    for file_name, dfs in gtfs_dfs.items():
        headers = [set(df.columns) for df in dfs]
        if not all(header == headers[0] for header in headers):
            inconsistent_files.append(file_name)
    return inconsistent_files

def find_duplicate_keys(df, unique_keys):
    """
    Finds duplicate rows in a DataFrame based on unique keys.
    Returns a DataFrame of duplicates.
    """
    duplicates = df[df.duplicated(subset=unique_keys, keep=False)]
    return duplicates