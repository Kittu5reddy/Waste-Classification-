# Waste Classification using CNN

This project utilizes a Convolutional Neural Network (CNN) to classify waste into four categories: **Biodegradable, Non-Biodegradable, Trash, or Hazardous**. The model is designed to assist in waste management by automating the classification process, making it easier to sort and recycle waste effectively.

## Dataset
# Download the dataset from Kaggle
!kaggle datasets download -d alistairking/recyclable-and-household-waste-classification


## Key Features

- **Model Loading**: The model is loaded using a cached function to improve performance.
- **Image Upload**: Users can upload images of waste through the Streamlit interface.
- **Prediction**: The uploaded image is processed and classified into one of the four categories using the trained CNN model.
- **User Feedback**: The app provides visual feedback by displaying the uploaded image and the predicted class.

## Resources and Tools Used

- **Dataset**: [Recyclable and Household Waste Classification](https://www.kaggle.com/datasets/alistairking/recyclable-and-household-waste-classification)
- **Framework**: PyTorch for building and training the CNN model.
- **Web App**: Streamlit for creating the user interface.
- **Image Processing**: PIL (Python Imaging Library) for handling image uploads and preprocessing.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/Waste-Classification.git
    cd Waste-Classification
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

3. Download the dataset from Kaggle:
    ```sh
    kaggle datasets download -d alistairking/recyclable-and-household-waste-classification
    ```

4. Extract the dataset and place it in the appropriate directory.

## Usage

1. Run the Streamlit app:
    ```sh
    streamlit run app.py
    ```

2. Upload an image of waste through the Streamlit interface.

3. The app will display the uploaded image and the predicted class.

## File Structure

- [app.py](http://_vscodecontentref_/0): Contains the Streamlit app code.
- [main.py](http://_vscodecontentref_/1): Contains the model loading, image preprocessing, and prediction functions.
- [model](http://_vscodecontentref_/2): Directory to store the trained model file (`40.pth`).
- [README.md](http://_vscodecontentref_/3): Project documentation.

## Model Training

The model is trained using a VGG16 architecture with the final layer modified to output four classes. The training script and dataset preprocessing steps are not included in this repository but can be adapted based on the provided dataset.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.