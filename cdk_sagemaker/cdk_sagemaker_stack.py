from aws_cdk import core
import aws_cdk.aws_s3 as s3
import aws_cdk.aws_sagemaker as sagemaker


class CdkSagemakerStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        bucket1 = s3.Bucket(self,
    		"BucketCDK", 
    		versioned=True,
    		bucket_name='cdk-sagemaker-bucket-s843971001',
            removal_policy=core.RemovalPolicy.DESTROY)

        sm_notebook = sagemaker.CfnNotebookInstance(self,
        "SageMakerNotebookInstance",
         instance_type='ml.m4.xlarge',
         role_arn='arn:aws:iam::304472691870:role/aws-sagemaker-role-s843971',
         notebook_instance_name='cdk-sagemaker-notebook-s843971',
         default_code_repository='https://github.com/abdul-pfg/sagemaker-iris')
