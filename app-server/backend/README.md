# Incomplete Backend

## Services that Run
- Upload
- Download
- Restart

## How to Run it
- First download a credentials json file from the service account for package-registry and name it credentials-project2.json
- Put the credentials file inside the main backend folder. 
- The credentials-project.json file has to be at the same level as manage.py 
- Then run locally python manage.py runserver (make sure you have all of the required packages downloaded on your machine)

## Upload and Download
- Only zipped folders of packages can be uploaded and downloaded from backend.

## Restart
- Restart will empty the Package Registry and will show how many packages were deleted
