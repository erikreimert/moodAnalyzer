import csv
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


def moodAnalyzer():
    # Load data from CSV
    # Load data from CSV, skip first row
    with open('inputData.csv', mode='r') as file:
        reader = csv.DictReader(file)
        next(reader)  # Skip the header row
        data = []
        for row in reader:
            tempo = float(row['tempo'])
            energy = float(row['energy'])
            data.append({'tempo': tempo, 'key': row['key'], 'energy': energy})

    # Extract features
    features = np.array([[song['tempo'], song['energy']] for song in data])

    # Normalize data
    scaler = StandardScaler()
    normalized_features = scaler.fit_transform(features)

    # Encode categorical 'key'
    key_encoder = OneHotEncoder()
    encoded_key = key_encoder.fit_transform(np.array([song['key'] for song in data]).reshape(-1, 1)).toarray()

    # Combine features
    encoded_data = np.concatenate((normalized_features, encoded_key), axis=1)

    # Apply K-means clustering
    n_clusters = 3  # Adjust as needed
    kmeans = KMeans(n_clusters=n_clusters)
    clusters = kmeans.fit_predict(encoded_data)

    visualize_clusters(encoded_data, clusters)

    # 'clusters' now contains the cluster assignments for each song
    return clusters


def visualize_clusters(encoded_data, clusters):
    pca = PCA(n_components=2)
    pca_result = pca.fit_transform(encoded_data)

    plt.scatter(pca_result[:, 0], pca_result[:, 1], c=clusters, cmap='viridis')
    plt.colorbar()
    plt.title('Cluster Visualization')
    plt.xlabel('PCA 1')
    plt.ylabel('PCA 2')
    plt.show()
