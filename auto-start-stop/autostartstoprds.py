import boto3

region  = "ap-south-1"
cluster = "database-1"

def status(cluster):
    client = boto3.client('rds', region_name=region)

    response = client.describe_db_clusters(
        DBClusterIdentifier=cluster
    )
    for dbclusters in response['DBClusters']:
        if dbclusters['Status'] == 'available':
            print ('available')
            client.stop_db_cluster(
                DBClusterIdentifier=cluster
            )
        elif dbclusters['Status'] == 'stopped':
            print ('stopped')
            client.start_db_cluster(
                DBClusterIdentifier=cluster
            )

status(cluster)