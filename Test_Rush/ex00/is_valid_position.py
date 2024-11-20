def is_valid_position(x, y, size):
    """
    Parameters
        x (int) แนวนอน
        y (int) แนวตั้ง
        size (int) บอร์ดSize Line 18
    Returns
        bool (T,F) เช็คตามเงื่อนไข 0 -- sz - 1 ค้องไม่ต่ำกว่า 0 และก็ต้องไม่เกิน ขอบ sz ของบอร์ด
    """
    # ตรวจสอบว่า x อยู่ในขอบเขตของกระดาน (0 ถึง (size-1))
    x_inside_area = (x >= 0) and (x < size)
    # ตรวจสอบว่า y อยู่ในขอบเขตของกระดาน (0 ถึง (size-1))
    y_inside_area = (y >= 0) and (y < size)
    
    # ถ้า x และ y อยู่ในขอบเขตทั้งสองด้าน ให้คืนค่า True
    return x_inside_area and y_inside_area

size = 8  # 8x8

#TEST CASE
print(is_valid_position(3, 4, size))  # True 
print(is_valid_position(-1, 5, size)) # False x นอก
print(is_valid_position(8, 2, size))  # False x เกิน
print(is_valid_position(4, 8, size))  # False y เกิน