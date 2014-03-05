import pytesser

text = pytesser.image_file_to_string('shangwu.png', lang='chi_sim', graceful_errors=True)
print text
text = pytesser.image_file_to_string('taihaole.png', lang='chi_sim', graceful_errors=True)
print text

