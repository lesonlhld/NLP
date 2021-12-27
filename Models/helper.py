token_types = {
    'train': ['tàu_hỏa', 'Tàu_hỏa', 'tàu'],
    'run': ['chạy'],
    'city': ['thành_phố', 'Thành_phố', 'TP', 'Tp'],
    'arrive': ['đến', 'tới'],
    'from': ['từ'],
    'which': ['nào', 'mấy_giờ'],
    'where': ['đâu'],
    'yesno': ['không'],
    'time': ['lúc', 'vào_lúc', 'từ_lúc', 'Thời_gian', 'thời_gian'],
    'name': ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'HUE', 'HCM', 'HCMC', 'HN', 'DANANG', 'Hồ_Chí_Minh', 'Hà_Nội', 'Huế', 'Đà_Nẵng', 'Nha_Trang', 'NTrang'],
    'hour': ['hour'],
}

def getType(token):
    for token_type in token_types:
        if token in token_types[token_type]:
            return token_type
    if token.find("HR") != -1:
        return 'hour'
    if token == '<ROOT>':
        return token
    return '<UNKNOWN>'