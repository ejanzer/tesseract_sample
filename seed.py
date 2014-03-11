import model
import csv

def load_dict(session):
    with open('cedict3.csv', 'rb') as f:
        reader = csv.reader(f, delimiter=',', quotechar='"')
        for row in reader:
            if row[0] == '#':
                continue
            else:
                for i in range(len(row)):
                    row[i] = row[i].decode('utf-8')

                trad, simp, pinyin = row[0], row[1], row[2]
                definition = ''.join(row[3:])
                pinyin = pinyin.strip('"')
                definition = definition.strip('"')

                entry = model.Entry(simplified=simp, traditional=trad, pinyin=pinyin, definition=definition)
                session.add(entry)

        try: 
            session.commit()
        except sqlalchemy.exc.IntegrityError, e:
            session.rollback()

def main(session):
    load_dict(session)

if __name__ == "__main__":
    session = model.connect()
    main(session)



