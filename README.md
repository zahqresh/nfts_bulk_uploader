# nfts_bulk_uploader
NFTS bulk uploader using selenium in python 


## Setup

download repo and install python after that run below commands in the repository folder directory

1 - `` pip install pipenv ``

2- `` pipenv install selenium ``

3-  have to download the webdriver related to your chrome version

4- install metamask crx extension


## To Run

`` pipenv run python uploader.py ``

## Note

You will have to specify paths to folder and change few things in the script such as , Your nfts and json metadata, number of traits to be created in the properties and minor 
stuff if any error occurs (shouldn't be there lets hope for the best)

Have to also add a limit on line 79 for starting number and on line 202 add a starting and ending limit of uploading process


## Best Thing

You can create as much as you want instances of script change limit and run multiple scripts to speed up the whole uploading process
