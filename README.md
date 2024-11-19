# KinFace: Family Facial Similarity Analysis

KinFace는 가족 구성원 간의 얼굴 유사도를 분석하기 위한 프로젝트입니다. 
이 프로젝트는 다양한 얼굴 메트릭(눈동자 색, 코와 입의 모양, 얼굴 랜드마크 기반 비율 등)을 활용하여 부모-자녀, 형제-자매 간의 유사성을 계산하고 시각화합니다.

## 📂 Repository Structure

```
KinFace/
│ ├── data/
│ ├── processed_images/ # 전처리된 얼굴 이미지
│ ├── embeddings/ # 얼굴 임베딩 데이터
│ ├── results/ # 결과 파일 저장 (유사도 점수, 시각화 등)
│ ├── src/
│ ├── similarity_metrics.py # 유사도 계산 함수들 (코사인 유사도, SSIM 등)
│ ├── landmark_analysis.py # 랜드마크 기반 메트릭 (곡률, 위치 비율 등)
│ ├── preprocessing.py # 이미지 전처리 (얼굴 탐지, 랜드마크 추출 등)
│ ├── visualization.py # 시각화 코드 (그래프 생성 등)
│ ├── notebooks/
│ ├── analysis.ipynb # 주요 분석 및 결과 정리 노트북
│ ├── README.md # 프로젝트 개요 및 설명
| ├── requirements.txt # 프로젝트 의존성 파일
│ ├── code # streamlit 구현
  │ ├── app.py # 메인 실행 파일
```

## 🛠 Features

- **Facial Feature Similarity**: 코사인 유사도, 구조적 유사도(SSIM) 등을 사용하여 얼굴 임베딩 비교.
- **Landmark Analysis**: 입술 곡률, 눈, 코, 입 위치 비율 계산.
- **Visualization**: 가족 구성원 간의 유사성을 시각적으로 표현하는 바 차트 생성.
- **Preprocessing**: 얼굴 탐지, 랜드마크 추출 및 전처리 자동화.

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/Seyoung-C/KinFace.git
cd KinFace
```
2. Install Dependencies
```
pip install -r requirements.txt
```
4. Run the Project
```
python main.py
```

📊 Example Output
Similarity Chart
프로젝트 실행 후 생성된 바 차트:
![image](https://github.com/user-attachments/assets/c672e178-4a04-4a04-9d5c-2f0c449b8237)

Sample Similarity Scores
```
Final Similarity Scores:
Father-Child: 0.84
Mother-Child: 0.89
Sibling-Child: 0.81
```

✨ Future Enhancements
랜드마크 기반 유사성 개선 및 추가 메트릭 개발.
가족 관계 예측 기능 추가 (e.g., 부모-자녀, 형제-자매).
웹 기반 대시보드 제공.
