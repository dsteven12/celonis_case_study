import cloud_api
import pandas as pd
import csv_to_cleaned_df as ccd
import config as c
from rich.console import Console
from time import sleep

console = Console()

csvUploadFile = ccd.updated_file # Path to csv file you want to upload

cloud = cloud_api.cloud(c.TENANT, c.REALM, c.TOKEN)
new_job = cloud.create_job(c.POOL_ID, "CLAIMS_DATA")
new_job_id = new_job["id"]

# Provides console status for pushing data chunks and submitting of jobs
with console.status("[bold green]Uploading Data...") as status:
    push_chunk = cloud.push_new_chunk(c.POOL_ID, new_job_id, csvUploadFile)
    console.log(f"[green]Finished pushing data! {push_chunk}[/green]")
    sleep(1)
    submit_job = cloud.submit_job(c.POOL_ID, new_job_id)
    console.log(f"[green]Finished submitting job! {submit_job}[/green]")
    console.log(f'[bold][red]Done!')  