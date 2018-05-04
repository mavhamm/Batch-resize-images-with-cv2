import cv2  # image processing (OpenCV)
import glob  # finds paths
import os  # creates new folder

# creates list of images with .jpg extension
all_images = glob.glob("*.jpg")

# creates folder 'resized' if it doesn't exist yet
new_directory = "resized"
if not os.path.exists(new_directory):
    os.makedirs(new_directory)

for i in all_images:
    # reads all_images path
    img = cv2.imread(i, 1)

    # resizes to 25%
    resized = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)

    # # checks resized images for 0.4s then closes
    # cv2.imshow("Cheking", resized)
    # cv2.waitKey(400)
    # cv2.destroyAllWindows()

    # writes resized files to the new directory
    cv2.imwrite(f"{new_directory}/{i}_resized", resized)
