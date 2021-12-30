"""
Generate Pencil Sketch from Photo in Python
https://towardsdatascience.com/generate-pencil-sketch-from-photo-in-python-7c56802d8acb
"""
import cv2


def img2sketch(photo, k_size):
    # Read Image
    img = cv2.imread(photo)
    assert img is not None, "image reading failed"

    # Convert to Grey Image
    grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Invert Image
    invert_img = cv2.bitwise_not(grey_img)

    # Blur image
    blur_img = cv2.GaussianBlur(invert_img, (k_size, k_size), 0)

    # Invert Blurred Image
    invblur_img = cv2.bitwise_not(blur_img)

    # Sketch Image
    sketch_img = cv2.divide(grey_img, invblur_img, scale=256.0)

    # Save Sketch
    cv2.imwrite('sketch.jpg', sketch_img)

    # Display sketch
    cv2.imshow('sketch image', sketch_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Function call
img2sketch(photo='c.jpg', k_size=19)
