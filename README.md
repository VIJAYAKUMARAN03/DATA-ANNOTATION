# Data Annotation Using Python for DICOM Files

## Data Annotation
Data annotation plays a crucial role in organizing and categorizing information for various applications, particularly in medical imaging. Annotation involves labeling data according to predefined categories, facilitating efficient retrieval and analysis.
Data Annotation using Python 

## Data Annotation Significance:
As said, Data annotation involves categorizing and labeling data according to specific criteria or classes, facilitating organization and analysis.In medical imaging, annotation is crucial for identifying and categorizing DICOM files based on factors such as disease type, patient condition, or imaging characteristics.

## Script Objective:

The provided Python script aims to automate the process of annotating DICOM files based on predefined categories.
It streamlines the task of sorting DICOM files into respective categories, such as CN (Cognitively Normal), AD (Alzheimer's Disease), and MCI (Mild Cognitive Impairment), as specified in a CSV file.

## Libraries Utilized:

The script leverages three key libraries:
pydicom: This library is used for reading and handling DICOM files, enabling access to DICOM metadata and pixel data.
pandas: Utilized for reading and parsing CSV files, enabling efficient extraction of annotation information and organization into dataframes.
os: Essential for performing file operations such as directory navigation, file listing, and moving files between directories.

## Directory Structure:

The script assumes a specific directory structure:
Input DICOM files are stored in nested folders within a base directory named "ADNI".
A CSV file named "ADNI_MRI_8_18_2023.csv" contains information about subjects and their corresponding groups (e.g., CN, AD, MCI).
Output folders for categorized DICOM files are created within a base directory named "SEPARATED", with subfolders for each category (CN, AD, MCI).
Workflow Overview:

The script iterates over each entry in the CSV file, representing a subject and their assigned group.
For each subject, it navigates through nested folders within the "ADNI" directory to access DICOM files.
Upon identifying a DICOM file, it determines its category based on the subject's group in the CSV file.
The DICOM file is then moved to the appropriate category folder within the "SEPARATED" directory structure.

## Annotation Statistics:

Throughout the process, the script keeps track of the number of files processed for each category (CN, AD, MCI) and the total number of files.

## Output and Verification:

Upon completion, the script provides feedback on the number of files processed for each category and the overall total.
Users can verify the correctness of the annotation process by inspecting the output folders within the "SEPARATED" directory.

## Benefits and Implications:

By automating the annotation of DICOM files, the script enhances efficiency and accuracy in medical imaging analysis and research.
Researchers can devote more time to data interpretation and insights generation, rather than manual data organization.
The script's adaptability allows for customization according to specific annotation criteria and directory structures, catering to diverse research needs and datasets.






