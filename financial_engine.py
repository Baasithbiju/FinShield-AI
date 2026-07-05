def analyze_customer(
    salary,
    expenses,
    savings,
    existing_loan,
    credit_bill,
    cibil,
    employment
):

    disposable_income = salary - expenses

    debt = existing_loan + credit_bill

    if salary == 0:
        debt_ratio = 100
    else:
        debt_ratio = (debt / (salary * 12)) * 100

    if salary == 0:
        savings_ratio = 0
    else:
        savings_ratio = (savings / (salary * 12)) * 100

    score = 50

    reasons = []

    recommendations = []

    # ---------- CIBIL ----------

    if cibil >= 800:
        score += 20
        reasons.append("Excellent CIBIL Score")

    elif cibil >= 750:
        score += 15
        reasons.append("Good Credit History")

    elif cibil >= 650:
        score += 5

    else:
        score -= 20
        reasons.append("Poor Credit History")

    # ---------- Savings ----------

    if savings_ratio > 40:
        score += 15
        reasons.append("Healthy Savings")

    elif savings_ratio > 20:
        score += 8

    else:
        score -= 10

    # ---------- Debt ----------

    if debt_ratio < 20:
        score += 15
        reasons.append("Low Debt Burden")

    elif debt_ratio < 40:
        score += 8

    else:
        score -= 15

    # ---------- Employment ----------

    if employment == "Permanent":
        score += 10
        reasons.append("Stable Employment")

    elif employment == "Self Employed":
        score += 5

    else:
        score -= 5

    # ---------- Disposable Income ----------

    if disposable_income > 30000:
        score += 10

    elif disposable_income < 10000:
        score -= 10

    # ---------- LIMIT SCORE ----------

    score = max(0, min(score, 100))

    # ---------- RISK ----------

    if score >= 80:
        risk = "LOW"

    elif score >= 60:
        risk = "MEDIUM"

    else:
        risk = "HIGH"

    # ---------- LOAN ----------

    if score >= 75:
        decision = "APPROVED"

    elif score >= 60:
        decision = "REVIEW REQUIRED"

    else:
        decision = "REJECTED"

    probability = score

    # ---------- Recommendations ----------

    if score >= 80:

        recommendations.extend([
            "Premium Credit Card",
            "Home Loan",
            "Fixed Deposit",
            "Health Insurance"
        ])

    elif score >= 60:

        recommendations.extend([
            "Gold Loan",
            "Savings Account Upgrade"
        ])

    else:

        recommendations.extend([
            "Improve CIBIL",
            "Reduce Existing Debt",
            "Increase Savings"
        ])

    return {

        "score": score,

        "risk": risk,

        "decision": decision,

        "probability": probability,

        "reasons": reasons,

        "recommendations": recommendations,

        "debt_ratio": round(debt_ratio,2),

        "savings_ratio": round(savings_ratio,2),

        "disposable_income": disposable_income
    }