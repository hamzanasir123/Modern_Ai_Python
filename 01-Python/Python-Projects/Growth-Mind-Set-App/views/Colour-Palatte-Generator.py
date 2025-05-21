import streamlit as st
import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import webcolors

def rgb_to_hex(rgb):
    """Convert RGB tuple to HEX color."""
    return "#{:02x}{:02x}{:02x}".format(rgb[0], rgb[1], rgb[2])

def extract_colors(image, num_colors=5):
    """Extract dominant colors using KMeans clustering."""
    img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB
    img = img.reshape((-1, 3))  # Flatten image array
    kmeans = KMeans(n_clusters=num_colors, random_state=42, n_init=10)
    kmeans.fit(img)
    colors = kmeans.cluster_centers_.astype(int)  # Get dominant colors
    return colors

# Streamlit UI
st.title("🎨 Color Palette Generator")
st.write("Upload an image to extract its dominant colors and see magic!.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)  # Read image

    # Show uploaded image
    st.image(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), caption="Uploaded Image", use_container_width=True)

    num_colors = st.slider("Select number of colors:", min_value=2, max_value=10, value=5)

    # Extract dominant colors
    colors = extract_colors(image, num_colors)

    # Display color swatches and HEX codes
    st.subheader("Extracted Colors:")
    cols = st.columns(num_colors)
    
    for i, col in enumerate(cols):
        hex_color = rgb_to_hex(colors[i])
        col.markdown(f'<div style="background-color:{hex_color}; width: 100px; height: 100px; border-radius: 5px;"></div>', unsafe_allow_html=True)
        col.write(f"`{hex_color}`")  # Display HEX code

    # Copy HEX codes
    hex_list = ", ".join([rgb_to_hex(c) for c in colors])
    st.text_input("Copy HEX codes:", hex_list)
