from azure.cosmos import CosmosClient, exceptions
import os

url = os.environ['ACCOUNT_URI']
key = os.environ['ACCOUNT_KEY']

RES_GROUP=GitHubARM
ACCT_NAME=githubcosmosdb

export ACCOUNT_URI=$(az cosmosdb show --resource-group $RES_GROUP --name $ACCT_NAME --query documentEndpoint --output tsv)
export ACCOUNT_KEY=$(az cosmosdb list-keys --resource-group $RES_GROUP --name $ACCT_NAME --query primaryMasterKey --output tsv)


client = CosmosClient(url, credential=key)
database_name = 'testDatabase'
try:
    database = client.create_database(database_name)
    container = database.create_container(id=container_name, partition_key=PartitionKey(path="/productName"))
except exceptions.CosmosResourceExistsError:
    database = client.get_database_client(database_name)
    container = database.get_container_client(container_name)
except exceptions.CosmosHttpResponseError:
    raise
