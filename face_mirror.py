
import cv2
import sys


def main():
    camera = cv2.VideoCapture(0)

    if not camera.isOpened():
        print("ERROR: Could not open webcam.")
        print("Check camera permissions or try camera index 1.")
        camera.release()
        return

    try:
        # Load OpenCV's built-in Haar cascade face detector.
        cascade_path = (
            cv2.data.haarcascades
            + "haarcascade_frontalface_default.xml"
        )

        detector = cv2.CascadeClassifier(cascade_path)

        if detector.empty():
            print("ERROR: Could not load face detector.")
            print("Cascade path:", cascade_path)
            return

        print("Face Mirror started.")
        print("Press Q to quit.")

        while True:
            ok, frame = camera.read()

            if not ok or frame is None:
                print("ERROR: Could not read webcam frame.")
                break

            # Mirror the camera image.
            frame = cv2.flip(frame, 1)

            # Convert to grayscale for face detection.
            gray = cv2.cvtColor(
                frame,
                cv2.COLOR_BGR2GRAY
            )

            # Detect faces.
            faces = detector.detectMultiScale(
                gray,
                scaleFactor=1.15,
                minNeighbors=5,
                minSize=(60, 60)
            )

            # Draw a rectangle around every detected face.
            for (x, y, w, h) in faces:
                cv2.rectangle(
                    frame,
                    (x, y),
                    (x + w, y + h),
                    (0, 220, 255),
                    3
                )

                # Keep the label inside the image.
                label_y = max(y - 10, 25)

                cv2.putText(
                    frame,
                    "Face detected",
                    (x, label_y),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (0, 220, 255),
                    2
                )

            # Display the number of detected faces.
            cv2.putText(
                frame,
                f"Faces: {len(faces)} | Q to quit",
                (12, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.75,
                (40, 255, 40),
                2
            )

            cv2.imshow(
                "Face Mirror - Local Face Detection",
                frame
            )

            # Press Q to close the window.
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

    except cv2.error as error:
        print("OpenCV error:", error)

    finally:
        camera.release()
        cv2.destroyAllWindows()
        print("Face Mirror closed.")


if __name__ == "__main__":
    main()
