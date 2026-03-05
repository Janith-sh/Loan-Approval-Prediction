import joblib
import pandas as pd

# Load the model and features
model = joblib.load("model/loan_model.pkl")
features = joblib.load("model/features.pkl")

print("Expected feature names by the model:")
print("=" * 60)
if hasattr(model, 'feature_names_in_'):
    print("\nFeature names:")
    for i, feature in enumerate(model.feature_names_in_, 1):
        print(f"{i:2d}. {feature}")
    print(f"\nTotal features expected: {len(model.feature_names_in_)}")
else:
    print("Model doesn't have feature_names_in_ attribute")

print("\n" + "=" * 60)
print("\nFeatures.pkl content:")
print(features)
print(type(features))
