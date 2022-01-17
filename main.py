import time
from Dt_extractor import Extractor
from cutter import Parser

URL = "https://swapi.dev/api/people/?page={}"


start = time.perf_counter()
with Extractor(URL) as ex:
    # ex.test_connection()
    my_data = ex.extract_all_data()
my_data = [item for page in my_data for item in page["results"]]
parser = Parser(my_data)
parameters = ("name", "species")
required_data = parser.return_columns(*parameters)
end = time.perf_counter()
print(required_data, f"Total amount of people in StarWars is {len(required_data)}")
print(f"Finished in {round(end - start, 2)} second(s)")
