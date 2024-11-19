# KinFace: Family Facial Similarity Analysis

KinFace는 가족 구성원 간의 얼굴 유사도를 분석하기 위한 프로젝트입니다. 
이 프로젝트는 다양한 얼굴 메트릭(눈동자 색, 코와 입의 모양, 얼굴 랜드마크 기반 비율 등)을 활용하여 부모-자녀, 형제-자매 간의 유사성을 계산하고 시각화합니다.

## 📂 Repository Structure

```
KinFace/ │ ├── data/ │ ├── processed_images/ # 전처리된 얼굴 이미지 │ ├── embeddings/ # 얼굴 임베딩 데이터 │ ├── results/ # 결과 파일 저장 (유사도 점수, 시각화 등) │ ├── src/ │ ├── similarity_metrics.py # 유사도 계산 함수들 (코사인 유사도, SSIM 등) │ ├── landmark_analysis.py # 랜드마크 기반 메트릭 (곡률, 위치 비율 등) │ ├── preprocessing.py # 이미지 전처리 (얼굴 탐지, 랜드마크 추출 등) │ ├── visualization.py # 시각화 코드 (그래프 생성 등) │ ├── notebooks/ │ ├── analysis.ipynb # 주요 분석 및 결과 정리 노트북 │ ├── README.md # 프로젝트 개요 및 설명 ├── requirements.txt # 프로젝트 의존성 파일 └── main.py # 메인 실행 파일
```
