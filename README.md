# edu-ai-workflow-automation

Sistem otomatis berbasis AI yang dirancang untuk menghasilkan konten
pembelajaran, mulai dari rangkuman materi, soal latihan, penjelasan,
hingga ilustrasi. Dibuat berdasarkan workflow terstruktur menggunakan LLM dan tool
generatif lainnya. Proyek ini menggabungkan pemrosesan teks, analisis
materi, AI generation, serta automasi layout untuk mendukung proses
produksi konten edukasi secara cepat, konsisten, dan dapat
direplikasi.

## Purpose

Proyek ini dibuat untuk mengeksplorasi bagaimana AI Workflow Automation
dapat membantu proses pembuatan konten pendidikan. Workflow mencakup:
ekstraksi materi, peringkasan, pembuatan soal & pembahasan, proofreading
berbasis AI, pembuatan ilustrasi AI, penyusunan layout otomatis, serta
dokumentasi hasil eksperimen AI.

Pipeline ini dirancang modular sehingga mudah dikembangkan untuk
kebutuhan content creation di edutech, kurasi konten, eksperimen LLM,
generasi soal otomatis, atau produksi materi pembelajaran dalam skala
besar.

## Key Features

### 1. Automated Material Processing

-   Ekstraksi teks dari PDF atau input manual.
-   Pembersihan dan normalisasi materi.

### 2. Summarization & Concept Mapping

-   Ringkasan terstruktur dengan LLM.
-   Identifikasi learning objective dan konsep inti.

### 3. AI Question Generation

-   Pembuatan soal pilihan ganda, isian, dan uraian.
-   Termasuk jawaban, pembahasan, dan level kesulitan.

### 4. Quality Check & Proofreading

-   Validasi konsep dan pengecekan kesalahan akademik dengan LLM kedua.

### 5. AI-Based Illustration

-   Pembuatan ilustrasi atau diagram menggunakan image generation tools.

### 6. Automated Layout Builder

-   Penyusunan konten ke template modul/slide menggunakan Python
    (pptx/ReportLab).

### 7. Experiment Logging & Documentation

-   Menyimpan prompt, parameter, dan hasil generasi untuk evaluasi.

## Workflow Overview

1.  Input Material\
2.  Preprocessing\
3.  LLM Processing\
4.  Quality Revision\
5.  Illustration Generation\
6.  Layout Automation\
7.  Export & Documentation

## Tech Stack

-   Python
-   Streamlit
-   LLM APIs (Gemini / OpenAI)
-   Midjourney / Image Models
-   python-pptx / ReportLab
-   PyPDF2 / pdfplumber

## Use Cases

-   Produksi soal otomatis
-   Modul belajar cepat
-   Riset LLM untuk konten akademik
-   Proofreading AI
-   Pipeline generatif untuk kurasi konten

## Repository Structure (Draft)

    edu-ai-content-pipeline/
    │
    ├── data/
    │   ├── samples/
    │   └── outputs/
    │
    ├── src/
    │   ├── preprocessing/
    │   ├── summarization/
    │   ├── question_generation/
    │   ├── quality_check/
    │   ├── illustration/
    │   └── layout_automation/
    │
    ├── logs/
    │
    ├── streamlit_app/
    │
    ├── README.md
    └── requirements.txt

## Future Enhancements

-   Support multi-subject
-   Template builder
-   Model benchmarking
-   Multilingual content generation
-   Auto-tagging kurikulum

## License

MIT License.