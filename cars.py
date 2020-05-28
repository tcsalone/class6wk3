#!/usr/bin/env python3

import json
import locale
import sys

def load_data(filename):
  """Loads the contents of filename as a JSON file."""
  with open(filename) as json_file:
    data = json.load(json_file)
  return data


def format_car(car):
  """Given a car dictionary, returns a nicely formatted name."""
  return "{} {} ({})".format(
      car["car_make"], car["car_model"], car["car_year"])


def process_data(data):
  """Analyzes the data, looking for maximums.

  Returns a list of lines that summarize the information.
  """
  locale.setlocale(locale.LC_ALL, 'en_US.UTF8')
  max_revenue = {"revenue": 0}
  max_sales_car = {"total": 0}
  max_sales = 0
  year_dic = {}
  for item in data:
    # Calculate the revenue generated by this model (price * total_sales)
    # We need to convert the price from "$1234.56" to 1234.56
    item_price = locale.atof(item["price"].strip("$"))
    item_revenue = item["total_sales"] * item_price
    
    if item_revenue > max_revenue["revenue"]:
      item["revenue"] = item_revenue
      max_revenue = item
    
    # TODO: also handle max sales
    item_sales = item["total_sales"]
    if max_sales < item["total_sales"]:
       max_sales = item["total_sales"]
       max_sales_car = item
       print(max_sales)

    # TODO: also handle most popular car_year
   # print(item)
   # print(item["car"]["car_year"])
    if not (item["car"]["car_year"]) in year_dic:
      year_dic[item["car"]["car_year"]] = 1
    else:
      year_dic[item["car"]["car_year"]] +=1
    most_sales = max(year_dic, key=year_dic.get)
    best_year = max(year_dic)
    print(best_year)
    #print(type(most_sales))
    print(year_dic)
    #print(max(year_dic, key=year_dic.get))

  summary = [
    "The {} generated the most revenue: ${}".format(
      format_car(max_revenue["car"]), max_revenue["revenue"]),
    [
    "The {} had the most sales: {}".format(
      format_car(max_sales_car["car"]), max_sales_car["total_sales"]),
   
    "The most popular year was {} with {} sales.".format(
     most_sales, best_year)
    ]
  ]
  return summary


def cars_dict_to_table(car_data):
  """Turns the data in car_data into a list of lists."""
  table_data = [["ID", "Car", "Price", "Total Sales"]]
  for item in car_data:
    table_data.append([item["id"], format_car(item["car"]), item["price"], item["total_sales"]])
  return table_data


def main(argv):
  """Process the JSON data and generate a full report out of it."""
  data = load_data("car_sales.json")
  summary = process_data(data)
  print(summary)
  # TODO: turn this into a PDF report

  # TODO: send the PDF report as an email attachment


if __name__ == "__main__":
  main(sys.argv)
