import boto3

def lambda_handler(event, context):

    k = "f61b2fa6-b2c3-4436-8bd1-5470b8c65377.csv"
    b = "lambda-functions-cm443"
    # Connect to S3
    s3 = boto3.client('s3')

    # Retrieve the CSV file from the S3 bucket
    response = s3.get_object(Bucket=b, Key=k)
    csv_file = response['Body'].read()

    # Convert the binary data to a string
    csv_string = csv_file.decode()

    # Split the string into a list of lines
    lines = csv_string.split('\n')

    # Modify the IP addresses in the file
    for i, line in enumerate(lines):
        if i != 0 and i != len(lines) - 1:  # Check if it's not the first line or the last line
            columns = line.strip().split(',')
            columns[0] = columns[0] + '/32'
            lines[i] = ','.join(columns)

    # Join the modified lines back into a single string
    csv_string_modified = '\n'.join(lines)

    # Convert the modified string back to binary data
    csv_file_modified = csv_string_modified.encode()

    # Write the modified file back to the S3 bucket
    s3.put_object(Bucket=b, Key=k, Body=csv_file_modified)