import fiftyone as fo
import fiftyone.zoo as foz

dataset = foz.load_zoo_dataset(
              "open-images-v7",
              split="validation",
              label_types=["classifications"],
              classes=["Ball", "Cat", "Dog", "Tree", "Dolphin", "Doll", "Bird", "Beer", "Man", "Pasta", "Bicycle", "Bottle", "Clock", "Flower", "Boat"],
              max_samples=10000,
          )

print(dataset)