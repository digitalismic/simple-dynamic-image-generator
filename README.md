# About Script

This python script will help you generate images with text by providing and argument. This is useful if you want to create set of images for your development requirements such as load testing without worrying about copyright (if you randomly scrapping & download it from internet)

Random unique prefix will be appended into file name & by default, this script will create 100px * 30px .png image with size less than 300Bytes.

## Dependencies

[Python](https://www.python.org/) 2.4 or greater check your version with -- `python --version`  or `python3 --version`

[Pillow](https://pillow.readthedocs.io/en/stable/)  -- `pip install Pillow` 

## How to Use

Create folder to store result `mkdir ./images`

Generate image with text KOMODO `python dynamic-image-generator.py KOMODO`
Result :  

> ![komodo](https://raw.githubusercontent.com/digitalismic/simple-dynamic-image-generator/main/images/fed22b65-KOMODO.png)


## Practical Use Case ; Example

**Scenario** : You need to create *1000 images* with *random number* and upload it into an *Amazon S3 Bucket* for a development requierement 

Step 1 : Login into your AWS account, search for service 'AWS Cloud9'

Step 2 : Create AWS Cloud9 Environment

Step 3 : Clone script from Github `git clone https://github.com/digitalismic/simple-dynamic-image-generator`

Step 4 : Install dependencies `pip install pillow --user Admin`

Step 5 : Go to script folder and create 1000 images `for i in {1..1000}; do python ./dynamic-image-generator.py $RANDOM; done`

Step 6 : S3 sync your images to your destination Bucket `aws s3 sync ./images/ s3://DESTINATION-BUCKET`

Done


> ![result-100](https://github.com/digitalismic/simple-dynamic-image-generator/blob/main/images/random-image-generator-100.png)
