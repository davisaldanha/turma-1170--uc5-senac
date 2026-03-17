import tkinter as tk
from tkinter import ttk
import csv

def read_csv(filename):
    '''Retorna as linhas do arquivo csv passado por parâmetro.'''
    rows = []

    with open(filename, newline='') as file:
        reader = csv.DictReader(file)

        for row in reader:
            rows.append(row)
    
    return rows

def prepare_tree_data(rows, icon_male, icon_female):
    '''Retorna um dicionário com os dados agrupados por cidade'''
    grouped_data = {}

    for row in rows:
        if row['Gender'] == 'Male':
            row['Icon'] = icon_male
        else:
            row['Icon'] = icon_female
    
        city = row['City']
        if city not in grouped_data:
            grouped_data[city] = []
        grouped_data[city].append(row)
    
    return grouped_data

def format_currency(value):
    try:
        return f"${int(value):,}"
    except ValueError:
        return value

def create_tree_view(root, employees, icons):
    
    frame = ttk.Frame(root)

    treeview = ttk.Treeview(frame, columns=("Salary", "Bonus"))

    treeview.heading('#0', text="Employee")
    treeview.heading('Salary', text='Salary')
    treeview.heading('Bonus', text='Bonus')

    employees_data = prepare_tree_data(employees, icons['female'], icons['male'])

    for city in employees_data.keys():
        #Adicionar cidade
        city_id = treeview.insert('', tk.END, text=city, image=icons['city'])

        #Adicionar os empregados da cidade
        for employee in employees_data[city]:
            treeview.insert(
                city_id,
                tk.END,
                text=employee['First Name'] + ' ' + employee['Last Name'],
                values=(format_currency(employee['Salary']), format_currency(employee['Bonus'])),
                image=employee['Icon']
            )
    
    # Criando um objeto scrollbar e associando a treeview
    v_scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=treeview.yview)
    treeview.configure(yscrollcommand=v_scrollbar.set)

    # Empacotando a treeview e o scrollbar
    treeview.pack(fill=tk.BOTH, side=tk.LEFT)
    v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Empacotando o frmae
    frame.pack(padx=10, pady=10, fill='both', expand=True)

def main():

    root = tk.Tk()
    root.title('Lista de Empregados')
    root.state('zoomed')

    ICON_CITY = './assets/city.png'
    ICON_MALE = './assets/male.png'
    ICON_FEMALE = './assets/female.png'
    PATH_CSV = './archives/employees.csv'

    icons = {
        'city': tk.PhotoImage(file=ICON_CITY),
        'male': tk.PhotoImage(file=ICON_MALE),
        'female': tk.PhotoImage(file=ICON_FEMALE)
    }
    employees = read_csv(PATH_CSV)

    create_tree_view(root, employees, icons)


    root.mainloop()

if __name__ == "__main__":
    main()


