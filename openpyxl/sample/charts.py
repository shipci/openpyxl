"""Simple test charts"""
from datetime import date
import os
from openpyxl import Workbook
from openpyxl.charts import Chart, Series, Reference, BarChart, PieChart, LineChart, ScatterChart


def numbers(wb):
    ws = wb.create_sheet(1, "Numbers")
    for i in range(10):
        ws.append([i])
    chart = BarChart()
    values = Reference(ws, (0, 0), (9, 0))
    series = Series(values)
    chart.append(series)
    ws.add_chart(chart)

def negative(wb):
    ws = wb.create_sheet(1, "Negative")
    for i in range(-5, 5):
        ws.append([i])
    chart = BarChart()
    values = Reference(ws, (0, 0), (9, 0))
    series = Series(values)
    chart.append(series)
    ws.add_chart(chart)

def letters(wb):
    ws = wb.create_sheet(2, "Letters")
    for idx, l in enumerate("ABCDEFGHIJ"):
        ws.append([l, idx, idx])
    chart = BarChart()
    labels = Reference(ws, (0, 0), (9, 0))
    values = Reference(ws, (0, 1), (9, 1))
    series = Series(values, labels=labels)
    chart.append(series)
    #  add second series
    values = Reference(ws, (0, 2), (9, 2))
    series = Series(values, labels=labels)
    chart.append(series)
    ws.add_chart(chart)

def dates(wb):
    ws = wb.create_sheet(3, "Dates")
    for i in range(1, 10):
        ws.append([date(2013, i, 1), i])
    chart = BarChart()
    values = Reference(ws, (0, 1), (8, 1))
    labels = Reference(ws, (0, 0), (8, 0))
    labels.number_format = 'd-mmm'
    series = Series(values, labels=labels)
    chart.append(series)
    ws.add_chart(chart)

def pie(wb):
    ws = wb.create_sheet(4, "Pie")
    for i in range(1, 5):
        ws.append([i])
    chart = PieChart()
    values = Reference(ws, (0, 0), (3, 0))
    series = Series(values, labels=values)
    chart.append(series)
    ws.add_chart(chart)

def line(wb):
    ws = wb.create_sheet(5, "Line")
    for i in range(1, 5):
        ws.append([i])
    chart = LineChart()
    values = Reference(ws, (0, 0), (3,0))
    series = Series(values)
    chart.append(series)
    ws.add_chart(chart)

def scatter(wb):
    ws = wb.create_sheet(6, "Scatter")
    for i in range(10):
        ws.append([i, i])
    chart = ScatterChart()
    xvalues = Reference(ws, (0, 1), (9, 1))
    values = Reference(ws, (0, 0), (9, 0))
    series = Series(values, xvalues=xvalues)
    chart.append(series)
    ws.add_chart(chart)

if __name__ == "__main__":
    wb = Workbook()
    ws = wb.get_active_sheet()
    wb.remove_sheet(ws)
    numbers(wb)
    negative(wb)
    letters(wb)
    dates(wb)
    pie(wb)
    line(wb)
    scatter(wb)

    folder = os.path.split(__file__)[0]
    wb.save(os.path.join(folder, "files", "charts.xlsx"))
