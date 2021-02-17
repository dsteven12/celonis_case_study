import cloud_api
import pandas as pd
import csv_to_cleaned_df as ccd
import config as c
from rich.console import Console
from time import sleep

console = Console()

csvUploadFile = ccd.updated_file # Path to csv file you want to upload
cloud = cloud_api.cloud(c.TENANT, c.REALM, c.TOKEN)

def list_recent_job(job_id: str, pool_id: str) -> None:
    """
    Gives job information for currently executed job by checking the job list. 
    If new_job_id matches job_id, it prints that specific job in the console.
    """
    for job in cloud.list_jobs(pool_id):
        if job_id == job['id']: 
            console.log(f"[yellow]JOB_ID: {job['id']}") 
            console.log(f"[blue]TARGET_NAME: {job['targetName']}") 
            console.log(f"[yellow]JOB_STATUS: {job['status']}") 
            console.log(f"[blue]FILE_TYPE: {job['fileType']}")
            console.log(f"[blue]JOB_TYPE: {job['type']}")
            console.log(f"[yellow]JOB_LOGS: {job['logs']}")
            console.log(f"[blue]DATA_POOL_ID: {job['dataPoolId']}") 
    

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
    list_recent_job(new_job_id, c.POOL_ID)
    console.log(f"[bold][green]Finished listing current job for status check![/green]")
    sleep(1)
    console.log(f'[bold][red]Done!') 

