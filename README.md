# DATA-ANNOTATION
Data Annotation using Python 
Packages:
  * pandas
  * os
  * pydicom

# TASK
  * The task is to read the files(.dcm) from the nested folders in the "Data" folder and segregating those files with a specific heading(AN,CN,MCI) that is to which category the file belongs to with the help of csv file and saving those files under the appropriate folders(AN,CN,MCI) which is inside the "SEPARATED" folder. 
  * The files are of Digital Imaging and Communications in Medicine(DICOM) that is .dcm type. So the files are read using pydicom.
  * To locate and save those files, os(Operating System) package is used.
  * To read the csv file, pandas is used.
