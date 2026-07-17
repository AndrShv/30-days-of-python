import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from shared import parse_kv_record  # noqa: E402

raw_log = "  ID:1042_Model:ResNet50_Accuracy:0.9482_Epochs:50  "
striped_log = raw_log.strip()

log_parts = striped_log.split("_")
print(log_parts)


id, model, accuracy, epochs = log_parts
print(f"ID: {id}, Model: {model}, Accuracy: {accuracy}, Epochs: {epochs}")


record = parse_kv_record(raw_log, "_")
obtained_model = record["Model"]
accuracy_value = float(record["Accuracy"])
obtained_epochs = record["Epochs"]


percentage_accuracy = round(accuracy_value * 100, 2)

print(f"Модель {obtained_model} показала точность {percentage_accuracy}%")
