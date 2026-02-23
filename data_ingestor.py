import os
import pandas as pd

class DataIngestor:

    def load_pdf(self, file_path):
        if not os.path.exists(file_path):
            raise FileNotFoundError("PDF not found.")
        return file_path

    def load_csv(self, file_path):
        if not os.path.exists(file_path):
            raise FileNotFoundError("CSV not found.")
        return pd.read_csv(file_path)

    def load_user_notes(self, notes_text):
        return notes_text