import numpy as np
from sklearn.cluster import KMeans
from PIL import Image
import streamlit as st

# Title
st.title("Image Segmentation using K-Means")

# Upload image
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

# Slider for k
k = st.slider("Select number of clusters (k)", 2, 10, 5)

if uploaded_file is not None:
    # Load image
    image = Image.open(uploaded_file)
    image_array = np.array(image)

    st.write("Image Shape:", image_array.shape)

    # Reshape
    pixels = image_array.reshape(-1, 3)
    st.write("Pixels Shape:", pixels.shape)

    # Clustering
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(pixels)

    st.write("Clustering done with k =", k)

    # Replace pixels
    segmented_pixels = kmeans.cluster_centers_[kmeans.labels_]

    # Reshape back
    segmented_image = segmented_pixels.reshape(image_array.shape)
    segmented_image = segmented_image.astype(np.uint8)

    # Show images
    st.subheader("Results")
    col1, col2 = st.columns(2)

    with col1:
        st.image(image_array, caption="Original Image")

    with col2:
        st.image(segmented_image, caption="Segmented Image")