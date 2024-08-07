LOG_FILE_PATH = 'metadata-extractor.log'

# Headers for the CSV report
REPORT_HEADERS = [
    'File Name',
    'File Size',
    'File Type',
    'Image Width',
    'Image Height',
    'Megapixels',
    'Modify Date',
    'Camera Make',
    'Camera Model',
    'Orientation',
    'X Resolution',
    'Y Resolution',
    'Resolution Unit',
    'Software',
    'Exposure Time',
    'F Number',
    'ISO',
    'Date/Time Original',
    'Flash',
    'Focal Length',
    'GPS Latitude',
    'GPS Longitude',
    'GPS Altitude',
    'GPS Date/Time',
    'Mode',  # Added for Pillow integration
    'GPSInfo'  # This is a dictionary, if you need specific GPS data, add more specific fields
]
