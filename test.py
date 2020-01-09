import XlsWriter
import DataModifier

qid = "AG-201912-001"

ipath = "/Users/aronwiederkehr/Desktop/TheFile.xlsx"
opath = "/Users/aronwiederkehr/Desktop/test.xlsx"

modes = {
            0: "0: Full Test",
            1: "1: Test Address"
        }


def test_address():
    result = get_data()[1]['shipping_address'][0]
    rs = DataModifier.get_address(result)
    print(rs)


def get_data():
    result = XlsWriter.get_items(qid)
    return result


def full_test():
    result = get_data()
    if type(result) == int:
        print("Error {res}".format(res=result))
    else:
        XlsWriter.write_xlsx(ipath, opath, result[0], result[1])
        print("Success")
    print("xlsx created")


while True:
    for i in modes:
        print(modes[i])
    inp = int(input("Select one of these options: "))
    if inp == 0:
        full_test()
        break
    if inp == 1:
        test_address()
        break
    else:
        continue
