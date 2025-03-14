# AWS-Pipelines: Lambda,S3,CodePipelines,CodeBuild


This project is an AWS scenario where i will be using AWS Pipelines to automate the refresh in a lambda function for a script execution when i throw the script into an S3.

## Diagram
![alt text](https://github.com/JaimeMLGT/AWS-Pipelines-Lambda-S3/blob/main/awspipeline.jpg)
## Technologies Used 
* CloudFormation
* CodePipeline
* CodeBuild
* Lambda
* S3
* CloudWatch
* Python development
 

## STAR method Explanation

The **situation** here is a case scenario based on an implementation that i did as requested by an end client.They needed an script that could read from a json and based on cache , they only work with the first element that was inserted in the json.They had an S3 when they wanted to load the script in .zip format and they wanted to have an instant update with seamless integration in the Lambda function that should execute the script.

The **task** here was to obtain that seamless integration with a lambda function based on a quick upload from an S3 bucket.Also my dutty in this case was to build a python script that could simulate that case scenario very fairly. 

The **actions** the actions that i took in this scenario was to build a python script that could consider the first register in the json for a particular element.Also they needed an AWS pipeline to make automatic updates once that you already upload a file into the S3.For more clarity on the steps i used CodeBuild too check any weird behaviour that the pipeline itself could have.Of course , the Lambda creation was defined as a Cloudformation template , the same template that i used for the pipeline.

As a **result**  i built a pipeline that could automate the mission to acomplish and all the configurations needed as well.The client was happy about the end result , the pipeline deploys very fast the solution and any logic implementation is needed for further situations.

## Considerations 
* Once that you executed the pipeline once you can watch on live the process in CloudWatch.
* Relevant to activate versioning in the S3 bucket.The Old versions will be stored as a new folder with the name of the deployment defined in the cloudformation template.
* This version will be updated with new features and bug fixes.


# End Credits
This program is ready to use and set up if you wanna to give it a try , so feel free to use it with responsability and don't forget to write your own values in the yaml file.
