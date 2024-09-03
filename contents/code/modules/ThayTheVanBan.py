def ThayTheVanBan(text):
    # NOTE: Thay thế văn bản
    # text = text.replace
    # Microsof => Dịch vụ vi mô
    text = text.replace("[Tự động tạo]", "")
    text = text.replace("[Được tạo tự động]", "")
    text = text.replace("[Người hướng dẫn]", "")
    text = text.replace("\u202B", "")
     

    # !Thay thế văn bản
    while "  " in text:
        text = text.replace("  ", " ")
    return text.strip()