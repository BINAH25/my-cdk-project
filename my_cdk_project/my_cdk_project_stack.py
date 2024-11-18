from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
    aws_ec2 as ec2,
    aws_s3 as s3,
)

from constructs import Construct

class MyCdkProjectStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # 1. Creating a VPC
        vpc = ec2.Vpc(self, "MyVpc", max_azs=2,  nat_gateways=1)

        # 2. Creating an EC2 instance in the public subnet
        instance = ec2.Instance(self, 
                                "MyInstance",
                                instance_type=ec2.InstanceType("t2.micro"),
                                machine_image=ec2.MachineImage.latest_amazon_linux(),
                                vpc=vpc,
                                vpc_subnets=ec2.SubnetSelection(subnets=vpc.public_subnets),
                                key_name="dev",
                                security_group=ec2.SecurityGroup(self, "MyInstanceSG",vpc=vpc))

        # 3. Creating an S3 bucket
        bucket = s3.Bucket(self, "MyBucket", versioned=False)