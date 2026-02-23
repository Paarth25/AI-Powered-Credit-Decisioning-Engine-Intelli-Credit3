import pdfplumber
from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")

class PDFParser:

    def extract_text(self, pdf_path):
        full_text = ""
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                full_text += page.extract_text() + "\n"
        return full_text

    def extract_structured_data(self, text):
        prompt = f"""
        Extract the following from the financial report:

        1. Total Revenue
        2. Net Profit
        3. Total Debt
        4. Contingent Liabilities
        5. Auditor Remarks
        6. Legal Cases Mentioned

        Return in JSON format.

        Text:
        {text[:12000]}
        """

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        return response.choices[0].message.content