# ImageClassification
## Team name: "What could go wrong?"

## Team members: Szakszon Mátyás - DXR372, ~~Pete Dávid - GVJ529, Hajszter Donát - QOZ2I7~~

Pete Dávid és Hajszer Donát neve, azért van áthúzva, mert november 16-án úgy döntöttek, hogy abbahagyják az Msc képzést, úgyhogy egyedül Szakszon Mátyás készítette a feladatot.

## Project description:

The goal of this project is to compare and demonstrate the advantages of using pretrained neural networks vs randomly initialized ones for image classification. Build an image classification pipeline for a smaller dataset (e.g. CIFAR-10), and train both a randomly initialized and an ImageNet-pretrained network (e.g. ResNet) for the task. Compare their performance.

## Functions of the files in the repository:
- **build/Dockerfile** : Describes the process of the containerization of the solution.
- **build/requirements.txt** : Contains the installed requirements of the project with fixed version numbers.
- **build/resnet.ipynb** : Contains the implementation and evaluation of a `PreTrained` and a `Not PreTrained` resnet model. It also contains a small `Gradio` implementation that shows the difference between the two model. We can upload any `Image` we would like to test the two different models with.

 
**How to run it:** 
1. Navigate from the Project's root directory to the build directory.
2. Run this command: ```docker compose up -d```

## Introduction

