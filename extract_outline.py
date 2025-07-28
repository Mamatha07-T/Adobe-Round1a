import fitz  # PyMuPDF
import os
import json

def extract_outline_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    outline = []
    title = os.path.splitext(os.path.basename(pdf_path))[0]

    for page_num in range(len(doc)):
        page = doc[page_num]
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            if "lines" in block:
                for line in block["lines"]:
                    line_text = " ".join(span["text"] for span in line["spans"]).strip()
                    font_size = line["spans"][0]["size"]
                    # Headings based on font size
                    if font_size > 20:
                        level = "H1"
                    elif font_size > 16:
                        level = "H2"
                    elif font_size > 12:
                        level = "H3"
                    else:
                        continue

                    outline.append({
                        "level": level,
                        "text": line_text,
                        "page": page_num + 1
                    })

    result = {
        "title": title,
        "outline": outline
    }
    return result

def main():
    input_dir = "/app/input"
    output_dir = "/app/output"

    for file in os.listdir(input_dir):
        if file.endswith(".pdf"):
            pdf_path = os.path.join(input_dir, file)
            result = extract_outline_from_pdf(pdf_path)

            output_path = os.path.join(output_dir, file.replace(".pdf", ".json"))
            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(result, f, indent=2)

if __name__ == "__main__":
    main()
