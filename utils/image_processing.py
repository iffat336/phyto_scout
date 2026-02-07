import numpy as np
from PIL import Image

def calculate_green_index(image_file):
    """
    Calculates the ratio of green pixels in the image to estimate biomass.
    This is a simplified computer vision approach often used in phenotyping.
    
    Args:
        image_file: Uploaded file object or PIL Image.
        
    Returns:
        float: Percentage of green pixels (0-100).
        Image: processed image with green mask (for visualization).
    """
    # Convert to PIL Image if it's not already
    img = Image.open(image_file).convert("RGB")
    
    # Convert to NumPy array
    img_array = np.array(img)
    
    # Extract RGB channels
    r = img_array[:, :, 0]
    g = img_array[:, :, 1]
    b = img_array[:, :, 2]
    
    # Define "Green" condition: Green > Red AND Green > Blue
    # This is a basic Excess Green Index (ExG) approach
    green_mask = (g > r) & (g > b)
    
    # Calculate ratio
    total_pixels = img_array.shape[0] * img_array.shape[1]
    green_pixels = np.sum(green_mask)
    
    if total_pixels == 0:
        return 0.0, img
        
    green_ratio = (green_pixels / total_pixels) * 100
    
    # Create a masked image for display (turning non-green pixels grayscale)
    # This helps the user see what the computer "sees"
    gray = img.convert("L")
    gray_array = np.array(gray)
    img_array[~green_mask] = np.stack([gray_array[~green_mask]]*3, axis=-1)
    
    processed_img = Image.fromarray(img_array)
    
    return green_ratio, processed_img
