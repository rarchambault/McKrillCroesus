import finance_client as fc

data = fc.getData(["AAL", "DAL", "UAL", "LUV", "HA"], "2023-01-01", "2023-02-01")

print(data["AAL"])
