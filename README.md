# Accident Database Project
<hr>
This repository consists of the following files:<br>
1. DMQLUI.ipynb: This is the final jupyter notebook that contains the data preprocessing steps applied ot the original dataset along with the code for the UI that was written for the purpose of insertion, deletion and retreival of data
<br>2. DMQLUI.py: This is the same file as that of the jupyter notebook. This python file was created for the sole purpose of executing the UI locally. The UI can be easily executed using the command prompt. 
<br>Step1: Open Command prompt on your Windows 
<br>Step2: Traverse to the directory where the DMQLUI.py file is stored/downloaded
<br>Step3: Enter the following command- pip install psycopg2
<br>This will import all the required libraries that need before execution of the UI
<br>Step4: Enter the following command- python DMQLUI.py
<br>Once you press enter the UI will be executed and running on your screen. To view how this UI works and what type of outputs can be expected from the UI, you can refer to the Mileston2_LevelUp.pdf
<br>3. DMQL_Checkpoint.ipynb: This jupyter notebook contains all the data preprocessing steps along with all the tables that were created so that the data was loaded into the POSTGRESQL database. Once the tables were created all query executions and optimizations were performed using the POSTGRESQL(pgAdmin)
<br>4. Dataset.pdf: This pdf contains the link to where you can find the dataset. The dataset was too large to be uploaded here and so the link of the dataset is provided in the given pdf alongwith its description so that it is easier to find the dataset online
<br>5. Milestone2_LevelUp.pdf: This pdf contains the whole project from scratch. It contains steps from why this dataset was chosen, all the visualizations on the data and also how the data formation was done. In addition to this all the required steps to convert the table into 3NF and BCNF has laso been shown. In assition to this, optimization steps like indexing are also shown. Finally a brief about the UI which was developed has been written in this pdf.
<br>6. milestone1_LevelUp.pdf: This pdf contains steps the intial steps of the project. It contains steps from why this dataset was chosen, all the visualizations on the data and also how the data formation was done.
<hr>
 
# NOTE: 
<br>After the checkpoint, for the purpose of optimization, the BCNF tables were split further into smaller tables for faster execution of queries.
<br>All the 6 queries for the tables have been mentioned below.
<br>These queries were derived from the EntireDB Table, which contains the entire database rows and attributes as well. 
<br>
<br>CREATE TABLE WeatherTable AS
<br>SELECT "AccidentID","WeatherID","Number","Street","Side","City","County","State","Zipcode","Country","Timezone","Airport_Code","Weather_Timestamp","Temperature","Wind_Chill","Humidity","Pressure","Visibility","Wind_Direction","Wind_Speed","Precipitation","Weather_Condition" FROM "EntireDB";
<br>
<br>CREATE TABLE AccidentTable AS
<br>SELECT "AccidentID", "Severity", "Start_Time","End_Time","Distance","Description" FROM "EntireDB";
<br>
<br>CREATE TABLE FeatureTable AS
<br>SELECT "AccidentID","FeatureID","Amenity","Bump","Crossing","Give_Way","Junction","No_Exit","Railway","Roundabout","Station","Stop","Traffic_Calming","Traffic_Signal","Turning_Loop" FROM "EntireDB";
<br>
<br>CREATE TABLE StartLocationTable AS
<br>SELECT "AccidentID","Start_Lat","Start_Lng" FROM "EntireDB";
<br>
<br>ALTER TABLE  StartLocationTable
<br>ADD COLUMN "StartID" SERIAL PRIMARY KEY;
<br>
<br>CREATE TABLE EndLocationTable AS
<br>SELECT "AccidentID","End_Lat","End_Lng" FROM "EntireDB";
<br>
<br>ALTER TABLE EndLocationTable
<br>ADD COLUMN "EndID" SERIAL PRIMARY KEY;
<br>
<br>CREATE TABLE TwilightPhaseTable AS
<br>SELECT "AccidentID","Sunrise_Sunset","Civil_Twilight","Nautical_Twilight","Astronomical_Twilight" FROM "EntireDB";
<br>
<br>ALTER TABLE  TwilightPhaseTable
<br>ADD COLUMN "TID" SERIAL PRIMARY KEY;
<hr>
# FURTHER ENHANCEMENTS
<br>The database that we designed is good for businesses to get enough insights, but there is a scope for a few improvements. Since this is an already populated database and static in nature, we can improve the time taken to fetch the data by creating views for the queries that are frequently accessed on the front end.
