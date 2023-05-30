from dotenv import load_dotenv
import os

from constructs import Construct
from cdktf import App, TerraformStack, TerraformOutput
from cdktf_cdktf_provider_aws.provider import AwsProvider
from cdktf_cdktf_provider_aws.instance import Instance

load_dotenv()

class MyStack(TerraformStack):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        AwsProvider(
            self,
            "AWS",
            region="us-east-1",
            access_key=os.environ['ACCESS_KEY'],
            secret_key=os.environ['SECRET_KEY']
        )
        
        instance = Instance(
            self,
            "compute",
            ami="ami-0715c1897453cabd1",
            instance_type="t2.micro",
        )

        TerraformOutput(
            self,
            "public_ip",
            value=instance.public_ip
        )

app = App()
MyStack(app, "cdktf-project")

app.synth()
