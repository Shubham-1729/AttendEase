import cv2

# Load an image using 'imread' specifying the path to image
img = cv2.imread("/imageatt/disha.jpg")

# Display the image in a window
cv2.imshow("image", img)

# Wait for any key before the window closes
cv2.waitKey(0)

# Close the window
cv2.destroyAllWindows()
