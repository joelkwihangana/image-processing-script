This is a simple Python tool that automatically fixes images before they are used on a website.

It rotates images 90° clockwise, resizes them to 128x128 pixels, converts them to JPEG format, and saves the corrected versions in a separate folder.

---

## 📂 Project Structure

* `images/` → put your original images here
* `processed/` → processed images will be saved here
* `script.py` → main Python script
* `requirements.txt` → dependencies
* `README.md` → this file

---

## 🚀 How to Use

1. Clone the repository

   ```
   git clone https://github.com/your-username/image-processing-script.git
   cd image-processing-script
   ```
2. Install dependencies

   ```
   pip install -r requirements.txt
   ```
3. Add your images to the `images/` folder
4. Run the script

   ```
   python3 script.py
   ```
5. Check the `processed/` folder for results

---

## 🛠️ Customization

* Change the resize dimensions in `script.py`:

  ```
  resized = rotated.resize((128, 128))
  ```
* Change the output format from `"JPEG"` to `"PNG"` or another supported type if needed.

---

## 📖 Example

If you put `logo.png` inside `images/`, after running the script you’ll find `logo.jpeg` inside `processed/`.

---

## 🤝 Contributions

Feel free to fork this project and adapt it to your needs. Small improvements like adding new formats or filters are welcome.
