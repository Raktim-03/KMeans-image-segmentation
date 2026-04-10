# K-Means Image Segmentation

A web app that performs **image segmentation using K-Means clustering**. Upload an image and visualize how it is segmented into clusters.

## Live Demo

link : https://kmeans-image-segmentation-cmzj6jqpkypf9k5cosjn9w.streamlit.app/

---

## Features

* Upload any image
* Apply K-Means clustering
* Choose number of clusters (K)
* Visualize segmented output

---

## How It Works

* Each pixel is treated as a data point (RGB values)
* K-Means clusters pixels into K groups
* Each cluster represents a segment of the image

---

## Tech Stack

* Python
* NumPy
* Scikit-learn
* Matplotlib
* Streamlit

---


## Installation

```bash
git clone https://github.com/Raktim-03/KMeans-image-segmentation.git
cd KMeans-image-segmentation
pip install -r requirements.txt
streamlit run app.py
```

---

## Project Structure

```
├── app.py
├── main.py
├── requirements.txt
└── README.md
```

---

## Future Improvements

* Add different clustering algorithms
* Improve UI/UX
* Add real-time parameter tuning

---

## Author

Raktim Ranjan Handique
