# نظام لحساب جرعة الدواء باستخدام المنطق الضبابي  
Fuzzy Logic Based Drug Dosage Calculation System

## 📌 وصف المشروع | Project Description  
هذا المشروع عبارة عن نظام بسيط يستخدم المنطق الضبابي (Fuzzy Logic) لحساب جرعة دواء مناسبة للمريض بناءً على ثلاث مدخلات رئيسية:  
This project is a simple system that uses fuzzy logic to calculate an appropriate drug dosage for a patient based on three main inputs:  
- العمر | Age  
- الوزن | Weight  
- شدة المرض | Disease Severity  

النظام مبني باستخدام لغة Python مع واجهة رسومية GUI تعتمد على مكتبة `tkinter`. كما يعتمد على مكتبة `matplotlib` لعرض الرسومات البيانية.  
The system is built using Python with a GUI based on the `tkinter` library. It also uses `matplotlib` for displaying charts.

## ⚙️ المتطلبات | Requirements  
- Python 3.8 أو أحدث | Python 3.8 or later  
- المكتبات | Libraries:  
  - numpy  
  - matplotlib  
  - tkinter (موجودة افتراضيًا في بايثون | comes pre-installed with Python)

## 💡 كيفية الاستخدام | How to Use  
1. شغّل البرنامج عن طريق ملف `dozu_hesaplama.py`.  
   Run the program via the file `dozu_hesaplama.py`.  
2. أدخل القيم التالية | Enter the following values:  
   - العمر (بالسنوات) | Age (in years)  
   - الوزن (بالكيلوغرام) | Weight (in kg)  
   - شدة المرض (قيمة من 0 إلى 10) | Disease severity (value from 0 to 10)  
3. اضغط على "احسب الجرعة" لرؤية النتائج.  
   Click "Calculate Dosage" to see the results.  
4. يمكنك الضغط على "عرض دوال العضوية" لرؤية الرسومات البيانية للمدخلات.  
   You can click "Show Membership Functions" to view input charts.

## 📊 آلية العمل | How it Works  
يعتمد النظام على قواعد منطق ضبابي مثل:  
The system uses fuzzy logic rules such as:  
- إذا كان العمر صغيرًا والوزن خفيفًا والشدة خفيفة → الجرعة منخفضة.  
  If age is young, weight is light, and severity is low → dosage is low.  
- إذا كانت الشدة متوسطة والوزن متوسطًا → الجرعة متوسطة.  
  If severity is medium and weight is average → dosage is medium.  
- إذا كانت الشدة شديدة أو العمر كبيرًا → الجرعة مرتفعة.  
  If severity is high or age is old → dosage is high.

ثم يتم تطبيق عملية **الدمج والتقريب (defuzzification)** لحساب الجرعة النهائية كمقدار رقمي.  
Then a **defuzzification** process is applied to compute the final dosage as a numeric value.

## 👨‍💻 المطور | Developer  
- اسم المطور | Developer Name: نور الدين حباش  
- المشروع تم ضمن | Project done at: جامعة شرناك | University of Şırnak
