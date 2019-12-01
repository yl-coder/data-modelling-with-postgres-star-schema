## How to run the ETL process.
1) Create postgres database on localhost with dbname=studentdb user=student password=student 
1) Install and open Python3 cli
2) Run the following commands

```
import create_tables as ct;
ct.main;
import etl as e;
e.main();
```

## Purpose of this database in the context of the startup, Sparkify, and their analytical goals.

 - This database contains analytical information about the usage of Sparkify users song play represented as a fact table using star schema. It also contains dimension data of user information, songs, artists and timestamps of records in songplay.
 - Sparkify oftens want to know where their user is located at, and what songs interest them. So that they can procure better song content with music provider.
 - Sparkify also wants to popular song and artist in the area so that they can do song recommendation to their user in similar location.

## Database schema design and ETL pipeline.
 - The data is modelled using star schema. Song play data is represented as a fact table and user information, songs, artists and timestamps of records in songplay is represented as dimension table.
 - The ETL pipeline reads from JSON files on local storage and process them into fact and dimension table using python and pandas data abstraction api. The processed records is then saved into postgres database for analytical purpose.

## Directory

 - data : Input files for ETL process.
 - test.ipynb : Notebook for testing sql queries.
 - sql_queries.py: python file that contains create tables, insert  and select queries string.
 - README.md: This file that you are reading.
 - etl.py: etl main file. You can run main() method here to start the etl process, but you need to run create_tables.main() first
 - create_tables.py: Contains the logic to create tables based on sql_queries constants.

## Possible Improvement

 - Stricter data type, to define the length of varchar
 - To log on conflict sql queries
 - To handle potential exception
 - In the event we need to process the entire dataset (Few hundred GB), we can use apache spark for data processing engine. HDFS and parquet files for input layer, and Redshift for output layer.