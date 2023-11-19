import fiftyone as fo
import fiftyone.zoo as foz
import matplotlib.pyplot as plt

dataset = foz.load_zoo_dataset(
              "open-images-v7",
              split="validation",
              label_types=["classifications"],
              classes=["Ball", "Cat", "Dog", "Tree", "Dolphin", "Doll", "Bird", "Beer", "Man", "Pasta", "Bicycle", "Bottle", "Clock", "Flower", "Boat"],
              max_samples=1000,
          )

# Specify the path where you want to save the CSV file
csv_export_path = "dataset_export.csv"

# Export the dataset to CSV
dataset.export(
    export_path=csv_export_path,
    export_type="csv",
    label_field="classifications",  # Specify the field containing the labels
    overwrite=True,  # Set to True if you want to overwrite an existing file
)