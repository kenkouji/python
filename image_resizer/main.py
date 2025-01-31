import cv2

# Read the image
image = cv2.imread("/Users/g.aasish/Desktop/GitHub/image_resizer/nig.jpeg", cv2.IMREAD_UNCHANGED)

# Check if the image was loaded successfully
if image is None:
    print("Error: Unable to load image. Please check the file path.")
else:
    # Display the image
    cv2.imshow("Image", image)

    # Wait for a key press and close the window
    cv2.waitKey(0)
    cv2.destroyAllWindows()
