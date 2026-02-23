import pandas as pd

class FinancialAnalyzer:

    def compare_gst_bank(self, gst_df, bank_df):

        gst_total = gst_df["reported_revenue"].sum()
        bank_total = bank_df["deposit_amount"].sum()

        difference = gst_total - bank_total

        result = {
            "gst_total": gst_total,
            "bank_total": bank_total,
            "difference": difference,
            "flag": abs(difference) > (0.1 * gst_total)
        }

        return result

    def calculate_debt_ratio(self, total_debt, total_revenue):
        if total_revenue == 0:
            return 0
        return total_debt / total_revenue