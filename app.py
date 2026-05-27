import streamlit as st
from ultralytics import YOLO
from PIL import Image
import tempfile
import cv2

# Load trained model
model = YOLO("runs/detect/train/weights/best.pt")

st.title("Garbage Detection using YOLO")

# Sidebar option
option = st.sidebar.selectbox(
    "Choose Detection Mode",
    ["Image Upload", "Live Camera"]
)

# ---------------- IMAGE UPLOAD ---------------- #
if option == "Image Upload":

    uploaded_file = st.file_uploader(
        "Upload an Image",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_file is not None:

        # Display uploaded image
        image = Image.open(uploaded_file)

        st.image(
            image,
            caption="Uploaded Image",
            use_container_width=True
        )

        uploaded_file.seek(0)

        # Save temp image
        with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_file:
            temp_file.write(uploaded_file.read())
            temp_path = temp_file.name

        # Run detection on GPU
        results = model(temp_path, device=0)

        # Draw detections
        output_image = results[0].plot()

        st.subheader("Detection Result")

        st.image(
            output_image,
            use_container_width=True
        )

        # Detection summary
        boxes = results[0].boxes

        count = len(boxes)

        st.subheader("Detection Summary")

        st.write(f"Total Garbage Objects Detected: {count}")

        # Density
        if count <= 2:
            density = "Low"

        elif count <= 5:
            density = "Medium"

        else:
            density = "High"

        st.write(f"Garbage Density: {density}")

        st.subheader("Detected Objects")

        for box in boxes:

            class_id = int(box.cls[0])

            confidence = float(box.conf[0])

            label = model.names[class_id]

            st.write(
                f"{label} - Confidence: {confidence:.2f}"
            )

# ---------------- LIVE CAMERA ---------------- #
elif option == "Live Camera":

    st.subheader("Live Webcam Detection")

    run = st.checkbox("Start Camera")

    FRAME_WINDOW = st.image([])

    camera = cv2.VideoCapture(0)

    while run:

        success, frame = camera.read()

        if not success:
            st.error("Failed to access webcam")
            break

        # YOLO prediction using GPU
        results = model(frame, device=0)

        # Draw detections
        annotated_frame = results[0].plot()

        # Convert BGR to RGB
        annotated_frame = cv2.cvtColor(
            annotated_frame,
            cv2.COLOR_BGR2RGB
        )

        FRAME_WINDOW.image(
            annotated_frame,
            channels="RGB"
        )

    camera.release()