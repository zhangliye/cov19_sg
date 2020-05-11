import camelot

DATE_NAMES = ['4-11']

for DATE_NAME in DATE_NAMES:
    ## extract data to json from pdf 
    f = r'/mnt/c/temp/%s.pdf' % DATE_NAME
    tables = camelot.read_pdf(f, pages='all')

    print( tables[0].data[0] )
    row_names = tables[0].data[0]

    data = {}
    for i in range(len(row_names)):
        data[i] = []

    for i in range(len(tables)):
        for r in tables[i].data[1:]:
            if len(r) != len(row_names):
                print("wrong row: ", r)
            else:
                for j in range(len(r)):
                    data[j].append(r[j])

    # change column names
    data_new = {}
    for i in range(len(row_names)):
        k = row_names[i]
        new_k = k.replace(' ', '_').replace('\n', '').strip()
        data_new[new_k] = data[i]

    import json
    json_file = r'/mnt/c/temp/%s.json' % DATE_NAME
    with open(json_file, 'w') as f:
        json.dump(data_new, f)
    print("saved to: ", json_file)

