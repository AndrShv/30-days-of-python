raw_log = "  ID:1042_Model:ResNet50_Accuracy:0.9482_Epochs:50  "
striped_log = raw_log.strip()

log_parts = striped_log.split("_")
print(log_parts)


id, model, accuracy, epochs = log_parts
print(f"ID: {id}, Model: {model}, Accuracy: {accuracy}, Epochs: {epochs}")


data_set = {"ID": id, "Model": model, "Accuracy": accuracy, "Epochs": epochs}
obtained_model = str(data_set.get("Model").split(":")[1])
accuracy_value = float(data_set.get("Accuracy").split(":")[1])
obtained_epochs = str(data_set.get("Epochs").split(":")[1])


percentage_accuracy = round(accuracy_value * 100, 2)

print(f"Модель {obtained_model} показала точность {percentage_accuracy}%")
