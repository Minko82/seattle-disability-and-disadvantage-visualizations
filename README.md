# 🌟 Socioeconomic and Health Disparities in Seattle

## 📝 **Project Description**

This project uses Altair to visualize socioeconomic disadvantage and health outcomes in Seattle, showcasing metrics like disadvantage scores, health scores, and disability percentages.

<br>

---

## 📂 **Dataset**

The data is sourced from a GeoJSON file with features like:
- **SOCIOECON_DISADV_SCORE**: Socioeconomic Disadvantage Score.
- **HEALTH_DISADV_SCORE**: Health Disadvantage Score.
- **PCT_ADULT_WITH_DISABILITY**: Percentage of adults with disabilities.
- **PCT_ADULT_WITH_OBESITY**: Percentage of adults with obesity.
- **PCT_ADULT_WITH_ASTHMA**: Percentage of adults with asthma.

<br>

---

## 🎨 **Visualizations**


<br>


---

## 💻 **Technologies and Tools**
- **Altair:** Declarative visualization library for Python.
- **Pandas:** For data manipulation and processing.

<br>

---

## 🚀 **How to Use**

### **Option 1: Run with Google Colab (Preferred)**
1. Upload the **seattle-disability-vis.ipynb** notebook to Google Colab
   
2. Update Altair:
   
   If you’re running the project in Google Colab, update your Altair version to avoid compatibility issues. Run the following line of code in a Colab cell:
   ```bash
   pip install -U altair vega_datasets
   ```

   After running this, go to **Runtime > Restart Runtime** in the Colab menu.

3. Run the Notebook:
   
   Execute all cells in the notebook to generate visualizations and analyze data.


---

### **Option 2: Run with Jupyter Notebook**
1. Clone and open the repository:  
   ```bash
   git clone https://github.com/Minko82/Seattle-Disability-and-Disadvantage-Visualizations.git
   cd Seattle-Disability-and-Disadvantage-Visualizations
   ```

2. Launch the Notebook:
Open the notebook using Jupyter:

   ```bash
   jupyter notebook seattle-disability-vis.ipynb
   ```

---
   

### **Option 3: Run with Python Command Line**

1. Clone and open the repository:  
   ```bash
   git clone https://github.com/Minko82/Seattle-Disability-and-Disadvantage-Visualizations.git
   cd Seattle-Disability-and-Disadvantage-Visualizations
   ```

2. Run the Python script from the Command Line:
   ```bash
   python Visualizations.py
   ```

