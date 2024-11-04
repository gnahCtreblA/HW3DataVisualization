import os
import matplotlib.pyplot as plt
from collections import Counter

# Define the path to your dataset
dataset_path = "../dataset/images"

# Dictionary to store counts for each category
category_counts = Counter()

# Loop through each folder in the dataset directory
for category_folder in os.listdir(dataset_path):
    # Get the path to the category folder
    category_path = os.path.join(dataset_path, category_folder)

    # Check if it is a folder (in case there are any non-folder files)
    if os.path.isdir(category_path):
        # Count the images in the category folder
        num_images = len([f for f in os.listdir(category_path) if os.path.isfile(os.path.join(category_path, f))])

        # Update the counter with the category name and image count
        category_counts[category_folder] = num_images

# Extract the counts to use in the histogram
counts = list(category_counts.values())

# Calculate the range of data
min_count = min(counts)
max_count = max(counts)

# Create a histogram of the count frequencies in different ranges
plt.figure(figsize=(10, 6))
n, bins, patches = plt.hist(counts, bins=10, color='salmon', edgecolor='black')  # Set bins based on your desired range
plt.xlabel('Range of Image Counts')
plt.ylabel('Number of Categories')
plt.title(f'Distribution of Image Counts Across Categories\nRange: {min_count} to {max_count}')
plt.tight_layout()

# Add frequency labels above each bin in the histogram
for i in range(len(patches)):
    height = patches[i].get_height()
    if height > 0:
        plt.text(patches[i].get_x() + patches[i].get_width() / 2, height, str(int(height)),
                 ha='center', va='bottom')  # Center text on the bin

# Display the histogram
plt.show()
