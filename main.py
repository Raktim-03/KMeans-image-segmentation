import numpy as np                                # handles pixel data
import matplotlib.pyplot as plt                   # for plotting the data
from sklearn.cluster import KMeans                # clustering algorithm
from PIL import Image                             # open image

# loading the image
image_path = input("Enter image path (or press Enter for default): ")
if image_path == "":
    image_path = "image.jpg"
image = Image.open(image_path)

#converting the image to array using numpy
image_array = np.array(image)


#getting the shape of the image
print("Image Shape :", image_array.shape)

#Reshape it into 2D array pixels
pixels = image_array.reshape(-1,3)      # -1 means adapt to any dimension automatically
print("Pixels shape :", pixels.shape)

#clustering
try :
    k = int(input("Enter the number of clusters k :"))
except ValueError:
    print("Invalid Input ! using default k = 5")
    k = 5

kmeans = KMeans(n_clusters=k, random_state=42)
kmeans.fit(pixels)

print("Clustering done with k =", k)

#replacing the centers with cluster center
segmented_pixels = kmeans.cluster_centers_[kmeans.labels_]

#reshape back to original image shape
segmented_image = segmented_pixels.reshape(image_array.shape)
segmented_image = segmented_image.astype(np.uint8)

plt.figure(figsize=(10,5))

#original image
plt.subplot(1,2,1)
plt.imshow(image_array)
plt.title("Original Image")
plt.xlabel("width(pixels)")
plt.ylabel("height(pixels)")


#segmented image
plt.subplot(1,2,2)
plt.title("Segmented")
plt.imshow(segmented_image)
plt.xlabel("width(pixels)")
plt.ylabel("height(pixels")

plt.tight_layout()
plt.show()
