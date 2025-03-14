import json
import boto3

#Initialize codepipeline
codepipeline = boto3.client('codepipeline')

def lambda_handler(event, context):
    try:
        cache = set()       #cache items already registered 
        totales = {}
#Open the Json File and store the content in data variable
        with open("entrada.json", "r") as f:
            data = json.load(f)
#iterate in the data from the json
        for item in data:
            obj_id = item["id"]
            amount = item["amount"]
            category = item["category"]
        #if the item is already registered , ignore the next update
            if obj_id in cache:
                continue  
        #if not register a new one in cache
            cache.add(obj_id)
        #if the item is not registered increment his category total
            if category in totales:
                totales[category] += amount
            else:
                totales[category] = amount
        #stdout totals after the loop
        output = {"totals_by_category": totales}
        print(json.dumps(output, indent=2))

        # Success CodePipeline
        if "jobId" in event:
            job_id = event["jobId"]
            codepipeline.put_job_success_result(jobId=job_id)

        return {
            "statusCode": 200,
            "body": json.dumps(output)
        }
    #Failure CodePipeline
    except Exception as e:
        print(f"Error: {str(e)}")
        if "jobId" in event:
            job_id = event["jobId"]
            codepipeline.put_job_failure_result(
                jobId=job_id,
                failureDetails={
                    "message": str(e),
                    "type": "JobFailed"
                }
            )
        raise
