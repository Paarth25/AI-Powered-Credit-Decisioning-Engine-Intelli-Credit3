class RiskEngine:

    def compute_score(self, financial_result, debt_ratio, research_risk, user_note):

        score = 100

        if financial_result["flag"]:
            score -= 20

        if debt_ratio > 0.6:
            score -= 20

        if "litigation" in research_risk.lower():
            score -= 20

        if "40% capacity" in user_note.lower():
            score -= 10

        return max(score, 0)

    def recommend(self, score):
        if score > 80:
            return "Approve Full Limit", 9.5
        elif score > 60:
            return "Approve Reduced Limit", 11.5
        else:
            return "Reject", None