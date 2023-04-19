# Airflow_Reddit_API_Datapipeline

## Project overview

the process of creating a simple ETL (Extract, Transform, Load) pipeline using RedditAPI and Apache Airflow involves the following steps:

1. Spin up an EC2 instance and create an S3 bucket for the project.
2. Install the required packages for the pipeline project on the EC2 instance, including Apache Airflow, Pandas, and s3fs.
3. Deploy the Python scripts for downloading, extracting, and uploading data to S3, and schedule the workflow using Airflow's DAG (Directed Acyclic Graph) concept.
4. Start a standalone Airflow web server for the project, which allows for quick setup and experimentation. Access the Airflow console via the EC2's public DNS and configure the DAG folder to point to the directory where the Python scripts are deployed.
Trigger the DAG to start the workflow.
5. Confirm that the data was successfully stored in the S3 bucket.

Note: It's important to consider security best practices and not use the standalone Airflow mode for production use, as it may lack necessary functionalities and scalability.


## Python Code

etl_reddit.py: This Python script implements the ETL (Extract, Transform, Load) process for extracting data from the Reddit API, performing transformations, and loading the data into AWS S3 using the s3fs library.

etl_reddit_dag.py: This file contains the implementation of the Directed Acyclic Graph (DAG) and task definitions for Apache Airflow. The DAG defines the workflow and dependencies for executing the Reddit ETL script at scheduled intervals or manually triggered using the Airflow console.

variables.py: This module simply contains the variables to be used in etl_reddit.py module

For more information on how to execute this project, click https://medium.com/@iamzamartech/creating-a-simple-etl-pipeline-using-redditapi-and-apache-airflow-3597f3f22ded to view an article i have written for it.


## Architecture


![Screenshot 2023-04-19 at 02 57 25](https://user-images.githubusercontent.com/95361532/232946834-7cfceba1-726e-4c26-935f-37880197978b.png)

