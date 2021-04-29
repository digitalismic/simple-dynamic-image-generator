# About Script

This python script will help you generate images with text by providing and argument. This is useful if you want to create set of images for your development requirements such as load testing without worrying about copyright (if you randomly scrapping & download it from internet)

Random unique prefix will be appended into file name & by default, this script will create 100px * 30px .png image with size less than 300Bytes.

## Dependencies

[Python](https://www.python.org/) 2.4 or greater check your version with -- `python --version`  or `python3 --version`
[Pillow](https://pillow.readthedocs.io/en/stable/)  --- `pip install Pillow` 

## How to Use

Create folder to store result `mkdir ./images`
Generate image with text KOMODO `python dynamic-image-generator.py KOMODO`
Result :  

> ![komodo](https://raw.githubusercontent.com/digitalismic/simple-dynamic-image-generator/main/images/fed22b65-KOMODO.png)
