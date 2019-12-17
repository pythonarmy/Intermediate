import sys
from datetime import datetime as dt

def get_time(date):
    dtime = dt.strptime(date.strip(), '%a %d %b %Y %H:%M:%S %z')
    return dtime.timestamp()
def get_delta(date1, date2):
    date1, date2 = map(get_time, (date1, date2))
    return int(date1 - date2)
def main(input_file=sys.stdin, outfile=sys.stdout):
    T = int(input_file.readline().strip())
    for _ in range(T):
        t1 = input_file.readline().strip()
        t2 = input_file.readline().strip()
        delta = get_delta(t1, t2)
        outfile.write(f"{delta}\n")
        outfile.flush()
def test_case(test_input, expected_output):
    from io import StringIO
    test_file = StringIO(test_input)
    test_output = StringIO()
    main(test_file, test_output)
    test_output.seek(0)
    output = test_output.read()
    assert  output == expected_output, f"output should be: \n{expected_output}"
    return output

def test_example_case():
    test_input = """
2
Sun 10 May 2015 13:54:36 -0700
Sun 10 May 2015 13:54:36 -0000
Sat 02 May 2015 19:54:36 +0530
Fri 01 May 2015 13:54:36 -0000
""".strip()
    expected_output = "25200\n88200\n"
    output = test_case(test_input, expected_output)
    print(output)


if __name__=='__main__':
    #test_example_case()
    main()
