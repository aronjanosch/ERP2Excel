import DataRequest
import pandas as pd
from openpyxl import load_workbook
from datetime import datetime

columns = [
        "creation",
        "customer_group",
        "customer_name",
        "contact_display",
        "lieferdatum",
        "modified_by",
        "name",
        "owner",
        "pax",
        "sache",
        "angebotstyp",
        "shipping_address",
        "title",
        "total",
        "transaction_date",
        "lieferdatum",
        "uhrzeit",
        "standby",
        "menüart",
        "contact_mobile",
               ]


def get_items(qid):

    data = DataRequest.get_data('Quotation', qid)
    if data.status_code != 200:
        return data.status_code
    data = data.json()['data']
    df1 = pd.DataFrame.from_dict(data, orient='index')
    df1 = df1.transpose()
    df1 = df1.reindex(columns=columns)
    item_data = [
        [pd.DataFrame(data['items']), 'items']
        ,[pd.DataFrame(data['drinks']), 'drinks']
        ,[pd.DataFrame(data['personal_items']), 'personal_items']
        ,[pd.DataFrame(data['hardware_items']), 'hardware_items']
                ]

    return item_data, df1


def write_xlsx(input_path, output_path, item_data, df1):

    book = load_workbook(input_path)
    writer = pd.ExcelWriter(output_path, engine='openpyxl')
    writer.book = book
    writer.sheets = dict((ws.title, ws) for ws in book.worksheets)

    for i in item_data:
        try:
            i[0] = i[0][['item_name', 'qty', 'amount', 'item_group']]
        except:
            continue

    item_data.insert(0,[df1,'infos'])

    for i in item_data:
        i[0].to_excel(writer, sheet_name=i[1])

    writer.save()


