import tkinter as tk
from tkinter import ttk, messagebox
from collections import deque
from datetime import datetime

# --- Clase de Abstracción ---
class Afiliado:
    def __init__(self, id_type, id_number, full_name, income, service, emp_type, fee, date):
        self.id_type = id_type
        self.id_number = id_number
        self.full_name = full_name
        self.income = income
        self.service = service
        self.employment_type = emp_type
        self.affiliation_fee = fee
        self.affiliation_date = date

# --- Ventana de Login ---
class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Login - Compensándote")
        self.root.geometry("400x350")
        self.root.configure(bg="#1a2a3a")
        
        # Título
        tk.Label(root, text="Compensándote", font=("Arial", 20, "bold"), fg="#00bcd4", bg="#1a2a3a").pack(pady=30)
        tk.Label(root, text="Family Compensation Fund — Affiliation Control", font=("Arial", 9), fg="white", bg="#1a2a3a").pack()
        
        # Campo de contraseña
        tk.Label(root, text="Password:", font=("Arial", 11), fg="white", bg="#1a2a3a").pack(pady=(20, 5))
        self.password_entry = tk.Entry(root, show="*", font=("Arial", 12), width=25)
        self.password_entry.pack(pady=5)
        
        # Botones
        btn_style = {"font": ("Arial", 11), "width": 25}
        tk.Button(root, text="Login →", command=self.check_password, bg="#00bcd4", fg="white", **btn_style).pack(pady=10)
        tk.Button(root, text="About", command=self.show_about, bg="#5a6a7a", fg="white", **btn_style).pack(pady=5)
        tk.Button(root, text="Exit", command=root.quit, bg="#e53935", fg="white", **btn_style).pack(pady=5)

    def check_password(self):
        if self.password_entry.get() == "Caja":
            self.root.destroy()
            open_main_app()
        else:
            messagebox.showerror("Error", "Contraseña incorrecta. Intente de nuevo.")

    def show_about(self):
        info = ("Course: Data Structures — 301305\n"
                "Student: Hernando Arbey Robles Puentes\n"
                "Collaborative Group: 301305_1\n"
                "UNAD · ECBTI · Systems Engineering\n"
                f"Date: {datetime.now().strftime('%B %d, %Y')}")
        messagebox.showinfo("About", info)

