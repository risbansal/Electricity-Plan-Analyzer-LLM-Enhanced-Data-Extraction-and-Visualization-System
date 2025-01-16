# tools/pdf_tools.py
from crewai_tools import BaseTool
import pdfplumber
import csv
import os

class file_reader(BaseTool):
    
    # def run(self,folder_path):
        
    #     try:
    #         self.process_pdfs(folder_path)
    #     except FileNotFoundError as e:
    #         return f"Error: {str(e)}"
        
            

    def process_pdfs(folder_path):
        data = []
        for filename in os.listdir(folder_path):
            if filename.endswith('.pdf'):
                file_path = os.path.join(folder_path, filename)
                with pdfplumber.open(file_path) as pdf:
                    text = ''.join(page.extract_text() for page in pdf.pages)
                    data.append(extract_data_from_text(text))
        return data

    def write_to_csv(data):
        
        output_file = "D:\Projects\WhiteGlove\data_processing\src\output\out.csv"
        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Company Name', 'Plan Name', 'Base Charge', 'Energy Charge'])
            writer.writerows(data)

        # return f"Processed {len(data)} files and saved to {output_file}"




# def extract_data_from_text(text):
#     # Extract fields using custom logic
#     return ["Example Company", "Example Plan", "$10.00", "$0.15/kWh"]
