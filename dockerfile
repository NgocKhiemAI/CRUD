# Dua tren image co ban nao
FROM python:3.9.1
# Khai bao thu muc lam viec
WORKDIR /home/ngockhiem/fastAPI-mongo-app


# Copy toàn bộ file mã nguồn và các file khác vào image
COPY setup.txt setup.txt
# cai dat cac nen tang can thiet cho file chay  dua vao file cai
RUN pip3 install -r setup.txt
# run cmd
COPY . .

CMD ["uvicorn","motormongo:app","--host","0.0.0.0","--port","3000"]
