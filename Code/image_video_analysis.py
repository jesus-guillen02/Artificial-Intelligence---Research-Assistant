import cv2
import numpy as np
from sklearn import svm
from sklearn.decomposition import PCA
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from skimage.feature import hog

# Function to load the image specified by the user
def load_image(image_path):
    image = cv2.imread(image_path)
    return image

# Function to convert an image to grayscale
def convert_to_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Function to resize an image
def resize_image(image, width, height):
    return cv2.resize(image, (width, height))

# Function to extract HOG (Histogram of Oriented Gradients) features
def extract_hog_features(image):
    resized_image = resize_image(image, 64, 128)  # Resizing for HOG feature extraction
    features, _ = hog(resized_image, orientations=9, pixels_per_cell=(8, 8),
                      cells_per_block=(2, 2), visualize=True, multichannel=True)
    return features

# Dummy classifier function (you should train this classifier with your own data)
def classify_image(image):
    features = extract_hog_features(image)
    model = make_pipeline(StandardScaler(), PCA(n_components=50), svm.SVC())
    # Dummy prediction as the model is not trained
    prediction = model.predict([features])
    return prediction

# Function to load a video from the user specified path
def load_video(video_path):
    cap = cv2.VideoCapture(video_path)
    return cap

# Function to process video frames from the given video
def process_video_frames(video_capture):
    while video_capture.isOpened():
        ret, frame = video_capture.read()
        if not ret:
            break

        gray_frame = convert_to_grayscale(frame)
        cv2.imshow('Frame', gray_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()

def run():
    choice = input("Choose 'image' or 'video' for analysis: ")

    if choice == 'image':
        image_path = input("Enter the path of the image: ")
        image = load_image(image_path)
        gray_image = convert_to_grayscale(image)

        prediction = classify_image(gray_image)
        print(f"Prediction: {prediction}")

        cv2.imshow('Image', gray_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    elif choice == 'video':
        video_path = input("Enter the path of the video: ")
        video_capture = load_video(video_path)
        process_video_frames(video_capture)

if __name__ == "__main__":
    run()
