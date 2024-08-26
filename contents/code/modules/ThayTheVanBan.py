def ThayTheVanBan(text):
    # NOTE: Thay thế văn bản
    # text = text.replace
    # Microsof => Dịch vụ vi mô
    text = text.replace("[Tự động tạo]", "")
    text = text.replace("\u202B", "")
    text = text.replace('\u202B', '')

    # !Thay thế văn bản
    while "  " in text:
        text = text.replace("  ", " ")
    return text
