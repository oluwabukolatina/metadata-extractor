import os

from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS


# Extracts metadata from an image file using Pillow.
#  Args:
#         imagePath (str): The path to the image file.
#
#     Returns:
#         dict: A dictionary containing extracted metadata.
def extractMetadata(imagePath):

    metadata = {}
    try:
        with Image.open(imagePath) as img:
            metadata['FileName'] = os.path.basename(imagePath)
            metadata['FileSize'] = os.path.getsize(imagePath)
            metadata['FileType'] = img.format
            metadata['ImageWidth'] = img.width
            metadata['ImageHeight'] = img.height
            metadata['Mode'] = img.mode

            exif_data = img._getexif()
            if exif_data:
                for tag, value in exif_data.items():
                    tag_name = TAGS.get(tag, tag)
                    metadata[tag_name] = value
                    if tag_name == 'GPSInfo':
                        gps_data = {}
                        for gps_tag in value:
                            gps_tag_name = GPSTAGS.get(gps_tag, gps_tag)
                            gps_data[gps_tag_name] = value[gps_tag]
                        metadata['GPSInfo'] = gps_data
    except Exception as e:
        print(f"Error extracting metadata from {imagePath}: {e}")

    return metadata
