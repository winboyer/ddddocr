from PIL import Image
import cv2

# Read the image
image = Image.open('/Users/jinyfeng/Downloads/c4_20260327_162943.jpg')

# Get image dimensions
width, height = image.size

# Calculate 75% of width
crop_width = int(width * 0.75)

# Crop the image (left, top, right, bottom)
cropped_image = image.crop((0, 0, crop_width, height))

image = cv2.imread('/Users/jinyfeng/Downloads/c4_20260327_162943.jpg')
print(image.shape)  # Print original dimensions
height, width, channels = image.shape
crop_width = int(width * 0.75)  # Calculate 75% of width
image = image[:, :crop_width]  # Crop the image to 75% of its width

# Save or display
# cropped_image.save('/Users/jinyfeng/Downloads/cropped_image.png')
# cropped_image.show()