import os
import matplotlib.pyplot as plt
from collections import Counter

# Define the path to your dataset
dataset_path = "./dataset/images"

# Dictionary to store counts for each category
category_counts = Counter()

# Loop through each folder in the dataset directory
for images in os.listdir(dataset_path):
    # Get the path to the category folder
    category_path = os.path.join(dataset_path, images)

    # Check if it is a folder (in case there are any non-folder files)
    if os.path.isdir(category_path):
        # Count the images in the category folder
        num_images = len([f for f in os.listdir(category_path) if os.path.isfile(os.path.join(category_path, f))])

        # Update the counter with the category name and image count
        category_counts[images] = num_images

# Display the counts for each category
print("Image counts by category:")
for category, count in category_counts.items():
    print(f"{category}: {count} images")

# Sort the category counts from most to least
sorted_category_counts = category_counts.most_common()  # This returns a list of tuples sorted by count

# Prepare data for the histogram
categories = [category for category, count in sorted_category_counts]
counts = [count for category, count in sorted_category_counts]

# Create a bar chart
plt.figure(figsize=(10, 6))
plt.bar(categories, counts, color='skyblue')
plt.xlabel('Categories')
plt.ylabel('Number of Images')
plt.title('Number of Images in Each Category')
plt.xticks(rotation=45)  # Rotate category labels for better readability
plt.tight_layout()  # Adjust layout to make room for rotated labels
plt.show()