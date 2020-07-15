#!/usr/bin/env python3

from aws_cdk import core

from cdk_sagemaker.cdk_sagemaker_stack import CdkSagemakerStack


app = core.App()
CdkSagemakerStack(app, "cdk-sagemaker")

app.synth()
