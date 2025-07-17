import cv2
import os

# Map keys to folder names and class names
key_to_label = {'0': '0', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6'}
label_to_name = {'0': 'A', '1': 'B', '2': 'L', '3': 'D', '4': 'E', '5': 'F', '6': 'C'}

DATA_DIR = 'data'

# Ensure directories exist
for label in key_to_label.values():
    dir_path = os.path.join(DATA_DIR, label)
    os.makedirs(dir_path, exist_ok=True)

cap = cv2.VideoCapture(0)

print("Press '0' for A, '1' for B, '2' for L, '3' for D, '4' for E, '5' for F, '6' for C. Press 'q' to quit.")

counters = {label: len(os.listdir(os.path.join(DATA_DIR, label))) for label in key_to_label.values()}

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    # Show instructions on the frame
    for idx, (key, label) in enumerate(label_to_name.items()):
        cv2.putText(frame, f"Press {key} for {label}", (10, 30 + idx*30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
    cv2.putText(frame, "Press 'q' to quit", (10, 270), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

    cv2.imshow('Collect Images', frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break
    elif chr(key) in key_to_label:
        label = key_to_label[chr(key)]
        save_path = os.path.join(DATA_DIR, label, f"{counters[label]}.jpg")
        cv2.imwrite(save_path, frame)
        print(f"Saved {save_path}")
        counters[label] += 1

cap.release()
cv2.destroyAllWindows() 