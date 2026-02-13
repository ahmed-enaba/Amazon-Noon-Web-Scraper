# 🛒 Amazon & Noon Web Scraper (Python + Selenium)

A Python web scraping project that uses **Selenium** and **BeautifulSoup** to collect product data from **Amazon Egypt** and **Noon Egypt**, then saves the results into a CSV file.


## 📌 Project Overview

This project allows the user to:

- Search for any product keyword
- Scrape data from:
  - Amazon Egypt
  - Noon Egypt
- Extract the following data:
  - 📦 Product Name
  - 💰 Price
  - ⭐ Rating
  - 🔗 Product Link
- Save all collected data into a CSV file

The script works with **dynamic websites** using Selenium WebDriver.

## 🛠️ Technologies Used

- Python 3
- Selenium
- WebDriver Manager
- BeautifulSoup (bs4)
- CSV module
- Chrome WebDriver


## 📂 Project Structure

amazon-noon-scraper/
│
├── scraper.py
├── csv.csv
└── README.md

## ▶️ How to Run the Project

### 1️⃣ Install Required Libraries

```bash
pip install selenium webdriver-manager beautifulsoup4
```

### 2️⃣ Make Sure You Have Google Chrome Installed

The project uses **Chrome WebDriver**.

### 3️⃣ Run the Script

```bash
python scraper.py
```

---

### 4️⃣ Enter Search Keyword

When prompted:

```text
Enter what do you want to search about
```

Example:
```text
laptop
```


## 📊 Output (CSV File)

- The CSV file is created automatically
- Contains:
  - Amazon products
  - Separator row (************)
  - Noon products

### CSV Columns:
- item name
- price
- link
- rate


## 🧠 How the Code Works

- Uses Selenium to open Chrome browser
- Searches for user input keyword
- Collects product elements using XPath
- Extracts HTML and text data
- Stores results in Python dictionaries
- Writes all data into a CSV file using `csv.DictWriter`

## ⚠️ Important Notes

- This project is for **educational purposes only**
- Websites may change their structure at any time
- Scraping may require:
  - Waiting times (`time.sleep`)
  - Updated XPath selectors
- Excessive scraping may violate website policies


## 🚀 Future Improvements

- Add headless browser mode
- Add page scrolling for more results
- Handle pagination
- Save data into a database (SQLite / MySQL)
- Add price comparison feature
- Add error logging system


## 👨‍💻 Author

Ahmed  
Computer Science Student  
Interested in Web Scraping, Backend Development & Automation


## 📄 Disclaimer

This project is intended for learning and educational purposes only.  
Please review and respect the Terms of Service of any website before scraping.
