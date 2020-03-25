'''
Name: Zhengyang Zhao
Uniqname: zzyang
'''

import sqlite3 

def question0():
    ''' Constructs and executes SQL query to retrieve
    all fields from the Region table
    
    Parameters
    ----------
    None
    
    Returns
    -------
    list
        a list of tuples that represent the query result
    '''
    connection = sqlite3.connect("Northwind_small.sqlite")
    cursor = connection.cursor()
    query = "SELECT * FROM Region"
    result = cursor.execute(query).fetchall()
    connection.close()
    return result

def question1():
    ''' Constructs and executes SQL query to retrieve
    data based on requirements
    
    Parameters
    ----------
    None
    
    Returns
    -------
    list
        a list of tuples that represent the query result
    '''
    #TODO Implement function
    connection = sqlite3.connect("Northwind_small.sqlite")
    cursor = connection.cursor()
    query = "SELECT * FROM Territory"
    results = cursor.execute(query).fetchall()
    connection.close()
    return results

def question2():
    ''' Constructs and executes SQL query to retrieve
    data based on requirements
    
    Parameters
    ----------
    None
    
    Returns
    -------
    list
        a list of tuples that represent the query result
    '''
    #TODO Implement function
    connection = sqlite3.connect("Northwind_small.sqlite")
    cursor = connection.cursor()
    query = "SELECT count(Id) FROM Employee"
    result = cursor.execute(query).fetchall()
    connection.close()
    return result

def question3():
    ''' Constructs and executes SQL query to retrieve
    data based on requirements
    
    Parameters
    ----------
    None
    
    Returns
    -------
    list
        a list of tuples that represent the query result
    '''
    #TODO Implement function
    connection = sqlite3.connect("Northwind_small.sqlite")
    cursor = connection.cursor()
    query = "SELECT * FROM Product Order by Id DESC LIMIT 10"
    results = cursor.execute(query).fetchall()
    connection.close()
    return results

def question4():
    ''' Constructs and executes SQL query to retrieve
    data based on requirements
    
    Parameters
    ----------
    None
    
    Returns
    -------
    list
        a list of tuples that represent the query result
    '''
    #TODO Implement function 
    connection = sqlite3.connect("Northwind_small.sqlite")
    cursor = connection.cursor()
    query = "SELECT ProductName, UnitPrice FROM Product Order by UnitPrice DESC LIMIT 3"
    results = cursor.execute(query).fetchall()
    connection.close()
    return results

def question5():
    ''' Constructs and executes SQL query to retrieve
    data based on requirements
    
    Parameters
    ----------
    None
    
    Returns
    -------
    list
        a list of tuples that represent the query result
    '''
    #TODO Implement function
    connection = sqlite3.connect("Northwind_small.sqlite")
    cursor = connection.cursor()
    query = "SELECT ProductName, UnitPrice, UnitsInStock FROM Product WHERE UnitsInStock >= 60 AND UnitsInStock <= 100"
    results = cursor.execute(query).fetchall()
    connection.close()
    return results

def question6():
    ''' Constructs and executes SQL query to retrieve
    data based on requirements
    
    Parameters
    ----------
    None
    
    Returns
    -------
    list
        a list of tuples that represent the query result
    '''
    #TODO Implement function
    connection = sqlite3.connect("Northwind_small.sqlite")
    cursor = connection.cursor()
    query = "SELECT ProductName FROM Product WHERE UnitsInStock < ReorderLevel"
    results = cursor.execute(query).fetchall()
    connection.close()
    return results

def question7():
    ''' Constructs and executes SQL query to retrieve
    data based on requirements
    
    Parameters
    ----------
    None
    
    Returns
    -------
    list
        a list of tuples that represent the query result
    '''
    #TODO Implement function
    connection = sqlite3.connect("Northwind_small.sqlite")
    cursor = connection.cursor()
    query = "SELECT Id FROM [Order] WHERE ShipCountry = 'France' AND ShipPostalCode like '%04'"
    results = cursor.execute(query).fetchall()
    connection.close()
    return results

def question8():
    ''' Constructs and executes SQL query to retrieve
    data based on requirements
    
    Parameters
    ----------
    None
    
    Returns
    -------
    list
        a list of tuples that represent the query result
    '''
    #TODO Implement function
    connection = sqlite3.connect("Northwind_small.sqlite")
    cursor = connection.cursor()
    query = "SELECT CompanyName, ContactName FROM Customer WHERE Country = 'UK' AND Fax is NOT NULL"
    results = cursor.execute(query).fetchall()
    connection.close()
    return results

