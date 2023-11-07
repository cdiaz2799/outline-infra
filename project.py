import pulumi
import pulumi_digitalocean as digitalocean

# Setup Config
config = pulumi.Config()
region = config.get('do-region')

outline_project = digitalocean.Project(
    'outline-project',
    name='outline',
    environment='Production',
    purpose='Web Application',
    opts=pulumi.ResourceOptions(protect=True),
)
