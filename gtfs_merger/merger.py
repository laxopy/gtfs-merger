import os
import pandas as pd
import zipfile
import shutil
from gtfs_merger.utils import read_gtfs_file, check_headers_consistency, find_duplicate_keys
from gtfs_merger.constants import UNIQUE_KEYS

class GTFSMerger:
    def __init__(self, input_dir, output_dir):
        self.input_dir = input_dir
        self.output_dir = output_dir
        self.gtfs_dfs = {}
        self.temp_extracted_dir = "temp_gtfs_extracted"  # Temporary extraction folder

    def extract_gtfs_feeds(self):
        """Extracts all GTFS .zip files into a temporary directory."""
        if os.path.exists(self.temp_extracted_dir):
            shutil.rmtree(self.temp_extracted_dir)  # Clear previous extractions
        os.makedirs(self.temp_extracted_dir, exist_ok=True)

        for file in os.listdir(self.input_dir):
            if file.endswith(".zip"):
                zip_path = os.path.join(self.input_dir, file)
                extract_path = os.path.join(self.temp_extracted_dir, file.replace(".zip", ""))
                os.makedirs(extract_path, exist_ok=True)
                with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                    zip_ref.extractall(extract_path)
                print(f"Extracted {file} to {extract_path}")

    def load_feeds(self):
        """Loads extracted GTFS .txt files into DataFrames."""
        self.extract_gtfs_feeds()  # Ensure extraction happens first

        for root, _, files in os.walk(self.temp_extracted_dir):
            for file in files:
                if file.endswith('.txt'):
                    file_path = os.path.join(root, file)
                    if file not in self.gtfs_dfs:
                        self.gtfs_dfs[file] = []
                    self.gtfs_dfs[file].append(read_gtfs_file(file_path))

        print(f"GTFS files loaded: {list(self.gtfs_dfs.keys())}")

    def merge_feeds(self):
        """Merges GTFS feeds into a single feed."""
        merged_dfs = {}
        for file_name, dfs in self.gtfs_dfs.items():
            if file_name in UNIQUE_KEYS:
                unique_keys = UNIQUE_KEYS[file_name]
                combined_df = pd.concat(dfs, ignore_index=True)
                duplicates = find_duplicate_keys(combined_df, unique_keys)
                if not duplicates.empty:
                    print(f"Duplicate keys found in {file_name}. Number of duplicates: {len(duplicates)}")
                    action = input("Type 'continue' to remove duplicates and proceed, or 'abort' to stop the process: ")
                    if action.lower() == 'abort':
                        print("Process aborted by the user.")
                        return
                    elif action.lower() == 'continue':
                        combined_df = combined_df.drop_duplicates(subset=unique_keys, keep='first')
                        print(f"Duplicates removed from {file_name}.")
                    else:
                        print("Invalid input. Process aborted.")
                        return
                merged_dfs[file_name] = combined_df
            else:
                merged_dfs[file_name] = pd.concat(dfs, ignore_index=True)
        self.save_merged_feed(merged_dfs)

    def save_merged_feed(self, merged_dfs):
        """Saves the merged GTFS feed as a compressed .zip file."""
        temp_output_dir = "temp_gtfs_output"  # Temporary folder to store .txt files

        # Ensure temporary output directory exists
        if not os.path.exists(temp_output_dir):
            os.makedirs(temp_output_dir)

        # Save each file as .txt in the temp directory
        for file_name, df in merged_dfs.items():
            print(f"Saving {file_name} with {len(df)} rows...")  # Debugging print
            if df.empty:
                print(f"Warning: {file_name} is empty. Skipping save.")
                continue
            output_path = os.path.join(temp_output_dir, file_name)
            df.to_csv(output_path, index=False)

        # Create the final GTFS .zip file in output_feed/
        zip_output_path = os.path.join(self.output_dir, "merged_gtfs.zip")
        with zipfile.ZipFile(zip_output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for file in os.listdir(temp_output_dir):
                file_path = os.path.join(temp_output_dir, file)
                zipf.write(file_path, arcname=file)  # Add file to ZIP

        # Cleanup: Remove temporary .txt files
        shutil.rmtree(temp_output_dir)

        print(f"Merged GTFS feed saved as {zip_output_path}.")