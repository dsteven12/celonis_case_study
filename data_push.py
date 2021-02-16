import cloud_api
import pandas as pd
import csv_to_cleaned_df as ccd
import config as c

key = c.TOKEN
poolId = "6b43443e-0cee-40bc-90fb-e941e42f41f8"
teamSubDomain = c.TENANT
serverId = c.REALM
csvUploadFile = ccd.updated_file # Path to csv file you want to upload

cloud = cloud_api.cloud(teamSubDomain, serverId, key)
new_job = cloud.create_job(poolId, "PYTHON_INTEGRATION")
push_chunk = cloud.push_new_chunk(poolId, new_job["id"], csvUploadFile)
submit_job = cloud.submit_job(poolId, new_job["id"])

print(f"This is a new job: {new_job}")
print(f"This is a pushed chunk: {push_chunk}")
print(f"This is the submitted job: {submit_job}")