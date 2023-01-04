import xml.etree.ElementTree as ET


class TemperatureConverter:
    def convert_celsius_to_fahrenheit(self, value):
        result = 9/5 * value + 32
        return result
        

class ForecaseXmlParser:
    def __init__(self):
        self.converter = TemperatureConverter()
        
    def parse(self):
        tree = ET.parse('forecast.xml')
        for item in tree.getroot():
            converted_value = self.converter.convert_celsius_to_fahrenheit(
                float(item[1].text)
            )
            print(
                item[0].text, f'{float(item[1].text)} Celsius,', f'{converted_value}'
            )
        

if __name__ == '__main__':
    ForecaseXmlParser().parse()
