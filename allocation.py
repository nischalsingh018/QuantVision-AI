def allocation_guidance(data):

    data = data.copy()

    equity = []
    cash = []

    for _, row in data.iterrows():

        regime = row["Regime"]

        if regime == "Strong Bull":
            e, c = 90, 10

        elif regime == "Bull":
            e, c = 75, 25

        elif regime == "Neutral":
            e, c = 50, 50

        elif regime == "Bear":
            e, c = 30, 70

        else:
            e, c = 10, 90

        equity.append(e)
        cash.append(c)

    data["Equity Allocation"] = equity
    data["Cash Allocation"] = cash

    return data