For the task i choosed the [Resnet-18](https://pytorch.org/hub/pytorch_vision_resnet/) model because my task is to test the difference between a pretraiend and not pretrained model. The Resnet-18 model is perfect for that purpose because you can load a pretrained version of the network trained on more than a million images from the ImageNet database or just use the not pretrained version and train it myself.

## Dataset
I choose the [CIFAR10 Dataset](https://www.cs.toronto.edu/~kriz/cifar.html) which  consists of 60000 32x32 colour images in 10 classes, with 6000 images per class. There are 50000 training images and 10000 test images.
The classes are completely mutually exclusive.

The classes: `plane, car, bird, cat, deer, dog, frog, horse, ship, truck`

Few examples of the dataset:

| ![image](https://github.com/Matyiko/ImageClassification/assets/73035410/b262a315-b6a4-4081-8c8e-007c7ac2d39f)| ![image](https://github.com/Matyiko/ImageClassification/assets/73035410/96775d16-74a5-4ec7-866f-3099ab19b23f) | ![image](https://github.com/Matyiko/ImageClassification/assets/73035410/27d96882-f9da-4631-93c8-da2508537cbe)  | ![image](https://github.com/Matyiko/ImageClassification/assets/73035410/24809a72-e0dc-4c83-a86f-93e53d8b23ea) | ![image](https://github.com/Matyiko/ImageClassification/assets/73035410/4bf5eecb-7a98-4035-b9d8-6aba828dd1b4)
|----------------------|--------|------------|---------------|-----|
| Cat|Ship|Plane|Frog|Frog

### Interactive UI usage

I implemented an interactive UI with [Gradio](https://www.gradio.app/docs/interface) that allow us to upload any `Image` we would like and we can test the models with it. There are two `input` and `output` sections first one for the pretrained and the second one is for the not pretrained. 
If we upload any image in the input fields and submit it will auto select that image for the other input as well just to make it a little easier to test the two models with the same input. The ideal solution would be to use only one input field and two output field but it did not seem possible with Gradio but it is still pretty good to test the models.

After we uploaded and sumbitted the image we are able to see the results in the output field. It shows the model's probabilities for the 10 different classes (sum 100%).

![image](https://github.com/Matyiko/ImageClassification/assets/73035410/ecfcc41e-78e4-47a4-87d2-317d063cda4c)

# Architecture
The ResNet is a fully convolutional neural network, which ends in a fully connected layer to produce classification probabilities.
It  uses convolutional layers with strides of 2 to reduce the size of the feature maps, internally it reduces the image size from 224x224 to 7x7.
It uses batch normalization and ReLU activation functions.

It is a type of architecture that uses the same convolutional layers as a standard neural network,
but can be trained to be much deeper than previous attempts.
The ResNet's "secret ingredient" is the residual block.
We can imagine a neural network as a function,
that iteratively transforms the input into the output.
In each iteration we take the output of the previous layer,
and apply a transformation to it,
but in many cases we should only apply a small transformation to the output of the previous layer,
and the rest of the transformation should be the identity function.
In ResNets, skip connections are implemented just as described above:
the output of the previous layer is ADDED to the output of the current layer,
instead of concatenating them together.
That is why this is called residual connection, as residual means 'left over'.

![image](https://github.com/Matyiko/ImageClassification/assets/73035410/979b7672-8376-4348-a0c3-f346e25348cd)

# Methods of training

The dataset was resized to 224x224, and the images were normalized. Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])the mean and standard deviation values used here. The values [0.485, 0.456, 0.406] represent the mean values for the red, green, and blue channels, respectively. The values [0.229, 0.224, 0.225] represent the standard deviation for the red, green, and blue channels.

The reason for the images to be resized to 224x224 is that the resnet-18 model was designed to use 224x224 images it's architecture is built like that. 
The problem with the 32x32 images is that the resnet-18 model downscales the images atleast five times which results in 1x1 size of images on 512 channels before it reaches the convolutional layers. We can assume that it was not designed to deal with small images without resizing them even if it looks weird. If we used any image that is smaller than that it probably end up in an exception.

I used a train-validation split with 90-10 ratio. The test set is completely separate and is not involved in the training/validation split. It is created using the CIFAR-10 test dataset, which is distinct from the training dataset.
The dataset contains 10 different classes that we can classify using our models.

There is a visual representation of the Training of the two models.
The Purple is the PreTrained and the yellow is the Not PreTrained.

![image](https://github.com/Matyiko/ImageClassification/assets/73035410/2e2ffc76-9fb2-4e9f-a282-ed909486de19)
![image](https://github.com/Matyiko/ImageClassification/assets/73035410/1796acd8-80f5-4561-b0f6-efd123e9f5b8)
![image](https://github.com/Matyiko/ImageClassification/assets/73035410/71cf492f-57fc-4bbc-9470-b7fb43b6bd98)
![image](https://github.com/Matyiko/ImageClassification/assets/73035410/2f9e55b2-47fc-44f2-bf7f-5cddead194dd)

Trainging on the 32x32 images without upscaling.

![image](https://github.com/Matyiko/ImageClassification/assets/73035410/36d51352-19e0-4271-a3eb-ed518269ea15)
![image](https://github.com/Matyiko/ImageClassification/assets/73035410/1b620b0f-b94e-4f97-a5df-679e04aec927)

I trained on my own PC with a RTX 3070 GPU.
The training takes about 5-15 minits for each model so the whole training is about 20 minits.

## Results

Results with the upscaling of the images to 224x224:

| Model                | Epochs | Test Loss  | Test Accuracy |
|----------------------|--------|------------|---------------|
| PreTrained           | 10     | 0.2228     | 0.9369        |
| Not PreTrained       | 10     | 0.2316     | 0.9405        | 

Results with the origimal 32x32 images:

| Model                | Epochs | Test Loss  | Test Accuracy |
|----------------------|--------|------------|---------------|
| PreTrained           | 10     | 0.7594     | 0.7978        |
| Not PreTrained       | 10     | 0.8406     | 0.7980        | 

It's pretty surprising but the `Not PreTrained` model is basicly as good as the `PreTrained` version of it.
On basic pictures from the internet both of the models give the same results and they are very accurate however i tested the models with selfmade pictures and there i could find very different guesses from the models which is pretty intresting.

As we can see in the picture above that the PreTrained model is way more self-confident because it usually guesses the first class with a higher value than the Not Pretrained. Which is instresting because it's not clear if it's a good or bad property of the model.

My favourite test:

![image](https://github.com/Matyiko/ImageClassification/assets/73035410/1bf3a483-ebf0-4fa4-8fa2-be39b75804b0)

As we can see it's the `Not PreTrained` model that guessed this one correctly.

## Conlusions

The final conlusions is that in numbers there is almost no difference between the two models but they give very different percentages compare to that.

I most enjoyed the project is visualizing the results with Gradio it was pretty intresting.  However i would have preffered to do it with an actual team so we can try out more intresting and cool stuff together.

## Related works
[Learning Multiple Layers of Features from Tiny Images](https://www.cs.toronto.edu/~kriz/learning-features-2009-TR.pdf), Alex Krizhevsky, 2009

[Resnet Documentation](https://arxiv.org/abs/1512.03385)
