# AWS Lambda

This repository is to showcase some of the AWS Lambda function I created and found to be useful.

## Table of Contents
1. [gZipExtractor](README.md#gzipextractor)


## gZipExtractor

This script reads in events when any files touches the s3 bucket. If that file has .gzip extension
then lambda automatically grabs the file using boto3. Itextracts the file via gzip and deletes the .gzip file again using boto3.

## Acknowledgement

Python code done by Rad Huda
 
## Questions
For questions feel free to email me at rad.huda@gmail.com

