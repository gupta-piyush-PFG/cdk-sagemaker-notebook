from aws_cdk import core
import aws_cdk.aws_s3 as s3
import aws_cdk.aws_sagemaker as sagemaker


class CdkSagemakerStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        bucket1 = s3.Bucket(self,
    		"BucketCDK", 
    		versioned=True,
    		bucket_name='minotaur-data-bucket',
            removal_policy=core.RemovalPolicy.DESTROY)
        
        bucket2 = s3.Bucket(self,
    		"BucketCDK", 
    		versioned=True,
    		bucket_name='minotaur-data-bucket-1',
            removal_policy=core.RemovalPolicy.DESTROY)

        sm_notebook = sagemaker.CfnNotebookInstance(self,
        "SageMakerNotebookInstance",
         instance_type='ml.t2.medium',
         role_arn='arn:aws:iam::148231576589:role/sagemaker-g406428',
         notebook_instance_name='minotaur-notebook',
         default_code_repository='https://github.com/abdul-pfg/sagemaker-iris')
