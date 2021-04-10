
  

# MIDAS@IIITD RA Task 2 [CNN]

  

 
## Augmentation

  

- Using `imgaug` I have augmented the data with a `augmentation.py`. This script takes in the path of the data and produces the required augmented images thereby increasing the data by two-fold.

  

- I have used this augmentation script for training the first task i.e. classification of 62 classes (A-Z, a-z and 0-9).

  

- Usage of the augmentation script :

  

`images = create_images(repetitions = 1, path = 'Downloads/tt_data/lightweight-human-pose-estimation.pytorch/front/')`

  

`augmented_images = augment(images, save=True, path = 'Downloads/tt_data/augmented_forehand', save_original=True)`

  

Where `save_original` : saves the original images along with the augmented images.

  
  

-  `midas.ipynb` has the network architecture and the model checkpoints are saved [here]().

  

- The MNIST data consists of the numbers in white (255) pixels, the data provided has numbers where the numbers are of black (0 pixel value) pixels.

  

- I have also inverted the colors and applied threshold to the augmented images to produce white numbers on black backgrounds, this would ideally improve the performance of the classifier.

  

- All data to train is available [here](https://drive.google.com/drive/folders/10fA0NKez00UhPfsMcVem8BxPbWhJmyzh?usp=sharing).

  

  

## Explanation of the different notebooks used :

  

- The `0-9_training.ipynb` notebook contains the network that I had written from scratch (similar to the one in `midas.ipynb`.

  

- This network is trained for 50 epochs (only 25 is displayed as I trained it in 2 batches).

  

- The model model trained for 50 epochs is found [here](https://drive.google.com/file/d/1K_1rL61DgWerKz-zdg8YGtfguVnh5T0G/view?usp=sharing)

  

-  `part_2.ipynb` notebook contains evaluation of the above trained model with the MNIST data-set, the result was found to be pretty decent as the accuracy was about 56% with an f1 score of 55. Class '6' predicting the best with the f1 score being 0.75. This model is then trained again on the MNIST test train split to achieve a `val_loss` of `0.028`. The MNIST data was trained on scratch random initialized weights and then the achieved accuracy 10% with an f1 score of 0.1. This model is then trained from scratch on the MNIST test train splits to achieve an accuracy of 0.99 with min `val_loss` of `0.03` with a lower convergence time when compared to training on the model which had weights from when it was trained with the 0-9 images provided.
- `part_3.ipynb` goes about the third part of this task where the data-set provided is loaded and trained from scratch as well as trained on the same model from part 1 (62 classes). The results are quite dull because of the jumbled data that is produced although the model trained from scratch did a good job at wrongly predicting 9995/10000 data points in the MNIST test data.
- The results that I've concluded are all noted down in the form of text before each cell in the notebook.


