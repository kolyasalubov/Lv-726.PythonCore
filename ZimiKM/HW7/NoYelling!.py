def filter_words (st):
    split_list = st.split()
    for element in split_list:
        element = element.strip()
    result = ' '.join(split_list)
    return result.capitalize()
print(filter_words('WOW this is REALLY          amazing'))

