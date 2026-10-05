from ultralytics import YOLO
import cv2
import sys
import pyfiglet

# COCO Animal Class IDs + Names
ANIMAL_IDS = [14,15,16,17,18,19,20,21,22,23]
ANIMAL_NAMES = {
    14: "bird", 15: "cat", 16: "dog", 17: "horse", 18: "sheep",
    19: "cow", 20: "elephant", 21: "bear", 22: "zebra", 23: "giraffe"
}

def main():
    banner = pyfiglet.figlet_format("FARM GUARDIAN", font="standard")  
    print(banner)
    
    print("Animal Detection using YOLOv8 and OpenCV.\nThis program uses a pretrained YOLOv8 model to detect animals from the COCO dataset in real-time using your webcam.\nA live video feed window will open showing bounding boxes and labels for each detected animal.\nPress 'q' to quit the program.\n")
    print("This program can detect the following animals:")
    for id_ in ANIMAL_IDS:
        print(f"- {ANIMAL_NAMES[id_]}")
    print("\nStarting webcam feed...\n")

    # Load YOLOv8 model with verbose=False to suppress terminal output
    model = YOLO("yolov8n.pt")
    model.overrides['verbose'] = False  


    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("ERROR: Could not open webcam. Try changing index (0->1).")
        sys.exit(1)


    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Failed to read frame from camera.")
                break


            results = model(frame, conf=0.25)


            for r in results:
                for box in r.boxes:
                    cls_id = int(box.cls[0])
                    if cls_id not in ANIMAL_IDS:
                        continue

                    x1, y1, x2, y2 = box.xyxy[0].tolist()
                    conf = float(box.conf[0])
                    label = f"{ANIMAL_NAMES[cls_id]} {conf:.2f}"

                    cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)),
                                  (0, 255, 0), 2)
                    cv2.putText(frame, label, (int(x1), int(y1) - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

            cv2.imshow("Animal Detection - Live Feed", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    except KeyboardInterrupt:
        print("\nStopping the animal detcction program. Exiting...")

    finally:
        cap.release()
        cv2.destroyAllWindows()
        print("Camera and windows closed. Program ended.")

if __name__ == "__main__":
    main()

