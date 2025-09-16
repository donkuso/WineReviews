# adds csv package (used for file i/o)
import csv

class Finder:
    def __init__(self):
        self.wine_list = [] 
    
    def get_field(self, row, field_name):
        # helper to find a value in row
        for k in row:
            if k is None:
                continue
            if k.strip().lower() == field_name.lower():
                return row[k]
        return ""
    
    def read(self, filepath):
    """
    prints each line in the file provided in param
    filepath: str representing the path to the file to read in
    returns: nothing.  
    """
    
    # with block
    # handles opening and closing of file automatically. 
    # file is only open in indented block.
        with open(filepath, newline='', mode='r', encoding='utf-8-sig') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                id = self.get_field(row, "id")
                country = self.get_field(row, "country")
                description = self.get_field(row, "description")
                designation = self.get_field(row, "designation")
                points = self.get_field(row, "points")
                price = self.get_field(row, "price")
                province = self.get_field(row, "province")
                region_1 = self.get_field(row, "region_1")
                region_2 = self.get_field(row, "region_2")
                variety = self.get_field(row, "variety")
                winery = self.get_field(row, "winery")

                if id is None:
                    id = ""
                id = id.strip() if isinstance(id, str) else id
                if id == "":
                    id = 0

                if country is None:
                    country = ""
                country = country.strip()

                if description is None:
                    description = ""
                description = description.strip()

                if designation is None:
                    designation = ""
                designation = designation.strip()

                if points is None:
                    points = ""
                points = points.strip() if isinstance(points, str) else points
                if points == "":
                    points = 0

                if price is None:
                    price = ""
                price = price.strip() if isinstance(price, str) else price
                if price == "":
                    price = 0

                if province is None:
                    province = ""
                province = province.strip()

                if region_1 is None:
                    region_1 = ""
                region_1 = region_1.strip()

                if region_2 is None:
                    region_2 = ""
                region_2 = region_2.strip()

                if variety is None:
                    variety = ""
                variety = variety.strip()

                if winery is None:
                    winery = ""
                winery = winery.strip()
                
                r = Review(ID=id, country=country, description=description, designation=designation, points=points, price=price, province=province, region_1=region_1, region_2=region_2, variety=variety, winery=winery)
                self.wine_list.append(r)
            

    def average_price(self):
        total = 0.0
        count = 0
        for w in self.wine_list:
            total += float(w.price)
            count += 1
        if count == 0:
            return 0.0
        return total / count
    
    def ten_by_province_region(self, prov, reg):
        
