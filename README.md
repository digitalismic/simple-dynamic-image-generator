# About Script

This python script will help you generate images with text by providing and argument. This is useful if you want to create set of images for your development requirements such as load testing without worrying about copyright (if you randomly scrapping & download it from internet)

Random unique prefix will be appended into file name & by default, this script will create 100px * 30px .png image with size less than 300 Bytes.

## Dependencies

[Python](https://www.python.org/) 2.4 or greater check your version with -- `python --version`  or `python3 --version`

[Pillow](https://pillow.readthedocs.io/en/stable/)  -- `pip install Pillow` 

## How to Use

Create folder to store result `mkdir ./images`

Generate image with text KOMODO `python dynamic-image-generator.py KOMODO`
Result :  

> ![komodo](https://raw.githubusercontent.com/digitalismic/simple-dynamic-image-generator/main/images/fed22b65-KOMODO.png)


## Practical Use Case ; Example

**Scenario** : You need to create *1000 images* with *random number* and upload it into an *Amazon S3 Bucket* for a development requirement. In this scenario, we're going to use AWS Cloud9.

[AWS Cloud9](https://aws.amazon.com/cloud9/) is a cloud-based integrated development environment (IDE) that lets you write, run, and debug your code with just a browser. It also provide AWS S3 integration using AWS managed temporary credentials, so you will have access to your bucket without need to provide a static access & secret key. 

Enable auto shutdown when there is no activity on your AWS Cloud9 instance to save money. If your running t3.small (2vCPU and 2GiB RAM) for 4 hours per day, you will spent 13.32 USD Monthly. Detail calculation [here](https://calculator.aws/#/estimate?id=be76a61e45e9d7199c0fce6da17f3d321a98256b)

- Step 1 : Login into your AWS account, search for service 'AWS Cloud9'

- Step 2 : Create AWS Cloud9 Environment

- Step 3 : Clone script from Github `git clone https://github.com/digitalismic/simple-dynamic-image-generator`

- Step 4 : Install dependencies `pip install pillow --user Admin`

- Step 5 : Go to script folder and create 1000 images `for i in {1..1000}; do python ./dynamic-image-generator.py $RANDOM; done` *it took around 1~2 minutes using t3.small with total size of 4.0M*

- Step 6 : S3 sync your images to your destination Bucket `aws s3 sync ./images/ s3://DESTINATION-BUCKET`

Done


> ![result-100](https://github.com/digitalismic/simple-dynamic-image-generator/blob/main/images/random-image-generator-100.png)
