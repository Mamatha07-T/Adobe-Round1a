# Adobe - Connecting the Dots Challenge (Round 1A)

## 🚀 Challenge Summary

Build a document outline extractor that parses PDF files and returns structured metadata in JSON format. Output should include:

- 📌 Title of the document
- 📌 All headings with their respective levels (H1, H2, H3)
- 📌 Page numbers for each heading

### ✅ Expected Output Format:

```json
{
  "title": "Understanding AI",
  "outline": [
    { "level": "H1", "text": "Introduction", "page": 1 },
    { "level": "H2", "text": "What is AI?", "page": 2 },
    { "level": "H3", "text": "History of AI", "page": 3 }
  ]
}
````

---

## 🧠 Approach

* **PDF Parsing**: Utilized `PyMuPDF` (fitz) to read structured data like text blocks, fonts, and positioning.
* **Title Detection**: Assumed the largest, boldest top-centered text on the first page is the title.
* **Heading Hierarchy**:

  * Analyzed font sizes across pages to determine relative heading levels (H1 > H2 > H3).
  * Used text styles (bold, position, font family) and spatial layout.
* **Page Mapping**: For every heading, stored the page number it was found on.

---

## 📁 Project Structure

```
📁 Adobe-Round_1a/
├── Dockerfile
├── main.py
├── requirements.txt
└── README.md
```

---

## 🐳 Docker Instructions

### 🔧 Build Docker Image

```bash
docker build --platform linux/amd64 -t outline_extractor:solution1a .
```

### ▶️ Run the Container

```bash
docker run --rm \
  -v $(pwd)/input:/app/input \
  -v $(pwd)/output:/app/output \
  --network none \
  outline_extractor:solution1a
```

### 📂 Directory Setup

* `input/` — Place your `.pdf` files here
* `output/` — Extracted `.json` files will be saved here

#### Example:

```bash
input/
└── sample.pdf

output/
└── sample.json
```

---

## ⚙️ Dependencies

Dependencies are listed in `requirements.txt` and installed inside the container:

```txt
PyMuPDF
```

No external APIs or internet access required.

---

## 💡 Assumptions

* Font size and weight determine heading levels
* Same heading structure is used consistently across the document
* Title is prominent and unique on the first page

---

## ✅ Submission Checklist

* [x] Dockerfile at project root
* [x] Python script for outline extraction
* [x] Proper folder structure (`input/` and `output/`)
* [x] Output in valid JSON format
* [x] Adheres to:

  * CPU-only execution
  * <200MB image size
  * No internet access
  * <10s runtime per document

---

## 👤 Team Members

**Mamatha Taneti**
[Github](https://github.com/Mamatha07-T)
**Bhavani Sowmya Rella**
[GitHub](https://github.com/RELLABHAVANISOWMYA)
**Prajwala Pilli**
[Github](https://github.com/PrajwalaPilli/)


---

te this into your `README.md` in VS Code and commit it to your GitHub repo. Let me know if you want help with pushing it or with Dockerfile / `main.py` as well.
```
