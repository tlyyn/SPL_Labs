class DataPreprocessor:
    def __init__(self, data):
        self.data = data

    def filter_data(self, product=None, region=None):
        filtered_data = self.data
        if product:
            filtered_data = filtered_data[filtered_data['Product'] == product]
        if region:
            filtered_data = filtered_data[filtered_data['Region'] == region]
        return filtered_data

    def aggregate_sales_by_month(self):
        return self.data.groupby('Month')['Sales'].sum()
