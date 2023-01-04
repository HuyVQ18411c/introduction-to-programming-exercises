import xml.etree.ElementTree as ET


products_data = [
    {
        'attributes': {'name': 'Good Morning Sunshine'},
        'type': 'cereals',
        'producer': 'OpenEDG Testing Service',
        'price': 9.90,
        'currency': 'USD'
    },
    {
        'attributes': {'name': 'Spaghetti Veganietto'},
        'type': 'pasta',
        'producer': 'Programmers Eat Pasta',
        'price': 15.49,
        'currency': 'EUR'
    },
    {
        'attributes': {'name': 'Fantastic Almond Milk'},
        'type': 'beverages',
        'producer': 'Drinks4Coders Inc.',
        'price': 19.75,
        'currency': 'USD'
    }
]

root = ET.Element('shop')

category = ET.SubElement(root, 'category')

for product in products_data:
    attributes = product.pop('attributes')
    product_ele = ET.SubElement(category, 'product', attributes)

    for ele in product.keys():
        element = ET.SubElement(product_ele, ele)
        element.text = str(product[ele])

tree = ET.ElementTree(root)
tree.write('shop.xml')