import { Construct } from "constructs";
import { App, TerraformOutput, TerraformStack } from "cdktf";

import { AwsProvider } from "@cdktf/provider-aws/lib/provider"
import { Instance } from "@cdktf/provider-aws/lib/instance"

class MyStack extends TerraformStack {
  constructor(scope: Construct, id: string) {
    super(scope, id);

    new AwsProvider(this, "AWS", {
      region: "us-east-1"
    })

    const ec2Instance = new Instance(this, "compute", {
      ami: "ami-0715c1897453cabd1",
      instanceType: "t2.micro"
    })
    
    new TerraformOutput(this, "public_ip", {
      value: ec2Instance.publicIp
    })

  }
}

const app = new App();
new MyStack(app, "cdktf-project");
app.synth();