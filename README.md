# GTFS Merger

## 📌 Overview
GTFS Merger is a Python-based tool that **merges multiple General Transit Feed Specification (GTFS) feeds** into a single, unified feed. It ensures:
- Consistent file structures across feeds.
- Unique key validation for GTFS data.
- Duplicate handling with user confirmation.
- Compressed `.zip` output for easy use.

---

## 🚀 **Installation & Setup**

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/yourusername/gtfs_merger.git
cd gtfs_merger
```

### **2️⃣ Set Up a Virtual Environment**
Run the following to create and activate a virtual environment:

```sh
# Create virtual environment (only needed once)
python3 -m venv venv

# Activate virtual environment (Mac/Linux)
source venv/bin/activate

# Activate virtual environment (Windows)
venv\Scripts\activate
```

### **3️⃣ Install Dependencies**
Once inside the virtual environment, install required dependencies:

```sh
pip install -r requirements.txt
```

---

## 📂 **Project Structure**
```
gtfs_merger/
├── input_feeds/        # Place GTFS .zip files here
├── output_feed/        # Merged GTFS .zip file will be saved here
├── gtfs_merger/
│   ├── __init__.py
│   ├── merger.py       # Main GTFS merging logic
│   ├── utils.py        # Helper functions
│   ├── constants.py    # GTFS unique key definitions
├── main.py             # Entry point of the program
├── requirements.txt    # Python dependencies
├── .gitignore          # Files to exclude from version control
├── README.md           # Project documentation
```

---

## ▶️ **How to Use**

### **Step 1️⃣: Place GTFS Feeds in `input_feeds/`**
- Ensure you have **GTFS `.zip` files** in the `input_feeds/` directory.
- Each `.zip` file should contain GTFS `.txt` files.

### **Step 2️⃣: Run the Program**
Inside the project folder, run:

```sh
python main.py
```

During execution:
- The program **extracts the `.zip` feeds**.
- It **checks for duplicates** and asks the user for confirmation before removing them.
- The merged GTFS is **saved as a `.zip` file** in `output_feed/merged_gtfs.zip`.

---

## 🔄 **Reinstall Dependencies (If Needed)**
If you need to reinstall dependencies, use:

```sh
pip install -r requirements.txt
```

---

## ❌ **Deactivate Virtual Environment**
When finished, deactivate the virtual environment:

```sh
deactivate
```

---

## 💪 **Troubleshooting**
1. **Ensure `.zip` feeds are inside `input_feeds/`**  
   If no output is generated, check that `.zip` files exist in the correct folder.

2. **Check Dependencies**  
   If any error occurs, try reinstalling dependencies:

   ```sh
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

3. **Permission Issues on macOS/Linux?**  
   Run:

   ```sh
   chmod -R 755 output_feed/
   ```

---

## 🐟 **License**
This project is open-source and available under the MIT License.

---

### **✅ Now You're Ready to Use GTFS Merger! 🚀**

