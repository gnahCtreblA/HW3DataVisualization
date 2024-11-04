import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from collections import Counter

# Define the path to your dataset
dataset_path = "../dataset/images"

# Dictionary to store counts for each category and a sample image for each
category_counts = Counter()
sample_images = {}

# Loop through each folder in the dataset directory
for category in os.listdir(dataset_path):
    category_path = os.path.join(dataset_path, category)

    if os.path.isdir(category_path):
        image_files = [f for f in os.listdir(category_path) if os.path.isfile(os.path.join(category_path, f))]
        num_images = len(image_files)
        category_counts[category] = num_images

        # Store a sample image path if it exists
        if image_files:
            sample_images[category] = os.path.join(category_path, image_files[0])

# Sort counts from most to least and prepare data for bar chart
sorted_counts = category_counts.most_common()
categories = [category for category, count in sorted_counts]
counts = [count for category, count in sorted_counts]

fig, ax = plt.subplots(figsize=(16, 8))
bars = ax.bar(categories, counts, color='skyblue')
ax.set_ylabel('Number of Images', fontsize=20)
ax.set_xlabel('Categories',fontsize=20, labelpad=100)
ax.set_title('Number of Images in Each Category', fontsize=20)
ax.set_xticks(range(len(categories)))  # Position ticks for each bar
ax.set_xticklabels(categories)


# Add count labels on top of each bar
for bar, count in zip(bars, counts):
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), str(count),
            ha='center', va='bottom')



# Define parameters for image placement
image_width = 0.11
image_height = 0.11
y_offset = 0.08  # Position below each bar
spacing = 0   # Space between images

# Display sample images in a row
for i, category in enumerate(categories):
    if category in sample_images:
        img_path = sample_images[category]

        # Check if image path exists and load
        if os.path.exists(img_path):
            img = mpimg.imread(img_path)

            # Define inset axis for the image
            x0 = i * (0.834 / len(categories)) + 0.0625  # Center image under the bar
            inset_ax = fig.add_axes((x0, y_offset, image_width, image_height), transform=ax.transAxes)  # Adjust width and height

            # Display image in the inset axis
            inset_ax.imshow(img)
            inset_ax.axis('off')  # Hide inset axis
# Add category labels below the bars with specific y value


# Adjust y-axis limit to make room for images below the bars
plt.subplots_adjust(left=0.05, right=0.95, top=0.9, bottom=0.25)  # Adjust these values as needed
plt.show()