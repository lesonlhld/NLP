# Bài tập lớn xử lý ngôn ngữ tự nhiên HK211

## Thông tin chương trình:
1. Ngôn ngữ: Python
2. Hỗ trợ các câu hỏi dạng như:
    * Tàu hỏa nào đến thành phố Huế lúc 19:00HR ?
    * Thời gian tàu hỏa B3 chạy từ Đà Nẵng đến TP. Hồ Chí Minh là mấy giờ?
    * Tàu hỏa nào đến thành phố Hồ Chí Minh ?
    * Tàu hỏa nào chạy từ Hà Nội, lúc mấy giờ
    * Tàu hỏa nào chạy từ TP.Hồ Chí Minh đến Hà Nội ?
    * Tàu hỏa B5 có chạy từ Đà Nẵng không ?
    * Tàu hỏa B3 chạy từ Đà Nẵng lúc mấy giờ ?
    * Tàu hỏa B2 có chạy từ Hà Nội không ?
    * Tàu hỏa B5 chạy từ đâu ?
    * Tàu hỏa B5 chạy đến đâu ?
    * Tàu hỏa B5 chạy từ đâu đến đâu ?

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
    * `parser.py`: Chứa class tạo văn phạm phụ thuộc dạng malt parser
    * `proceduralSemantics.py`: Chứa class tạo ngữ nghĩa thủ tục
    * `query.py`: Chứa class truy xuất dữ liệu
4. File `main.py`: Entry point của chương trình

## Tài liệu tham khảo
1. [THƯ VIỆN TỰ HỌC DEEP LEARNING NATURAL LANGUAGE PROCESSING (NLP)](https://hoctructuyen123.net/thu-vien-tu-hoc-deep-learning-natural-language-processing-nlp/)
2. [Underthesea là gì?](https://github-wiki-see.page/m/undertheseanlp/underthesea/wiki/Câu-chuyện-của-underthesea)
3. [Open-source Vietnamese Natural Language Process Toolkit](https://github.com/undertheseanlp/underthesea)