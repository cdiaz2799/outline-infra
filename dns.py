import pulumi
from pulumi_cloudflare import Record

from app import outline_app

# Setup Config
config = pulumi.Config('cf')
zoneid = config.require('zoneId')

# Setup Inputs
url = outline_app.default_ingress
cname = url.apply(lambda url: url.replace('https://', ''))

# Setup Record
record = Record(
    'outline-dns-record',
    name='outline',
    type='CNAME',
    zone_id=zoneid,
    allow_overwrite=True,
    comment='Managed by Pulumi',
    proxied=True,
    value=cname,
    opts=pulumi.ResourceOptions(parent=outline_app),
)

# Setup Output
pulumi.export('app-url', lambda url: 'https://' + record.hostname)
