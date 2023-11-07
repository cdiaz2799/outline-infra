import pulumi
import pulumi_digitalocean as digitalocean

from bucket import bucket
from outline_redis import redis_instance
from project import region

# Setup Config
config = pulumi.Config()
domain = config.require('domain')
app_version = config.get('version', default='latest')
database_name = 'outline-db'
fqdn = config.require('fqdn')
from_email = config.require('from-email')
smtp_host = config.require('smtp-host')
smtp_port = config.require('smtp-port')
smtp_username = config.require_secret('smtp-username')
smtp_password = config.require_secret('smtp-password')
slack_app_id = config.require_secret('slack-app-id')
slack_client_id = config.require_secret('slack-client-id')
slack_client_secret = config.require_secret('slack-client-secret')
slack_verification_token = config.require_secret('slack-verification-token')

# Retrieve Secrets
access_key_id = config.require_secret('sa-access-key-id')
secret_access_key = config.require_secret('sa-secret-access-key')
secret_key = config.require_secret('secret-key')
utils_secret = config.require_secret('utils-secret')
database_url_string = config.get('database_url-string')

# Setup App
outline_app = digitalocean.App(
    'outline-app',
    spec=digitalocean.AppSpecArgs(
        name='outline',
        region=region,
        alerts=[
            digitalocean.AppSpecAlertArgs(
                rule='DEPLOYMENT_FAILED',
            ),
            digitalocean.AppSpecAlertArgs(
                rule='DOMAIN_FAILED',
            ),
        ],
        databases=[
            digitalocean.AppSpecDatabaseArgs(
                engine='PG',
                name=database_name,
            ),
            digitalocean.AppSpecDatabaseArgs(
                cluster_name=redis_instance.name,
                engine='REDIS',
                name=redis_instance.name,
                production=True,
                version=redis_instance.version,
            ),
        ],
        domain_names=[
            digitalocean.AppSpecDomainNameArgs(
                name=domain, type='PRIMARY', wildcard=False
            ),
        ],
        ingress=digitalocean.AppSpecIngressArgs(
            rules=[
                digitalocean.AppSpecIngressRuleArgs(
                    component=digitalocean.AppSpecIngressRuleComponentArgs(
                        name='outline',
                    ),
                    match=digitalocean.AppSpecIngressRuleMatchArgs(
                        path=digitalocean.AppSpecIngressRuleMatchPathArgs(
                            prefix='/',
                        ),
                    ),
                )
            ],
        ),
        services=[
            digitalocean.AppSpecServiceArgs(
                envs=[
                    digitalocean.AppSpecServiceEnvArgs(
                        key='AWS_REGION',
                        value=bucket.region,
                    ),
                    digitalocean.AppSpecServiceEnvArgs(
                        key='AWS_S3_ACL',
                        value=bucket.acl,
                    ),
                    digitalocean.AppSpecServiceEnvArgs(
                        key='AWS_S3_UPLOAD_BUCKET_URL',
                        value=f'https://{bucket.bucket_domain_name}',
                    ),
                    digitalocean.AppSpecServiceEnvArgs(
                        key='AWS_S3_FORCE_PATH_STYLE',
                        value='false',
                    ),
                    digitalocean.AppSpecServiceEnvArgs(
                        key='AWS_S3_ACCELERATE_URL',
                        value=f'https://{bucket.bucket_domain_name}',
                    ),
                    digitalocean.AppSpecServiceEnvArgs(
                        key='AWS_S3_UPLOAD_BUCKET_NAME',
                        value=bucket.name,
                    ),
                    digitalocean.AppSpecServiceEnvArgs(
                        key='AWS_SECRET_ACCESS_KEY',
                        type='SECRET',
                        value=secret_access_key,
                    ),
                    digitalocean.AppSpecServiceEnvArgs(
                        key='AWS_ACCESS_KEY_ID',
                        type='SECRET',
                        value=access_key_id,
                    ),
                    digitalocean.AppSpecServiceEnvArgs(
                        key='SECRET_KEY',
                        type='SECRET',
                        value=secret_key,
                    ),
                    digitalocean.AppSpecServiceEnvArgs(
                        key='UTILS_SECRET',
                        type='SECRET',
                        value=utils_secret,
                    ),
                    digitalocean.AppSpecServiceEnvArgs(
                        key='DATABASE_URL',
                        type='SECRET',
                        value=database_url_string,
                    ),
                    digitalocean.AppSpecServiceEnvArgs(
                        key='RATE_LIMITER_ENABLED',
                        value='true',
                    ),
                    digitalocean.AppSpecServiceEnvArgs(
                        key='RATE_LIMITER_REQUESTS',
                        value='1000',
                    ),
                    digitalocean.AppSpecServiceEnvArgs(
                        key='RATE_LIMITER_DURATION_WINDOW',
                        value='60',
                    ),
                    digitalocean.AppSpecServiceEnvArgs(
                        key='ENABLE_UPDATES',
                        value='true',
                    ),
                    digitalocean.AppSpecServiceEnvArgs(
                        key='FORCE_HTTPS',
                        value='false',
                    ),
                    digitalocean.AppSpecServiceEnvArgs(
                        key='MAXIMUM_IMPORT_SIZE',
                        value='5120000',
                    ),
                    digitalocean.AppSpecServiceEnvArgs(
                        key='LOG_LEVEL',
                        value='warn',
                    ),
                    digitalocean.AppSpecServiceEnvArgs(
                        key='DEFAULT_LANGUAGE',
                        value='en_US',
                    ),
                    digitalocean.AppSpecServiceEnvArgs(
                        key='URL',
                        value=fqdn,
                    ),
                    digitalocean.AppSpecServiceEnvArgs(
                        key='SMTP_PORT',
                        value=smtp_port,
                    ),
                    digitalocean.AppSpecServiceEnvArgs(
                        key='SMTP_HOST',
                        value=smtp_host,
                    ),
                    digitalocean.AppSpecServiceEnvArgs(
                        key='SMTP_FROM_EMAIL',
                        value=from_email,
                    ),
                    digitalocean.AppSpecServiceEnvArgs(
                        key='SMTP_SECURE',
                        value='true',
                    ),
                    digitalocean.AppSpecServiceEnvArgs(
                        key='SMTP_USERNAME',
                        type='SECRET',
                        value=smtp_username,
                    ),
                    digitalocean.AppSpecServiceEnvArgs(
                        key='SMTP_REPLY_EMAIL',
                        value=from_email,
                    ),
                    digitalocean.AppSpecServiceEnvArgs(
                        key='SMTP_PASSWORD', type='SECRET', value=smtp_password
                    ),
                    digitalocean.AppSpecServiceEnvArgs(
                        key='SLACK_APP_ID',
                        type='SECRET',
                        value=slack_app_id,
                    ),
                    digitalocean.AppSpecServiceEnvArgs(
                        key='SLACK_CLIENT_ID',
                        type='SECRET',
                        value=slack_client_id,
                    ),
                    digitalocean.AppSpecServiceEnvArgs(
                        key='SLACK_CLIENT_SECRET',
                        type='SECRET',
                        value=slack_client_secret,
                    ),
                    digitalocean.AppSpecServiceEnvArgs(
                        key='SLACK_MESSAGE_ACTIONS',
                        value='true',
                    ),
                    digitalocean.AppSpecServiceEnvArgs(
                        key='SLACK_VERIFICATION_TOKEN',
                        type='SECRET',
                        value=slack_verification_token,
                    ),
                    digitalocean.AppSpecServiceEnvArgs(
                        key='REDIS_URL',
                        value=redis_instance.uri,
                        type='SECRET',
                    ),
                    digitalocean.AppSpecServiceEnvArgs(
                        key='NODE_ENV',
                        value='production',
                    ),
                    digitalocean.AppSpecServiceEnvArgs(
                        key='NODE_TLS_REJECT_UNAUTHORIZED', value='0'
                    ),
                ],
                http_port=3000,
                image=digitalocean.AppSpecServiceImageArgs(
                    registry='outlinewiki',
                    registry_type='DOCKER_HUB',
                    repository='outline',
                    tag=app_version,
                ),
                instance_size_slug='basic-xxs',
                name='outline',
            )
        ],
    ),
    opts=pulumi.ResourceOptions(depends_on=[bucket, redis_instance]),
)

# Setup Outputs
pulumi.export('app-cname', outline_app.default_ingress)