def question9():
    ''' Constructs and executes SQL query to retrieve
    data based on requirements
    
    Parameters
    ----------
    None
    
    Returns
    -------
    list
        a list of tuples that represent the query result
    '''
    #TODO Implement function
    connection = sqlite3.connect("Northwind_small.sqlite")
    cursor = connection.cursor()
    query = "SELECT ProductName, UnitPrice FROM Product JOIN Category on Product.CategoryId = Category.Id WHERE CategoryName = 'Beverages'"
    results = cursor.execute(query).fetchall()
    connection.close()
    return results

def question10():
    ''' Constructs and executes SQL query to retrieve
    data based on requirements
    
    Parameters
    ----------
    None
    
    Returns
    -------
    list
        a list of tuples that represent the query result
    '''
    #TODO Implement function
    connection = sqlite3.connect("Northwind_small.sqlite")
    cursor = connection.cursor()
    query = "SELECT ProductName FROM Product JOIN Category on Product.CategoryId = Category.Id WHERE CategoryName = 'Meat/Poultry' AND Discontinued = 1"
    results = cursor.execute(query).fetchall()
    connection.close()
    return results

def question11():
    ''' Constructs and executes SQL query to retrieve
    data based on requirements
    
    Parameters
    ----------
    None
    
    Returns
    -------
    list
        a list of tuples that represent the query result
    '''
    #TODO Implement function
    connection = sqlite3.connect("Northwind_small.sqlite")
    cursor = connection.cursor()
    query = "SELECT [Order].Id, Employee.FirstName, Employee.LastName FROM [Order] JOIN Employee on [Order].EmployeeId = Employee.Id WHERE ShipCountry = 'Germany'"
    results = cursor.execute(query).fetchall()
    connection.close()
    return results

def question12():
    ''' Constructs and executes SQL query to retrieve
    data based on requirements
    
    Parameters
    ----------
    None
    
    Returns
    -------
    list
        a list of tuples that represent the query result
    '''
    #TODO Implement function
    connection = sqlite3.connect("Northwind_small.sqlite")
    cursor = connection.cursor()
    query = "SELECT [Order].Id, [Order].OrderDate, Customer.CompanyName FROM [Order] JOIN Customer on [Order].CustomerId = Customer.Id WHERE OrderDate <= '2012-07-10'"
    results = cursor.execute(query).fetchall()
    connection.close()
    return results



#################################################################
########################  ECs start here  #######################
#################################################################

#########
## EC1 ##
#########

def print_query_result(raw_query_result):
    ''' Pretty prints raw query result
    
    Parameters
    ----------
    list 
        a list of tuples that represent raw query result
    
    Returns
    -------
    None
    '''
    #TODO Implement function
    field_num = len(raw_query_result[0])
    i = 0
    border = '+'
    for i in range(field_num):
        border += '-' * 20 + '+'
    print(border)
    separator = '|'

    for row in raw_query_result:
        row_str = separator
        for item in row:    
            # print(type(item))
            if len(str(item)) > 15:
                item = f" {str(item)[:15]}... "
            else:
                space_num = int((20-len(str(item)))/2)
                space = ' ' * space_num
                if len(str(item)) % 2 == 0:
                    item = f"{space}{item}{space}"
                else:
                    item = f"{space}{item}{space} "
            row_str += item + separator
        print(row_str)

    print(border)

if __name__ == "__main__":
    '''WHEN SUBMIT, UNCOMMENT THE TWO LINES OF CODE
    BELOW IF YOU COMPLETED EC1'''

    result = question9()
    print_query_result(result)

#########
## EC2 ##
#########
    
    #TODO Implement interactive program here
    while True:
        inputs = input(f"Please enter a Order Date and a Ship Country seperated by space (e.g. 2010-07-04 France), or 'exit' to quit: ")
        if inputs == 'exit':
            break
        else:
            if ' ' in inputs:
                order_date = inputs[:10]
                ship_country = inputs[11:]

                connection = sqlite3.connect("Northwind_small.sqlite")
                cursor = connection.cursor()
                query = f"SELECT Employee.FirstName, Employee.LastName FROM [Order] JOIN Employee on [Order].EmployeeId = Employee.Id WHERE OrderDate = '{order_date}' AND ShipCountry = '{ship_country}'"
                results = cursor.execute(query).fetchall()
                connection.close()
                if len(results) == 0:
                    print("Sorry! Your search returns no results.")
                    print()
                else:
                    print_query_result(results)
                    print()
            else:
                print("Invalid Input. Please enter a Order Date and a Ship Country sepearted by space")
                print()