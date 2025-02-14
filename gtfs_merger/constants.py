# gtfs_merger/constants.py

# Unique keys for GTFS files
UNIQUE_KEYS = {
    'agency.txt': ['agency_id'],
    'stops.txt': ['stop_id'],
    'routes.txt': ['route_id'],
    'trips.txt': ['trip_id'],
    'stop_times.txt': ['trip_id', 'stop_sequence'],
    'calendar.txt': ['service_id'],
    'calendar_dates.txt': ['service_id', 'date'],
    'fare_attributes.txt': ['fare_id'],
    'fare_rules.txt': ['fare_id', 'route_id', 'origin_id', 'destination_id', 'contains_id'],
    'shapes.txt': ['shape_id', 'shape_pt_sequence'],
    'frequencies.txt': ['trip_id', 'start_time'],
    'transfers.txt': ['from_stop_id', 'to_stop_id'],
    'feed_info.txt': ['feed_publisher_name', 'feed_publisher_url', 'feed_lang'],
    'pathways.txt': ['pathway_id'],
    'levels.txt': ['level_id'],
    'translations.txt': ['table_name', 'field_name', 'language', 'record_id', 'record_sub_id', 'field_value'],
    'attributions.txt': ['attribution_id']
}