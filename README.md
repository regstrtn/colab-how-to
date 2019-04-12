# Instructions about how to use Google's colab notebooks
Creating a repository which will contain info about how to use Google's colab. 

## Reading Data
How to read data? There are several options: 
1. Use pandas to read data from a public url (eg github)
   `df = pd.read_csv([AmazonReviewDatasetURL](amazon_cells_labelled.txt))

2. Upload file into Google colab VM and then reading from there
  ```
  from google.colab import files
  import io
  
  uploaded = files.upload() #A dialog box will open up which will allow you to upload files
  df2 = pd.read_csv(io.BytesIO(uploaded['Filename.csv']))
  # Dataset is now stored in a Pandas Dataframe
  ```
  
3. Use wget shell command to download a file to the local filesystem of the colab VM and then read this file in python. Often times you will have to unzip the downloaded file. To execute a shell command from python, pre-pend it with ! sign. 
```
!wget https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png
```

-----------------------------------------

## Downloading a file
  This is extremely simple
  ```
  files.download("FileName.csv")
  ```
  
