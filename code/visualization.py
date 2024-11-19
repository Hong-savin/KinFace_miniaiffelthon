import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
import cv2
def plot_similarity_scores(similarity_details, roles):
    categories = list(similarity_details[next(iter(similarity_details))].keys())
    x = np.arange(len(categories))
    width = 0.25

    fig, ax = plt.subplots(figsize=(14, 8))
    for i, role in enumerate(roles):
        if role not in similarity_details:
            continue
        scores = [similarity_details[role][cat] * 100 for cat in categories]
        ax.bar(x + i * width, scores, width, label=f"Child-{role.capitalize()}")

    ax.set_xlabel("Metrics")
    ax.set_ylabel("Similarity (%)")
    ax.set_title("Family Similarity by Metrics")
    ax.set_xticks(x + width / 2)
    ax.set_xticklabels(categories, rotation=45)
    ax.legend()
    plt.tight_layout()
    st.pyplot(fig)



def display_images_in_row(image_paths, resize_dim=(224, 224)):
    """
    여러 이미지를 가로로 출력하기 위해 리사이즈 후 결합합니다.
    
    Args:
        image_paths (list): 이미지 경로 리스트
        resize_dim (tuple): 리사이즈할 크기 (width, height)

    Returns:
        None: 가로로 이어붙인 이미지를 Streamlit으로 출력합니다.
    """
    images = []

    for path in image_paths:
        # 이미지 로드
        img = cv2.imread(path)
        if img is None:
            print(f"Error: Unable to load image from {path}")
            continue

        # 리사이즈
        resized_img = cv2.resize(img, resize_dim)

        # BGR -> RGB로 변환 (Matplotlib 출력용)
        rgb_img = cv2.cvtColor(resized_img, cv2.COLOR_BGR2RGB)
        images.append(rgb_img)

    if not images:
        print("No valid images to display.")
        return

    # 가로로 이어붙임
    combined_image = np.hstack(images)

    # Streamlit 출력
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.imshow(combined_image)
    ax.axis("off")
    ax.set_title("Resized Images Combined in a Row")
    st.pyplot(fig)