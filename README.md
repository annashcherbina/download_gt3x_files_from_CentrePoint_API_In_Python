### Step 1: Identify the ID of your study of interest

```
python get_study_id.py -apiAccessKey xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx -apiSecretKey xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx -outf studies.txt
```

In studies.txt , you will see the following:

```
[
  {
    "Id": xxx,
    "Name": "MyStudyName",
    "DateCreated": "2017-09-12T18:09:21.827Z",
    "OrganizationName": "MyOrganization"
  }
]
```

### Step 2: Download gt3x data files

Now that you have identified the study id of interest (the "Id" entrie in the above-generated studies.txt), you can retrieve teh raw .gt3x files for all subjects associated with that study:



```
python download_data.py -apiAccessKey xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx -apiSecretKey xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx -studyId xxx -dirToStoreFiles myOutputDir

```
* Pass the "Id" value from your studies.txt file to the `-studyId` flag
* dirToStoreFiles is a path on your machine where the gt3x files will be stored, if this path does not exist, the code will create it.

The output files will be organized by subject in "myOutputDir" (substitute this with your actual directory of interest).

