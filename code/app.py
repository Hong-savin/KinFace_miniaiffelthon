import streamlit as st
from preprocessing import preprocess_images
from similarity_calculation import calculate_relationship_similarity
from visualization import plot_similarity_scores
from PIL import Image
import numpy as np
import cv2
def display_uploaded_images_in_row(uploaded_files, resize_dim=(224, 224)):
    """
    Streamlit UploadedFile 객체로 받은 이미지를 리사이즈하고 가로로 출력합니다.
    
    Args:
        uploaded_files (dict): {"role": UploadedFile 객체} 형태의 딕셔너리
        resize_dim (tuple): 리사이즈할 크기 (width, height)

    Returns:
        None: 이미지를 가로로 결합한 결과를 Streamlit 화면에 출력합니다.
    """
    images = []

    for role, file in uploaded_files.items():
        if file is not None:
            # Streamlit UploadedFile 객체를 PIL 이미지로 읽기
            image = Image.open(file)
            
            # 이미지를 OpenCV 형식으로 변환
            image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
            
            # 리사이즈
            resized_img = cv2.resize(image, resize_dim)
            
            # BGR -> RGB로 변환 (Matplotlib 출력용)
            rgb_img = cv2.cvtColor(resized_img, cv2.COLOR_BGR2RGB)
            images.append(rgb_img)

    if not images:
        st.write("No valid images to display.")
        return

    # 가로로 이어붙임
    combined_image = np.hstack(images)

    # Streamlit에서 이미지 출력
    st.image(combined_image, caption="Resized Images Combined in a Row", use_column_width=True)


# Streamlit UI
st.title("Family Similarity Calculator")

uploaded_files = {
    "child": st.file_uploader("Upload Child Photo"),
    "father": st.file_uploader("Upload Father Photo"),
    "mother": st.file_uploader("Upload Mother Photo"),
    "sibling": st.file_uploader("Upload Sibling Photo (Optional)")
}

if st.button("Calculate Similarity"):
    if not uploaded_files["child"] or not uploaded_files["father"] or not uploaded_files["mother"]:
        st.error("Please upload Child, Father, and Mother photos.")
    else:
        try:
            # Preprocess images
            processed_images = preprocess_images(uploaded_files)
            display_uploaded_images_in_row(uploaded_files)
            # Calculate similarities
            final_scores, similarity_details = calculate_relationship_similarity(processed_images)
            
            # Display results
            st.header("Final Scores")
            for relation, score in final_scores.items():
                st.write(f"{relation}: {score:.2f}")

            st.header("Similarity Breakdown")
            plot_similarity_scores(similarity_details, processed_images.keys())
        except Exception as e:
            st.error(f"Error calculating similarities: {e}")
