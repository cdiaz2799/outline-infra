import pulumi
import pulumi_digitalocean as digitalocean

from project import outline_project, region
from vpc import vpc

# Setup Config
config = pulumi.Config()
redis_size = config.get('redis-size-slug', default='db-s-1vcpu-1gb')

# Setup Redis Instance
redis_instance = digitalocean.DatabaseCluster(
    'outline-redis',
    name='outline-redis',
    engine='redis',
    version='7',
    node_count=1,
    private_network_uuid=vpc.id,
    project_id=outline_project.id,
    region=region,
    size=redis_size,
    opts=pulumi.ResourceOptions(parent=outline_project),
)
pulumi.export('redis-cluster', redis_instance.name)
