### **Project Summary: Hybrid Job Link Extractor and Filter**  

This Python script automates the extraction and filtering of job listings from `.eml` email files, identifying **hybrid/remote** job opportunities.  

---

### **Features & Functionality**
1. **Extracts Job Links from Emails**  
   - Scans all `.eml` files in the directory (`email1.eml`, `email2.eml`, etc.).
   - Decodes encoded links (handles `quoted-printable` and HTML entities).
   - Supports multi-line URLs (some emails split links across multiple lines).

2. **Filters Jobs Based on Keywords**  
   - Opens each job listing using **Selenium**.
   - Searches for terms: `"hybrid"`, `"remote"`, `"work from home"`, `"flexible working"`.
   - Only keeps job listings that match these keywords.

3. **Handles Errors & Encoding Issues**  
   - Skips unreadable email content while logging decoding errors.
   - Uses `errors="replace"` to ensure the script continues running.
   - Avoids crashes from broken or non-UTF-8 encoded emails.

4. **Runs Fully Automated with ChromeDriver**  
   - Uses **Selenium** to load and scan job listing pages.
   - Runs in **headless mode** (doesn't open a browser window).

---

### **How to Use**
1. **Install Dependencies**:
   ```bash
   pip install selenium
   ```
2. **Download & Set Up ChromeDriver**:
   - Ensure ChromeDriver is in the project folder or `/usr/local/bin/`
   - Run:  
     ```bash
     chromedriver --version
     ```
3. **Run the Script**:
   ```bash
   python3 filter_hybrid_jobs.py
   ```
4. **View Results**:
   - The script prints **Hybrid/Remote job links**.
   - Skips **Onsite jobs** automatically.

---

### **Use Cases**
✅ **Automates Job Hunting**: No need to manually check each job listing.  
✅ **Filters for Remote/Hybrid Work**: Saves time by skipping irrelevant jobs.  
✅ **Handles Large Email Files**: Processes multiple `.eml` files efficiently.  

---
