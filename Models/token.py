import re

token_types = {
    'train': ['train', 'tàu_hỏa', 'Tàu_hỏa'],
    'city': ['city', 'thành_phố', 'Thành_phố', 'TP', 'Tp'],
    'arrive': ['đến', 'tới'],
    'from': ['từ', 'từ_lúc'],
    'which': ['nào'],
    'atime': ['lúc', 'vào_lúc'],
    'dtime': ['lúc'],
    'name': ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'HUE', 'HCM', 'HCMC', 'HN', 'DANANG', 'Hồ_Chí_Minh', 'Hà_Nội', 'Huế', 'Đà_Nẵng', 'Nha_Trang', 'NTrang'],
    'runtime': ['Thời_gian', 'thời_gian'],
    'time': ['time'],
}

def token_type(token):
    for token_type in token_types:
        if token in token_types[token_type]:
            return token_type
    if re.search('\d{3,4}HR', token):
        return 'time'
    if token == '<ROOT>':
        return token
    return '<UNKNOWN>'