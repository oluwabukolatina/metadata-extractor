import os
import csv
import utils
import config
from extractor import extractMetadata


#  Main function to run the metadata extraction tool.
def main():
    # Setup logging
    utils.setupLogging(config.LOG_FILE_PATH)

    # Prompt user for directory path
    directoryPath = input("Enter the directory path containing image files: ").strip()

    if not os.path.isdir(directoryPath):
        print("The specified path is not a valid directory.")
        return

    # Process images in the directory
    metadataList = processDirectory(directoryPath)

    # Define the output path for the metadata report
    outputPath = os.path.join(directoryPath, "metadata-report.csv")

    # Generate the metadata report
    generateReport(metadataList, outputPath)

    print(f"Metadata report generated at {outputPath}")


# Processes all image files in the specified directory and extracts their metadata.
#    Args:       directoryPath (str): The path to the directory containing image files
#    Returns:
#       list: A list of dictionaries containing metadata for each image.
def processDirectory(directoryPath):
    metadataList = []
    for fileName in os.listdir(directoryPath):
        # Check if the file is an image and in the correct extension
        if fileName.lower().endswith(('.jpg', '.jpeg', '.png')):
            imagePath = os.path.join(directoryPath, fileName)
            metadata = extractMetadata(imagePath)
            if metadata:
                metadataList.append(metadata)
    return metadataList


#   Generates a CSV report from the extracted metadata.
#   Args:
# metadataList (list): A list of dictionaries containing metadata.
# outputPath (str): The path to the output CSV file.

def generateReport(metadataList, outputPath):
    if not metadataList:
        print("No metadata to write to CSV.")  # Debugging print
    else:
        with open(outputPath, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=config.REPORT_HEADERS)
            writer.writeheader()
            for metadata in metadataList:
                row = {
                    'File Name': metadata.get('FileName', 'N/A'),
                    'File Size': metadata.get('FileSize', 'N/A'),
                    'File Type': metadata.get('FileType', 'N/A'),
                    'Image Width': metadata.get('ImageWidth', 'N/A'),
                    'Image Height': metadata.get('ImageHeight', 'N/A'),
                    'Megapixels': metadata.get('Megapixels', 'N/A'),
                    'Modify Date': metadata.get('FileModifyDate', 'N/A'),
                    'Camera Make': metadata.get('Make', 'N/A'),
                    'Camera Model': metadata.get('Model', 'N/A'),
                    'Orientation': metadata.get('Orientation', 'N/A'),
                    'X Resolution': metadata.get('XResolution', 'N/A'),
                    'Y Resolution': metadata.get('YResolution', 'N/A'),
                    'Resolution Unit': metadata.get('ResolutionUnit', 'N/A'),
                    'Software': metadata.get('Software', 'N/A'),
                    'Exposure Time': metadata.get('ExposureTime', 'N/A'),
                    'F Number': metadata.get('FNumber', 'N/A'),
                    'ISO': metadata.get('ISO', 'N/A'),
                    'Date/Time Original': metadata.get('DateTimeOriginal', 'N/A'),
                    'Flash': metadata.get('Flash', 'N/A'),
                    'Focal Length': metadata.get('FocalLength', 'N/A'),
                    'GPS Latitude': metadata.get('GPS Latitude', 'N/A'),
                    'GPS Longitude': metadata.get('GPS Longitude', 'N/A'),
                    'GPS Altitude': metadata.get('GPS Altitude', 'N/A'),
                    'GPS Date/Time': metadata.get('GPS Date/Time', 'N/A'),
                }
                writer.writerow(row)
        print(f"Report generated at: {outputPath}")


if __name__ == "__main__":
    main()
