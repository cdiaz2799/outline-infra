import pulumi
import pulumi_digitalocean as digitalocean

from project import outline_project, region

# Setup Config
config = pulumi.Config()
fqdn = config.require('fqdn')

# Setup Bucket
bucket = digitalocean.SpacesBucket(
    'outline-s3-bucket',
    name='outline-s3',
    region=region,
    acl='private',
    opts=pulumi.ResourceOptions(protect=True),
)


bucket_cors = digitalocean.SpacesBucketCorsConfiguration(
    'outline-s3-bucket-cors',
    bucket=bucket.name,
    region=bucket.region,
    cors_rules=[
        digitalocean.SpacesBucketCorsConfigurationCorsRuleArgs(
            allowed_methods=['GET'],
            allowed_origins=['*'],
        ),
        digitalocean.SpacesBucketCorsConfigurationCorsRuleArgs(
            allowed_headers=['*'],
            allowed_methods=[
                'POST',
                'PUT',
            ],
            allowed_origins=[fqdn],
        ),
    ],
    opts=pulumi.ResourceOptions(parent=bucket, depends_on=[bucket]),
)

# Setup Project Attachment
project_resource = digitalocean.ProjectResources(
    'outline-bucket-project-resource',
    project=outline_project.id,
    resources=[bucket.bucket_urn],
    opts=pulumi.ResourceOptions(parent=bucket),
)

# Setup Output
pulumi.export('s3-bucket-name', bucket.name)
