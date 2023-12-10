# ImageClassification
## Team name: "What could go wrong?"

## Team members: Szakszon Mátyás - DXR 372, ~~Pete Dávid - GVJ529, Hajszter Donát - QOZ2I7~~

Pete Dávid és Hajszer Donát neve, azért van áthúzva, mert november 16-án úgy döntöttek, hogy abbahagyják az Msc képzést, úgyhogy egyedül Szakszon Mátyás készítette a feladatot.

## Project description:

The goal of this project is to compare and demonstrate the advantages of using pretrained neural networks vs randomly initialized ones for image classification. Build an image classification pipeline for a smaller dataset (e.g. CIFAR-10), and train both a randomly initialized and an ImageNet-pretrained network (e.g. ResNet) for the task. Compare their performance.

## Functions of the files in the repository:
- **build/Dockerfile** : Describes the process of the containerization of the solution.
- **build/requirements.txt** : Contains the installed requirements of the project with fixed version numbers.
- **build/resnet.ipynb** : Contains the implementation and evaluation of a `PreTrained` and a `Mot PreTrained` resnet model. It also contains a small `Gradio` implementation that shows the difference between the two model. We can upload any `Image` we would like to test the two different models with.

## Related works: 
- [CIFAR10 Dataset](https://www.cs.toronto.edu/~kriz/cifar.html)
- [Resnet](https://pytorch.org/hub/pytorch_vision_resnet/)
- [Gradio](https://www.gradio.app/docs/interface)

### Interactive UI usage

I implemented an interactive UI with Gradio that allow us to upload any `Image` we would like and we can test the models with it. There are two `input` and `output` sections first one for the pretrained and the second one is for the not pretrained. 
If we upload any image in the input fields and submit it will auto select that image for the other input as well just to make it a little easier to test the two models with the same input. The ideal solution would be to use only one input field and two output field but it did not seem possible with Gradio but it is still pretty good to test the models.

After we uploaded and sumbitted the image we are able to see the results in the output field. It shows the model's probabilities for the 10 different classes (sum 100%).
![image](https://github.com/Matyiko/ImageClassification/assets/73035410/ecfcc41e-78e4-47a4-87d2-317d063cda4c)


# Methods of training

The dataset contained 224x224 images, and they were normalized into..... TODO
I used a train-validation split with 90-10 ratio.
The dataeset contains 10 different classes that we can classify using our models.
We split the cases instead of the images, to avoid data leakage between the splits,
as neighbouring images are very similar to each other.

# Results

## Metrics on test set

| Model                | Epochs | Test Loss  | Test Accuracy |
|----------------------|--------|------------|---------------|
| PreTrained           | 10     | 0.2228     | 0.9369        |
| Not PreTrained       | 10     | 0.2316     | 0.9405        | 

It's pretty surprising but the `Not PreTrained` model is basicly as good as the `PreTrained` version of it.
On basic pictures from the internet both of the models give the same results and they are very accurate however i tested the models with selfmade pictures and there i could find very different guesses from the models which is pretty intresting.
This is my favourite test:
![image](https://github.com/Matyiko/ImageClassification/assets/73035410/1bf3a483-ebf0-4fa4-8fa2-be39b75804b0)
As we can see it's the `Not PreTrained` model that guessed here correctly.

 
**How to run it:** ```docker compose up -d```
