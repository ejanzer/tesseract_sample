import pytesser
import model

# Testing out Tesseract on a couple of simple images with Chinese characters.
text = pytesser.image_file_to_string('shangwu.png', lang='chi_sim', graceful_errors=True)

# Chinese characters from Tesseract are encoded as UTF-8 and appear to have two trailing newlines.
shangwu = text.decode('utf-8').strip()
print shangwu

text = pytesser.image_file_to_string('taihaole.png', lang='chi_sim', graceful_errors=True)
print text
taihaole = text.decode('utf-8').strip()

# Connect to the CEDICT database and search for entries with these characters.
session = model.connect()
sw_entry = session.query(model.Entry).filter_by(simplified=shangwu).one()
thl_entry = session.query(model.Entry).filter_by(simplified=taihaole).one()

print sw_entry.definition
print thl_entry.definition