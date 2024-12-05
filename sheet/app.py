import time
from sheets_helper import extract_spreadsheet_id, read_google_sheet

# Hàm kiểm tra xem dòng có đủ giá trị không
def is_row_complete(row, required_columns_count):
    # Kiểm tra nếu số lượng cột trong dòng bằng với số cột trong header
    if len(row) != required_columns_count:
        return False
    # Kiểm tra nếu tất cả các ô trong dòng đều có giá trị
    return all(cell != "" for cell in row)

# Nhập URL Google Sheet
spreadsheet_url = "https://docs.google.com/spreadsheets/d/1G9eqfrxXIMOxKL7ft5upzL-XG6x6vKshe1soaQSr34M/edit?usp=sharing"

# Lấy ID của Google Sheet từ URL
spreadsheet_id = extract_spreadsheet_id(spreadsheet_url)

# Cập nhật phạm vi dữ liệu cần đọc (ví dụ: Sheet1!A1:Z)
range_name = "Sheet1!A1:Z"  # Bạn có thể thay đổi phạm vi này tùy theo dữ liệu của mình


# Hàm chính để kiểm tra và in dữ liệu
def check_and_print_new_rows():
    # Đọc dữ liệu từ Google Sheet
    data = read_google_sheet(spreadsheet_id, range_name)

    # Lấy dòng đầu tiên làm tham chiếu để xác định số cột cần có
    header_row = data[0]  # Dòng đầu tiên
    required_columns_count = len(header_row)  # Số cột trong dòng đầu tiên

    # Kiểm tra từng dòng dưới header
    for row in data[1:]:  # Bỏ qua dòng đầu tiên (header)

        # Nếu dòng chưa được kiểm tra và đã đầy đủ giá trị
        if is_row_complete(row, required_columns_count) and row[4] == "0":
            # In dòng ra terminal
            print("Dòng mới đầy đủ giá trị từ Google Sheet:")
            print(row)

while True:
    check_and_print_new_rows()
