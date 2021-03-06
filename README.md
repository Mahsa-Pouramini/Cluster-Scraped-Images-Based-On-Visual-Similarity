# Mini Image Scraper
This project has the purpose of illustrating an elementary example of web scraping for images on [digikala](https://www.digikala.com), which is a Commercial Persian website.

## Requirement:
#### Install Requirement:
* Install with 'pip install -r requirement.txt' or 'pip3 install -r requirement.txt'

#### Description
In this project, we scraped N images of M pages of a particular department of the digikala website. In my case, I have used the women's shoe department that has 278 pages and 10005 images overall. I used a beautiful soup library, and what it does is parses the webpage in its HTML format so we can easily access any of the HTML tags and even refine it with different classes.
I scraped these images, and I will use them in a machine learning project as a robust dataset collected by myself.

#### Output

* Terminal:

This code passes pages of the website one by one and collects all the 'jpg' images, and shows you some messages that you can figure out where precisely the processing is.

![alt text](https://github.com/mahsa-pam/Creating-Dataset-Out-of-Web-Scraped-Images/blob/main/screen%20shots/output.PNG)

* Collected dataset:

Images stored in the folder 

![alt text](https://github.com/mahsa-pam/Creating-Dataset-Out-of-Web-Scraped-Images/blob/main/screen%20shots/shoes.PNG)

#### Next Updates
We'll use these scraped shoe images as training data and clustering them with machine learning algorithms in the following updates.