# --- Ventana Principal ---
class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Caja Compensándote – Control de Afiliados")
        self.root.geometry("1100x650")

        # Estructuras de datos
        self.pila = []
        self.cola = deque()
        self.lista = []

        self.create_widgets()

    def create_widgets(self):
        # --- Frame del Formulario ---
        form_frame = tk.LabelFrame(self.root, text="Registro de Afiliado", padx=10, pady=10)
        form_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

        # Tipo ID
        tk.Label(form_frame, text="Tipo de Identificación:").grid(row=0, column=0, sticky="w", pady=3)
        self.id_type_cb = ttk.Combobox(form_frame, values=["CC", "CE", "NUIP", "PAS"], state="readonly")
        self.id_type_cb.grid(row=0, column=1, pady=3)

        # Número ID
        tk.Label(form_frame, text="Número de Identificación:").grid(row=1, column=0, sticky="w", pady=3)
        self.id_num_entry = tk.Entry(form_frame)
        self.id_num_entry.grid(row=1, column=1, pady=3)

        # Nombre
        tk.Label(form_frame, text="Nombre Completo:").grid(row=2, column=0, sticky="w", pady=3)
        self.name_entry = tk.Entry(form_frame)
        self.name_entry.grid(row=2, column=1, pady=3)

        # Ingresos
        tk.Label(form_frame, text="Ingresos Actuales:").grid(row=3, column=0, sticky="w", pady=3)
        self.income_entry = tk.Entry(form_frame)
        self.income_entry.grid(row=3, column=1, pady=3)

        # Servicio
        tk.Label(form_frame, text="Servicio Deseado:").grid(row=4, column=0, sticky="w", pady=3)
        servicios = ["Subsidio de desempleo", "Ingreso a parque", "Curso de formación", "Paquete de viaje", "Medicina preventiva"]
        self.service_cb = ttk.Combobox(form_frame, values=servicios, state="readonly")
        self.service_cb.grid(row=4, column=1, pady=3)

        # Modalidad
        tk.Label(form_frame, text="Modalidad de Empleo:").grid(row=5, column=0, sticky="w", pady=3)
        self.emp_var = tk.StringVar(value="Empleado")
        tk.Radiobutton(form_frame, text="Empleado", variable=self.emp_var, value="Empleado").grid(row=5, column=1, sticky="w")
        tk.Radiobutton(form_frame, text="Independiente", variable=self.emp_var, value="Independiente").grid(row=5, column=1, sticky="e")

        # Tarifa
        tk.Label(form_frame, text="Tarifa de Afiliación:").grid(row=6, column=0, sticky="w", pady=3)
        self.fee_entry = tk.Entry(form_frame, state="readonly")
        self.fee_entry.grid(row=6, column=1, pady=3)
        tk.Button(form_frame, text="Calcular Tarifa", command=self.calculate_fee, bg="#ffb74d").grid(row=7, column=0, columnspan=2, pady=5)

        # Fecha
        tk.Label(form_frame, text="Fecha de Afiliación:").grid(row=8, column=0, sticky="w", pady=3)
        self.date_entry = tk.Entry(form_frame)
        self.date_entry.insert(0, datetime.now().strftime("%d/%m/%Y"))
        self.date_entry.grid(row=8, column=1, pady=3)

        # Estructura
        tk.Label(form_frame, text="Seleccionar Estructura:").grid(row=9, column=0, sticky="w", pady=(15, 3))
        self.struct_var = tk.StringVar(value="Pila")
        ttk.Combobox(form_frame, textvariable=self.struct_var, values=["Pila", "Cola", "Lista"], state="readonly").grid(row=9, column=1, pady=(15, 3))

        # Botones
        btn_frame = tk.Frame(form_frame)
        btn_frame.grid(row=10, column=0, columnspan=2, pady=15)
        tk.Button(btn_frame, text="Registrar", command=self.register_affiliate, bg="#66bb6a", width=10).pack(side=tk.LEFT, padx=3)
        tk.Button(btn_frame, text="Limpiar", command=self.clear_form, bg="#ffd54f", width=10).pack(side=tk.LEFT, padx=3)
        tk.Button(btn_frame, text="Eliminar", command=self.delete_affiliate, bg="#ef5350", width=10).pack(side=tk.LEFT, padx=3)
        tk.Button(btn_frame, text="Salir", command=self.root.quit, bg="#b0bec5", width=10).pack(side=tk.LEFT, padx=3)

        # --- Frame del Treeview ---
        tree_frame = tk.Frame(self.root)
        tree_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        tk.Button(tree_frame, text="Mostrar Reporte", command=self.show_report, bg="#42a5f5", fg="white").pack(pady=5)

        columns = ("id", "name", "income", "service", "type", "fee", "date")
        self.tree = ttk.Treeview(tree_frame, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col.capitalize())
            self.tree.column(col, width=110)
        self.tree.pack(fill=tk.BOTH, expand=True)

        self.report_label = tk.Label(tree_frame, text="Reporte: $0.00", font=("Arial", 12, "bold"), fg="#1e88e5")
        self.report_label.pack(pady=10)

    def calculate_fee(self):
        try:
            income = float(self.income_entry.get())
            service = self.service_cb.get()
            emp_type = self.emp_var.get()

            base_fee = 0
            if emp_type == "Empleado":
                if 1000000 <= income <= 2000000: base_fee = 45000
                elif 2000000 < income <= 3000000: base_fee = 60000
                elif 3000000 < income <= 4000000: base_fee = 75000
                elif 4000000 < income <= 5000000: base_fee = 90000
                elif income > 5000000: base_fee = 150000
            else:
                if 1000000 <= income <= 2000000: base_fee = 10000
                elif 2000000 < income <= 3000000: base_fee = 20000
                elif 3000000 < income <= 4000000: base_fee = 30000
                elif 4000000 < income <= 5000000: base_fee = 40000
                elif income > 5000000: base_fee = 80000

            if service == "Ingreso a parque": base_fee += 2500
            elif service == "Curso de formación": base_fee += 7500
            elif service == "Paquete de viaje": base_fee += 10000
            elif service == "Medicina preventiva": base_fee += income * 0.10

            self.fee_entry.config(state="normal")
            self.fee_entry.delete(0, tk.END)
            self.fee_entry.insert(0, f"{base_fee:.2f}")
            self.fee_entry.config(state="readonly")

        except ValueError:
            messagebox.showerror("Error", "Los ingresos deben ser un número válido.")

    def register_affiliate(self):
        # Validaciones
        if not self.id_num_entry.get() or not self.name_entry.get() or not self.fee_entry.get():
            messagebox.showwarning("Campos vacíos", "Por favor complete todos los campos y calcule la tarifa.")
            return

        if not self.id_num_entry.get().isdigit():
            messagebox.showerror("Error", "El número de identificación debe contener solo números.")
            return

        if not self.name_entry.get().replace(" ", "").isalpha():
            messagebox.showerror("Error", "El nombre debe contener solo letras.")
            return

        nuevo = Afiliado(
            self.id_type_cb.get(), self.id_num_entry.get(), self.name_entry.get(),
            float(self.income_entry.get()), self.service_cb.get(), self.emp_var.get(),
            float(self.fee_entry.get()), self.date_entry.get()
        )

        estructura = self.struct_var.get()
        if estructura == "Pila": self.pila.append(nuevo)
        elif estructura == "Cola": self.cola.append(nuevo)
        else: self.lista.append(nuevo)

        self.update_treeview()
        messagebox.showinfo("Éxito", "Afiliado registrado correctamente.")

    def update_treeview(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        
        estructura = self.struct_var.get()
        datos = self.pila if estructura == "Pila" else (self.cola if estructura == "Cola" else self.lista)

        for a in datos:
            self.tree.insert("", tk.END, values=(
                a.id_number, a.full_name, a.income, a.service,
                a.employment_type, a.affiliation_fee, a.affiliation_date
            ))

    def delete_affiliate(self):
        estructura = self.struct_var.get()
        if estructura == "Pila":
            if not self.pila:
                messagebox.showwarning("Vacío", "La pila está vacía.")
                return
            if messagebox.askyesno("Confirmar", "¿Eliminar el último registro de la pila?"):
                self.pila.pop()
        elif estructura == "Cola":
            if not self.cola:
                messagebox.showwarning("Vacío", "La cola está vacía.")
                return
            if messagebox.askyesno("Confirmar", "¿Eliminar el primer registro de la cola?"):
                self.cola.popleft()
        else:
            id_buscar = simpledialog.askstring("Eliminar", "Ingrese el número de ID del afiliado a eliminar:")
            if id_buscar:
                encontrado = None
                for a in self.lista:
                    if a.id_number == id_buscar:
                        encontrado = a
                        break
                if encontrado:
                    if messagebox.askyesno("Confirmar", f"¿Eliminar a {encontrado.full_name}?"):
                        self.lista.remove(encontrado)
                else:
                    messagebox.showwarning("No encontrado", "No se encontró un afiliado con ese ID.")
        self.update_treeview()

    def show_report(self):
        estructura = self.struct_var.get()
        datos = self.pila if estructura == "Pila" else (self.cola if estructura == "Cola" else self.lista)
        total = sum(a.affiliation_fee for a in datos)
        self.report_label.config(text=f"Reporte ({estructura}): ${total:,.2f}")

    def clear_form(self):
        self.id_type_cb.set("")
        self.id_num_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.income_entry.delete(0, tk.END)
        self.service_cb.set("")
        self.emp_var.set("Empleado")
        self.fee_entry.config(state="normal")
        self.fee_entry.delete(0, tk.END)
        self.fee_entry.config(state="readonly")
        self.date_entry.delete(0, tk.END)
        self.date_entry.insert(0, datetime.now().strftime("%d/%m/%Y"))

def open_main_app():
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    login = LoginWindow(root)
    root.mainloop()