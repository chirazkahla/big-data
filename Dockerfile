# نبدأ من نظام تشغيل أوبونتو
FROM ubuntu:20.04

# تثبيت الأدوات الأساسية
RUN apt-get update && apt-get install -y \
    wget unzip curl python3 python3-pip && \
    apt-get clean

# إنشاء مجلد داخل الحاوية
WORKDIR /reports

# نسخ كل ملفات مجلد tp3 إلى داخل الحاوية
COPY . .

# تثبيت مكتبات بايثون المطلوبة
RUN pip install jupyterlab pandas numpy matplotlib

# عند تشغيل الحاوية، تفتح JupyterLab على المنفذ 8888
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
