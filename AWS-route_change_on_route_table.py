import boto.utils
from boto.vpc import VPCConnection
import boto3

##The below two lines can give you a list of all the route tables in the VPC. This uses an older Boto and hence you will have to specify the region##

#conn=boto3.vpc.connect_to_region("region-string")
#c1=client.get_all_route_tables()
#print c1



##The below lines will create route in an existing table for you. You can add this as many times as you like for addign routes to multiple route tables. This uses Boto3 for which region code is not required; however you will have to execute the script on a device in the same VPC##

client = boto3.client("ec2")

c2=client.create_route(

    RouteTableId='string',
    DestinationCidrBlock='string',
    GatewayId='string',
)


##you can use the below lines to pring out the details of a route table if you need to before making the aobve change or to check the state of the route table after making a change to it##

response = client.describe_route_tables(
    RouteTableIds=[
        'string',
    ],
)

print(response)
