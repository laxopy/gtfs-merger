# main.py

from gtfs_merger.merger import GTFSMerger
from gtfs_merger.utils import check_headers_consistency

def main():
    input_dir = 'input_feeds'
    output_dir = 'output_feed'

    merger = GTFSMerger(input_dir, output_dir)
    merger.load_feeds()

    inconsistent_files = check_headers_consistency(merger.gtfs_dfs)
    if inconsistent_files:
        print(f"Inconsistent headers found in the following files: {', '.join(inconsistent_files)}")
        print("Process aborted due to header inconsistencies.")
        return

    merger.merge_feeds()

if __name__ == '__main__':
    main()