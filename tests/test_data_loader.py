import pandas as pd

from backend.data_loader import engineer_features


def test_feature_engineering():
    df = pd.DataFrame(
        {
            "Year_Birth": [1985],
            "Education": ["Graduation"],
            "Marital_Status": ["Single"],
            "Income": [50000],
            "Kidhome": [1],
            "Teenhome": [1],
            "Dt_Customer": ["2013-01-01"],
            "Recency": [20],
            "MntWines": [100],
            "MntFruits": [50],
            "MntMeatProducts": [200],
            "MntFishProducts": [50],
            "MntSweetProducts": [25],
            "MntGoldProds": [75],
            "NumDealsPurchases": [2],
            "NumWebPurchases": [5],
            "NumCatalogPurchases": [3],
            "NumStorePurchases": [7],
            "NumWebVisitsMonth": [5],
            "AcceptedCmp1": [1],
            "AcceptedCmp2": [0],
            "AcceptedCmp3": [0],
            "AcceptedCmp4": [0],
            "AcceptedCmp5": [1],
        }
    )

    result = engineer_features(df)

    assert result.loc[0, "Age"] == 29
    assert result.loc[0, "TotalChildren"] == 2
    assert result.loc[0, "TotalSpending"] == 500
    assert result.loc[0, "TotalPurchases"] == 15

    assert "DealPurchaseShare" in result.columns
    assert "WebPurchaseShare" in result.columns
    assert "CatalogPurchaseShare" in result.columns
    assert "CampaignAcceptedCount" in result.columns