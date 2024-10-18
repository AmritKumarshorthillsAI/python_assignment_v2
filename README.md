# Python Assignment

![image](https://github.com/user-attachments/assets/b4a9a821-9924-44e1-8ced-5806ac5f9344)

 
## Overview
The `data_extractor` directory houses a set of tools specifically designed to extract data from various file formats and efficiently store the resulting information.

## Purpose
The main goal of the `data_extractor` directory is to deliver a user-friendly and efficient method for extracting data from a variety of file formats and storing that data for subsequent analysis or processing.

 
## How to Use
To begin, clone the repository and set the file_path variable to the location of the main file. Afterward, run the main.py script to initiate the data extraction process.
 
## Loaders
The `data_extractor` directory features the following loaders, which facilitate data extraction from various file types:
 
- **PDFLoader**: Extracts data from PDF files.
- **DOCXLoader**: Extracts data from DOCX files.
- **PPTLoader**: Extracts data from PPTX files.
 
## Data Extraction
The `data_extractor` leverages the specified loaders to collect data from supported file formats, providing a unified interface for accessing the extracted information.
 
## Storage Options
The `data_extractor` directory offers the following storage solutions for managing the extracted data:
 
- **FileStorage**: Saves the extracted data in a file.
- **SQLStorage**: Saves the extracted data in a SQL database.
 
## Functionality
The `data_extractor` offers the following features:
 
- Extracts data from PDF, DOCX, and PPTX files using the appropriate loaders.
- Saves the extracted data either in a file or in a SQL database using the provided storage options.
- Provides a unified interface for easy access to the extracted data.
 


# Python Virtual Environment Setup

This document outlines how to set up a Python virtual environment and manage dependencies using a `requirements.txt` file.

## Prerequisites

* Ensure you have Python 3.10 installed on your system.
* Make sure you have the `apt` package manager available for installing packages.

## Steps to Set Up a Virtual Environment

1. **Install the `venv` module** (if not already installed):

```bash
sudo apt install python3.10-venv
```

2. **Create a Virtual Environment**:

```bash
python3 -m venv venv
```

3. **Activate the Virtual Environment**:

```bash
source venv/bin/activate
```

Once activated, your terminal prompt will change (e.g., `(venv)` will appear), and your Python and pip commands will use the versions specific to this environment.

4. **Install Dependencies**: If you have a `requirements.txt` file with the necessary packages listed, run:

```bash
pip install -r requirements.txt
```

This command installs all the packages specified in the `requirements.txt` file, quickly setting up your environment.

5. **Generate a `requirements.txt` File**: To create or update a `requirements.txt` file that lists the packages installed in your virtual environment, use:

```bash
pip3 freeze > requirements.txt
```

# How to run the code
```bash
python3 main.py
```
## After running the main.py you will see extracted files in extracted data folder

# How to check data stored in sqlite the code
```bash
sqlite3 assignment4.db
.tables  - will list down tables in database
select * from text;
ctrl + D - to exit sqlite
```