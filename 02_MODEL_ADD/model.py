import joblib
import pandas as pd
import numpy as np

def load_model(path="model.pkl"):
    """학습된 모델 파일 로드"""
    model = joblib.load(path)
    return model

def predict(model, input_data):
    """
    모델 예측 수행
    
    Parameters:
    -----------
    model : 학습된 모델 객체
    input_data : dict 형태의 입력 데이터
    
    Returns:
    --------
    prediction : 예측된 클래스 (<=50K 또는 >50K)
    probability : 각 클래스에 대한 확률
    """
    # DataFrame으로 변환
    df = pd.DataFrame([input_data])
    
    # 예측 수행
    prediction = model.predict(df)[0]
    probability = model.predict_proba(df)[0]
    
    return prediction, probability