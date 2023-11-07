import pulumi
import pulumi_digitalocean as digitalocean

from project import region

vpc = digitalocean.Vpc(
    'outline-vpc',
    name='outline-vpc',
    region=region,
    opts=pulumi.ResourceOptions(protect=True),
)

# Setup Outputs
pulumi.export('vpc', vpc.name)
