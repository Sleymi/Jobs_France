# Jobs_France
Get the job in France

version python3
Requirements: requests and scrapy.

Usage

python3 req.py
A folder contains web pages will be created.
put the path of the folder in the variable "path" in the file parse.py 

"""
import scrapy
import re
import glob


class Sp(scrapy.Spider):
    name = "sp1"

    path = "/home/mohamed/Desktop/Jobs-go/res_17_11_2019__08_51_12"
    
    all = glob.glob(path + "/*")

"""

then run
scrapy runspider parse.py -o res.csv

the res.csv contains the result of parsing.
