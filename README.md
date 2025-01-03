# 🌟 Socioeconomic and Health Disparities in Seattle

## 📝 **Project Description**

This project uses Altair to visualize socioeconomic disadvantage and health outcomes in Seattle, showcasing metrics like disadvantage scores, health scores, and disability percentages.

---

## 🎨 **Visualizations**

**1. Accessibility and Zoom**
<p align="center">
  <img src="https://github.com/user-attachments/assets/387328b3-c0ba-463c-80d5-7ed126dda687" alt="An interactive visualization with Accessibility and Zoom, showing disadvantage and disability in Seattle" width="50%">
</p>

**2. Dropdown Menu**
<p align="center">
  <img src="https://github.com/user-attachments/assets/ca5569c9-2651-449e-a98c-e86562abcaf4" alt="An interactive visualization with a Dropdown Menu, comparing disadvantage and disability with obesity and asthma" width="50%">
</p>

**3. Brush and Link - Multiple Selections**
<p align="center">
  <img src="https://github.com/user-attachments/assets/e0ab108b-2bf9-4277-848d-1806b9131bb3" alt="An interactive visualization with Brush and Link between Multiple Selections, comparing disadvantage and disability with obesity and asthma" width="50%">
</p>

**5.  Interactive Legend**
<p align="center">
  <img src="https://github.com/user-attachments/assets/078c3550-f209-4dc3-ae0e-813cd3d73655" alt="An interactive visualization with an Interactive Legend, showing disadvantage and disability in Seattle " width="50%">
</p>

**6. Strip Plots + Brushing**
<p align="center">
  <img src="https://github.com/user-attachments/assets/c1a215e8-3bd6-4647-92b2-f803468616e9" alt="An interactive visualization with brushing and strip plots, showing disadvantage and disability in Seattle" width="50%">
</p>


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


## 💻 **Technologies and Tools**
- **Altair:** Declarative visualization library for Python.
- **Pandas:** For data manipulation and processing.

<br>

---

## 🚀 **How to Use**

### **Option 1: Run with Google Colab (Recommended)**
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
