# MIDAS@IIITD RA Task 2 [CNN]

## Augmentation
- Using `imgaug` I have augmented the data with a `augmentation.py`. This script takes in the path of the data and produces the required augmented images thereby increasing the data by two-fold.
- I have used this augmentation script for training the first task i.e. classification of 62 classes (A-Z, a-z and 0-9).
- `midas.ipynb` has the network architecture and the model checkpoints are saved [here]().
- The MNIST data consists of the numbers in white (255) pixels, the data provided has numbers where the numbers are of black (0 pixel value) pixels.
- I have also inverted the colors and applied threshold to the augmented images to produce white numbers on black backgrounds, this would ideally improve the performance of the classifier.
- All data to train is available [here](https://drive.google.com/drive/folders/10fA0NKez00UhPfsMcVem8BxPbWhJmyzh?usp=sharing).

## Explanation of the different notebooks used :
-	The `0-9_training.ipynb` notebook contains the network that I had written from scratch (similar to the one in `midas.ipynb`. 
-	This network is trained for 75 epochs (only 25 is displayed as I trained it in 3 batches).
-	The model model trained for 75 epochs is found [here](https://drive.google.com/file/d/1-4CEtwla2H6YOKTFqsYWgA_9Ic3zgynE/view?usp=sharing)
-	`MNIST_evaluation.ipynb`
