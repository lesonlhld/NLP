# Bài tập lớn xử lý ngôn ngữ tự nhiên HK211

## Thông tin chương trình:
* Ngôn ngữ: Python

## Hướng dẫn sử dụng:
* Cài đặt thư viện underthesea
```
pip install underthesea
```

* Chạy chương trình
```
python main.py
```

## Cấu trúc thư mục
1. Thư mục **Input**: Các yêu cầu đầu vào của bài toán
    * `questions.txt`: Chứa danh sách các câu hỏi, mỗi câu nằm trên 1 dòng.
    * `database.txt`: Chứa cơ sở dữ liệu của các chuyến tàu hỏa.
2. Thư mục **Output**: Kết quả thực thi của mỗi câu hỏi
    * `output_a.txt`: Văn phạm phụ thuộc
    * `output_b.txt`: Quan hệ ngữ nghĩa
    * `output_c.txt`: Quan hệ văn phạm
    * `output_d.txt`: Dạng luận lý
    * `output_e.txt`: Ngữ nghĩa thủ tục
    * `output_f.txt`: Truy xuất dữ liệu
3. Thư mục **Models**: Các lớp phụ trợ để thực thi bài toán
    * `grammaticalRelation.py`: Chứa class tạo quan hệ ngữ nghĩa
    * `helper.py`: Chứa các hàm hỗ trợ
    * `logicalForm.py`: Chứa class tạo dạng luận lý
    * `maltParser.py`: Chứa class tạo văn phạm phụ thuộc dạng malt parser
    * `proceduralSemantics.py`: Chứa class tạo ngữ nghĩa thủ tục
    * `query.py`: Chứa class truy xuất dữ liệu
4. File `main.py`: Entry point của chương trình