from pycelonis import get_celonis
import csv_to_cleaned_df as clean_df
import config as c
from rich.console import Console
from time import sleep

# Global Variables and Envorinment Variables
connection_settings = {
    "celonis_url": c.API_URL,
    "api_token": c.API_TOKEN,
} 
console = Console()

# Connects to Celonis IBC
celonis = get_celonis(**connection_settings)

#Finds Data Pool
data_pool_id = "6b43443e-0cee-40bc-90fb-e941e42f41f8"
data_pool = celonis.pools.find(data_pool_id)

# Create Table in the data_pool based on Claims Data
with console.status("[bold green]Pushing data...") as status:
    create_table = data_pool.push_table(table_name='Claims', df_or_path=clean_df.df3, if_exists='replace')
    sleep(1)
    console.log(f"[green]Finished pushing data[/green]")
    console.log(f'[bold][red]Done!')
    #Validates table was created
    console.log(f'[bold][blue]Validating table: [green]{data_pool.tables}')