import os
from PIL import Image, ImageChops

def is_image_edited(image_path, error_threshold=100):
    try:
        with Image.open(image_path) as img:
            # Create a copy of the image to compare with
            duplicate = ImageChops.duplicate(img)

            # Save the duplicate image with a lossy format (JPEG) and then load it again
            duplicate.save("duplicate.jpg", "JPEG")
            duplicate = Image.open("duplicate.jpg")

            # Compare the original and duplicate images
            diff = ImageChops.difference(img, duplicate)
            diff.show()  # You can remove this line if you don't need to visualize the difference

            # Calculate the error level
            extrema = diff.getextrema()
            max_diff = max([ex[1] for ex in extrema])

            # Adjust the error threshold to fit your needs
            if max_diff > error_threshold:
                return True

        return False
    except Exception as e:
        print(f"Error: {e}")
        return None

def main():
    print("Image Edit Detection")
    image_path = input("Enter the path to the image you want to check: ")

    if os.path.exists(image_path):
        try:
            edited = is_image_edited(image_path)
            if edited is not None:
                if edited:
                    print("The image appears to be edited.")
                else:
                    print("The image does not appear to be edited.")
        except Exception as e:
            print(f"Failed to check the image: {e}")
    else:
        print("Error: The specified image path does not exist.")

if __name__ == "__main__":
    main()
