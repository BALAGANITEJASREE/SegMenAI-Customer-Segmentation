import pandas as pd

from backend.inference import (
    load_clustering_artifacts,
    predict_customer,
    predict_customers,
)

DATA_PATH = "data/processed/customer_cleaned.csv"


def test_model_artifacts_load():
    _, model, metadata = load_clustering_artifacts()

    assert type(model).__name__ == "KMeans"
    assert metadata["final_k"] == 3


def test_single_customer_prediction():
    df = pd.read_csv(DATA_PATH).head(1)

    result = predict_customer(df)

    assert "customer_id" in result
    assert "cluster" in result
    assert "cluster_name" in result
    assert "recommendation" in result
    assert result["cluster"] in [0, 1, 2]


def test_batch_prediction():
    df = pd.read_csv(DATA_PATH).head(10)

    result = predict_customers(df)

    assert len(result) == 10
    assert "ID" in result.columns
    assert "Cluster" in result.columns
    assert "Cluster_Name" in result.columns
    assert set(result["Cluster"]).issubset({0, 1, 2})