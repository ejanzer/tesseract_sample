import model
import csv

def load_dict(session):
    with open('cedict.txt', 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0][0] == '#':
                continue
            else:
                def_tokens = row[0].split('/')
                if len(def_tokens) > 1:
                    definition = ' '.join(def_tokens[1:]).decode('utf-8')
                else:
                    definition = ""

                entry_tokens = def_tokens[0].split(' ')
                if len(entry_tokens) > 2:
                    simp = entry_tokens[0].decode('utf-8')
                    trad = entry_tokens[1].decode('utf-8')
                    pinyin = entry_tokens[2].strip('[]')
                else: 
                    print "There aren't enough tokens in this entry!", row

                entry = model.Entry(simplified=simp, traditional=trad, pinyin=pinyin, definition=definition)
                session.add(entry)

            session.commit()

def main(session):
    load_dict(session)

if __name__ == "__main__":
    session = model.connect()
    main(session)



