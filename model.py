import pandas as pd

data = pd.read_csv("products.csv")

data["Deal_Score"] = (
    data["rating"] * 20
    + data["discount"] * 2
    + data["revie ws"] / 1000
    - data["price"] / 10000
)

print(data[["product_name", "website", "Deal_Score"]])
best_deal = data.loc[data["Deal_Score"].idxmax()]

print("\nBest Deal:")
print(best_deal[["product_name", "website", "price", "rating", "Deal_Score"]])