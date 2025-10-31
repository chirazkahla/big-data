# استخدم صورة بايثون الأساسية
FROM python:3.10-slim

# إعداد مجلد العمل داخل الحاوية
WORKDIR /app

# نسخ ملفات المشروع داخل الحاوية
COPY . .

# تثبيت المكتبات المطلوبة (إن وُجدت requirements.txt)
RUN pip install --no-cache-dir -r requirements.txt || true

# الأمر الافتراضي لتشغيل التطبيق (يمكنك تعديله)
CMD ["python3"]
