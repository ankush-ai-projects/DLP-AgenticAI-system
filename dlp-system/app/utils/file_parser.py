"""Bounded file parser used by local and endpoint system scanners."""
import csv
from typing import Optional


class FileParser:
    """Parse different file formats"""

    @staticmethod
    def parse_txt(file_path: str) -> Optional[str]:
        """Parse text file"""
        try:
            with open(file_path, "r", encoding="utf-8", errors="replace") as f:
                return f.read()
        except Exception as e:
            print(f"Error reading text file: {e}")
            return None

    @staticmethod
    def parse_pdf(file_path: str) -> Optional[str]:
        """Parse PDF file"""
        try:
            from pypdf import PdfReader
            reader = PdfReader(file_path)
            return "\n".join(page.extract_text() or "" for page in reader.pages)
        except Exception as e:
            print(f"Error reading PDF file: {e}")
            return None

    @staticmethod
    def parse_docx(file_path: str) -> Optional[str]:
        """Parse DOCX file"""
        try:
            from docx import Document
            document = Document(file_path)
            parts = [paragraph.text for paragraph in document.paragraphs]
            for table in document.tables:
                for row in table.rows:
                    parts.append(" ".join(cell.text for cell in row.cells))
            return "\n".join(parts)
        except Exception as e:
            print(f"Error reading DOCX file: {e}")
            return None

    @staticmethod
    def parse_csv(file_path: str) -> Optional[str]:
        """Parse CSV file"""
        try:
            with open(file_path, "r", encoding="utf-8", errors="replace", newline="") as f:
                return "\n".join(" ".join(row) for row in csv.reader(f))
        except Exception as e:
            print(f"Error reading CSV file: {e}")
            return None

    @staticmethod
    def parse_xlsx(file_path: str) -> Optional[str]:
        try:
            from openpyxl import load_workbook
            workbook = load_workbook(file_path, read_only=True, data_only=True)
            rows: list[str] = []
            for sheet in workbook.worksheets:
                rows.append(f"[sheet:{sheet.title}]")
                for row in sheet.iter_rows(values_only=True):
                    rows.append(" ".join("" if value is None else str(value) for value in row))
            workbook.close()
            return "\n".join(rows)
        except Exception as e:
            print(f"Error reading XLSX file: {e}")
            return None

    @classmethod
    def parse(cls, file_path: str) -> Optional[str]:
        lower = file_path.lower()
        if lower.endswith((".txt", ".json", ".xml", ".log")):
            return cls.parse_txt(file_path)
        if lower.endswith(".csv"):
            return cls.parse_csv(file_path)
        if lower.endswith(".pdf"):
            return cls.parse_pdf(file_path)
        if lower.endswith(".docx"):
            return cls.parse_docx(file_path)
        if lower.endswith(".xlsx"):
            return cls.parse_xlsx(file_path)
        return None
