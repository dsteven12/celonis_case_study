import cloud_api
import pandas as pd
import csv_to_cleaned_df as ccd
import config as c
from rich.console import Console
from time import sleep

console = Console()

csvUploadFile = ccd.updated_file # Path to csv file you want to upload

cloud = cloud_api.cloud(c.TENANT, c.REALM, c.TOKEN)


# Provides console status for pushing data chunks and submitting of jobs
with console.status("[bold][green]Uploading Data into Celonis...") as status:
    # Create Job
    new_job = cloud.create_job(c.POOL_ID, "CLAIMS_DATA")
    new_job_id = new_job["id"]
    console.log(f"New job id: {new_job_id}")
    console.log(f"[green]Finished creating job! {new_job}[/green]")
    sleep(1)
    # Push Data Chunks
    push_chunk = cloud.push_new_chunk(c.POOL_ID, new_job_id, csvUploadFile)
    console.log(f"[green]Finished pushing data chunk! {push_chunk}[/green]")
    sleep(1)
    # Submit Job
    submit_job = cloud.submit_job(c.POOL_ID, new_job_id)
    console.log(f"[green]Finished submitting job! {submit_job}[/green]")
    sleep(1)
    # List Jobs
    list_job = cloud.list_jobs(c.POOL_ID)
    console.log(f"[bold][green]Shows the most recent data jobs executed.")
    for job in list_job[:1]:
        console.log(f"[blue]Data_Pool_ID: {job['dataPoolId']}") 
        console.log(f"[blue]JOB_ID: {job['id']}") 
        console.log(f"[blue]JOB_STATUS: {job['status']}") 
        console.log(f"[blue]JOB_LOGS: {job['logs']}")
    console.log(f"[green]Finished list jobs for status check![/green]")
    sleep(1)
    console.log(f'[bold][red]Done!') 

