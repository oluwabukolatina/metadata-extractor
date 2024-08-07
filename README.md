## Metadata Extractor Tool

### Overview
The Metadata Extractor tool is designed to extract metadata from image files and generate a CSV report. This guide will walk you through the steps to set up, configure, and run the tool on your system.
### Features
- Metadata Extraction: Collects EXIF metadata from JPEG, JPG, and PNG images. 
- Report Generation: Generates a CSV report with the extracted metadata. 
- Batch Processing: Processes all images in the specified directory. 
- Image Integrity: Retains the original integrity of images during the extraction proces
## Prerequisites
- Python 3.x installed on your system 

## Installation Steps
- clone the repository: 
```commandline
git clone https://github.com/oluwabukolatina/metadata-extractor.git
cd metadata-extractor
```
- install dependencies
```commandline
pip install pillow
```
-  Prepare Your Image File: Place the image files you want to analyze into a directory. Make sure the files have the extensions supported by the tool (e.g., .jpg, .jpeg, .png).
## Usage
Open a terminal or command prompt and execute the metadata-extractor.py script by running:
```commandline
python metadata-extractor.py
```
- Follow the Prompts : The script will prompt you to enter the directory path where your image files are located. Provide the path and press Enter.
```commandline
Enter the directory path containing image files: /path/to/your/images
```
- Check Output - The script will process the images in the specified directory, extract metadata, and generate a CSV report named metadata-report.csv in the same directory. It will also create a log file named metadata-extractor.log where any errors encountered during processing are recorded.
