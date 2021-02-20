import json


class NameFinder:

    def __init__(self, file, counter=0):
        self.file = file
        self.counter = counter

    def __iter__(self):
        return self

    def __next__(self):
        with open(self.file, encoding='utf-8') as f_countries:
            data = json.load(f_countries)
            end = len(data)
            name_country = data[self.counter]["name"]["common"]
            # print(name_country)
            new_country_name = name_country.replace(" ", "_")
            print(new_country_name)
            wiki_link = "https://en.wikipedia.org/wiki/" + new_country_name
            print(wiki_link)
            with open('output.txt', 'a', encoding='utf-8') as f_output:
                f_output.write(f'{name_country} - {wiki_link}')
                f_output.write("\n")
        self.counter += 1
        if self.counter == end:
            raise StopIteration
        return self.counter


if __name__ == '__main__':
    for i in NameFinder('countries.json'):
        print("")
