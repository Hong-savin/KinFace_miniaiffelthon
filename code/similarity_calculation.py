import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from skimage.metrics import structural_similarity as ssim
import dlib
import cv2
# Load dlib predictor
predictor = dlib.shape_predictor("file/shape_predictor_68_face_landmarks.dat")
detector = dlib.get_frontal_face_detector()

weights = {
    "feature_distribution": 0.2,
    "eye_color": 0.15,
    "nose_shape": 0.1,
    "mouth_shape": 0.2,
    "eye_position_ratio": 0.1,
    "nose_position_ratio": 0.1,
    "mouth_position_ratio": 0.15
}

def calculate_relationship_similarity(images):
    similarities = {}
    for role in ["father", "mother", "sibling"]:
        if role not in images:
            continue
        similarities[role] = calculate_similarities(images["child"], images[role])

    final_scores = {
        f"Child-{role.capitalize()}": sum(similarities[role][key] * weights[key] for key in weights)
        for role in similarities
    }
    return final_scores, similarities
# Cosine Similarity
def calculate_cosine_similarity(embedding1, embedding2):
    embedding1 = np.array(embedding1).reshape(1, -1)
    embedding2 = np.array(embedding2).reshape(1, -1)
    return cosine_similarity(embedding1, embedding2)[0][0]

# RGB Similarity (for eye color)
def calculate_rgb_similarity(image1, image2):
    # Assume RGB average for entire image; refine for eye region if necessary
    avg_color1 = np.mean(image1, axis=(0, 1))  # [R, G, B]
    avg_color2 = np.mean(image2, axis=(0, 1))
    diff = np.linalg.norm(avg_color1 - avg_color2)
    return max(0, 1 - diff / 255)  # Normalize to range [0, 1]

# SSIM (for structural similarity of facial regions)
def calculate_ssim_similarity(image1, image2):
    gray1 = cv2.cvtColor(image1, cv2.COLOR_RGB2GRAY)
    gray2 = cv2.cvtColor(image2, cv2.COLOR_RGB2GRAY)
    return ssim(gray1, gray2)

# Lip curvature similarity
def calculate_lip_curvature_similarity(landmarks1, landmarks2):
    # Extract lip points: upper (48-54) and lower (54-60)
    upper_lip1 = landmarks1[48:54]
    upper_lip2 = landmarks2[48:54]
    lower_lip1 = landmarks1[54:60]
    lower_lip2 = landmarks2[54:60]

    # Calculate Euclidean distance between corresponding points
    upper_diff = np.mean(np.linalg.norm(upper_lip1 - upper_lip2, axis=1))
    lower_diff = np.mean(np.linalg.norm(lower_lip1 - lower_lip2, axis=1))
    max_possible_diff = 1000  # Assume a normalized maximum difference
    similarity = 1 - ((upper_diff + lower_diff) / (2 * max_possible_diff))
    return max(0, similarity)

# Eye, nose, and mouth position ratios
def calculate_position_ratio_similarity(landmarks1, landmarks2, index):
    # Calculate the ratio of a facial landmark relative to the face length
    def position_ratio(landmarks, idx):
        forehead = landmarks[27]  # Between eyebrows
        chin = landmarks[8]       # Tip of the chin
        face_length = np.linalg.norm(forehead - chin)
        if face_length == 0:
            raise ValueError("Face length is zero; invalid landmarks.")
        return (landmarks[idx][1] - forehead[1]) / face_length

    ratio1 = position_ratio(landmarks1, index)
    ratio2 = position_ratio(landmarks2, index)
    return max(0, 1 - abs(ratio1 - ratio2))

# Eye Position Ratio
def calculate_eye_position_ratio_similarity(landmarks1, landmarks2):
    return calculate_position_ratio_similarity(landmarks1, landmarks2, 36)

# Nose Position Ratio
def calculate_nose_position_ratio_similarity(landmarks1, landmarks2):
    return calculate_position_ratio_similarity(landmarks1, landmarks2, 30)

# Mouth Position Ratio
def calculate_mouth_position_ratio_similarity(landmarks1, landmarks2):
    return calculate_position_ratio_similarity(landmarks1, landmarks2, 51)
def calculate_similarities(image1, image2):
    landmarks1, landmarks2 = detect_landmarks(image1), detect_landmarks(image2)
    return {
        "feature_distribution": calculate_cosine_similarity(image1.flatten(), image2.flatten()),
        "eye_color": calculate_rgb_similarity(image1, image2),
        "nose_shape": calculate_ssim_similarity(image1, image2),
        "mouth_shape": calculate_lip_curvature_similarity(landmarks1, landmarks2),
        "eye_position_ratio": calculate_eye_position_ratio_similarity(landmarks1, landmarks2),
        "nose_position_ratio": calculate_nose_position_ratio_similarity(landmarks1, landmarks2),
        "mouth_position_ratio": calculate_mouth_position_ratio_similarity(landmarks1, landmarks2)
    }

# Supporting functions
def detect_landmarks(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    faces = detector(gray)
    if len(faces) == 0:
        raise ValueError("No face detected.")
    return np.array([[p.x, p.y] for p in predictor(gray, faces[0]).parts()])

# Other similarity functions omitted for brevity (same as previous responses)
