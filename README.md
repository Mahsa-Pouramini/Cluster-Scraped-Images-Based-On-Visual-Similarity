# Cluster Scraped Images Based On Visual Similarity 

In this project, we will scrap 10000 images to create our dataset and cluster them with their visual similarity using deep learning algorithms.

## Requirement
#### Install requirement

* Install with 'pip install -r requirement.txt' or 'pip3 install -r requirement.txt'


## Scraping data:

#### mini image scraper

In this part, we scraped N images of M pages of a particular department of the digikala website. we have used the women's shoe section that has 278 pages and 10005 images overall. we used BeautifulSoup library, and what it does is parses the webpage in its HTML format so we can easily access any of the HTML tags and even refine it with different classes.

#### Output

* Terminal:

This code passes pages of the website one by one and collects all the 'jpg' images, and shows you some messages that you can figure out where precisely the processing is.

* Collected dataset:

Images stored in the folder:
You can save the images, whether with their main labels or label them according to your need. I prefer to tag them in numerical order.

![alt text](https://github.com/Mahsa-Pouramini/Creating-Dataset-Out-of-Web-Scraped-Images/blob/main/screen%20shots/all.jpg) 

## clustering data

#### VGG16 model

after loading data, we use the VGG16 model witch is a convolutional neural network model for Large-Scale Image Recognition.It makes the improvement over AlexNet by replacing large kernel-sized filters (11 and 5 in the first and second convolutional layer, respectively) with multiple 3×3 kernel-sized filters one after another.

![alt text](https://github.com/Mahsa-Pouramini/Creating-Dataset-Out-of-Web-Scraped-Images/blob/main/screen%20shots/vgg.PNG)

you can learn more about VGG16 model [here](https://neurohive.io/en/popular-networks/vgg16/).

#### PCA

Principal Component Analysis (PCA) is an unsupervised, non-parametric statistical technique primarily used for dimensionality reduction in machine learning.We use it to reducing the dimensionality while keeping as much information as possible.It reduces the extracted components to 100 for a faster computation process.


#### KMeans clustering

We use This algorithm to group our feature vectors into k clusters. Each cluster should contain visually similar images.
The most critical thing here is, finding the optimal value of k; for doing this, we will use the Elbow method.

* Elbow Method:

In this method, we iterate the values of k from 2 to 30 and calculate the values of distortions for each value of k in the given range. To determine the optimal number of clusters, we have to select the value of k at the "elbow" ie, the point after which the distortion starts decreasing linearly. Thus for the given data, we conclude that the optimal number of clusters for the data is about 17.
 
![alt text](https://github.com/Mahsa-Pouramini/Creating-Dataset-Out-of-Web-Scraped-Images/blob/main/screen%20shots/elbow.PNG)

#### One last step

All we have left to do is to view a cluster to see how well our model did by inspecting the clusters.

![alt text](https://github.com/Mahsa-Pouramini/Creating-Dataset-Out-of-Web-Scraped-Images/blob/main/screen%20shots/clusterd.jpg)

##### it's all done :))



