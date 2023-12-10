# ImageClassification
## Team name:** "What could go wrong?"

## Team members: Szakszon Mátyás - DXR 372, ~~Pete Dávid - GVJ529, Hajszter Donát - QOZ2I7~~

Pete Dávid és Hajszer Donát neve, azért van áthúzva, mert november 16-án úgy döntöttek, hogy abbahagyják ezt az Msc képzést, úgyhogy egyedül Szakszon Mátyás készíti a feladatot.

## Project description:

The goal of this project is to compare and demonstrate the advantages of using pretrained neural networks vs randomly initialized ones for image classification. Build an image classification pipeline for a smaller dataset (e.g. CIFAR-10), and train both a randomly initialized and an ImageNet-pretrained network (e.g. ResNet) for the task. Compare their performance.

## Functions of the files in the repository:
- **build/Dockerfile** : Describes the process of the containerization of the solution.
- **build/requirements.txt** : Contains the installed requirements of the project with fixed version numbers.
- **build/resnet.ipynb** : Contains the implementation and evaluation of a `pretrained` and a `not pretrained` resnet model. It also contains a small `Gradio` implementation that shows the difference between the two model. We can upload any `Image` we would like to test the two different models with.

## Related works: 
- [CIFAR Dataset](https://www.cs.toronto.edu/~kriz/cifar.html)
- [Resnet](https://pytorch.org/hub/pytorch_vision_resnet/)
- [Gradio](https://www.gradio.app/docs/interface)

### Interactive UI usage

I implemented an interactive UI with Gradio that allow us to upload any `Image` we would like and we can test the models with it. There are two `input` and `output` sections first one for the pretrained and the second one is for the not pretrained. 
If we upload any image in the input fields and submit it will auto select that image for the other input as well just to make it a little easier to test the two models with the same input. The ideal solution would be to use only one input field and two output field but it did not seem possible with Gradio but it is still pretty good to test the models.
 
**How to run it:** ```docker compose up -d```
