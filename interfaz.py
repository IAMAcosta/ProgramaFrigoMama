# interfaz.py

import tkinter as tk
from tkinter import ttk, messagebox
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from Frigo import Carne, Cliente, Ciudad, Provincia, crear_remito, cortes_carne

class FrigorificoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Frigorífico")
        
        self.provincias = {}

        # Provincia Frame
        self.provincia_frame = ttk.LabelFrame(root, text="Agregar Provincia")
        self.provincia_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        self.provincia_nombre_label = ttk.Label(self.provincia_frame, text="Nombre de la Provincia:")
        self.provincia_nombre_label.grid(row=0, column=0, padx=5, pady=5)

        self.provincia_nombre_entry = ttk.Entry(self.provincia_frame)
        self.provincia_nombre_entry.grid(row=0, column=1, padx=5, pady=5)

        self.agregar_provincia_button = ttk.Button(self.provincia_frame, text="Agregar Provincia", command=self.agregar_provincia)
        self.agregar_provincia_button.grid(row=0, column=2, padx=5, pady=5)

        # Ciudad Frame
        self.ciudad_frame = ttk.LabelFrame(root, text="Agregar Ciudad")
        self.ciudad_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        self.ciudad_nombre_label = ttk.Label(self.ciudad_frame, text="Nombre de la Ciudad:")
        self.ciudad_nombre_label.grid(row=0, column=0, padx=5, pady=5)

        self.ciudad_nombre_entry = ttk.Entry(self.ciudad_frame)
        self.ciudad_nombre_entry.grid(row=0, column=1, padx=5, pady=5)

        self.provincia_ciudad_label = ttk.Label(self.ciudad_frame, text="Provincia:")
        self.provincia_ciudad_label.grid(row=0, column=2, padx=5, pady=5)

        self.provincia_ciudad_combobox = ttk.Combobox(self.ciudad_frame)
        self.provincia_ciudad_combobox.grid(row=0, column=3, padx=5, pady=5)

        self.agregar_ciudad_button = ttk.Button(self.ciudad_frame, text="Agregar Ciudad", command=self.agregar_ciudad)
        self.agregar_ciudad_button.grid(row=0, column=4, padx=5, pady=5)

        # Cliente Frame
        self.cliente_frame = ttk.LabelFrame(root, text="Agregar Cliente")
        self.cliente_frame.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

        self.cliente_nombre_label = ttk.Label(self.cliente_frame, text="Nombre del Cliente:")
        self.cliente_nombre_label.grid(row=0, column=0, padx=5, pady=5)

        self.cliente_nombre_entry = ttk.Entry(self.cliente_frame)
        self.cliente_nombre_entry.grid(row=0, column=1, padx=5, pady=5)

        self.provincia_cliente_label = ttk.Label(self.cliente_frame, text="Provincia:")
        self.provincia_cliente_label.grid(row=0, column=2, padx=5, pady=5)

        self.provincia_cliente_combobox = ttk.Combobox(self.cliente_frame)
        self.provincia_cliente_combobox.grid(row=0, column=3, padx=5, pady=5)
        self.provincia_cliente_combobox.bind("<<ComboboxSelected>>", self.actualizar_ciudades_cliente)

        self.ciudad_cliente_label = ttk.Label(self.cliente_frame, text="Ciudad:")
        self.ciudad_cliente_label.grid(row=0, column=4, padx=5, pady=5)

        self.ciudad_cliente_combobox = ttk.Combobox(self.cliente_frame)
        self.ciudad_cliente_combobox.grid(row=0, column=5, padx=5, pady=5)

        self.agregar_cliente_button = ttk.Button(self.cliente_frame, text="Agregar Cliente", command=self.agregar_cliente)
        self.agregar_cliente_button.grid(row=0, column=6, padx=5, pady=5)

        # Solicitud Frame
        self.solicitud_frame = ttk.LabelFrame(root, text="Agregar Solicitud de Carne")
        self.solicitud_frame.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

        self.cliente_solicitud_label = ttk.Label(self.solicitud_frame, text="Cliente:")
        self.cliente_solicitud_label.grid(row=0, column=0, padx=5, pady=5)

        self.cliente_solicitud_combobox = ttk.Combobox(self.solicitud_frame)
        self.cliente_solicitud_combobox.grid(row=0, column=1, padx=5, pady=5)

        self.tipo_carne_label = ttk.Label(self.solicitud_frame, text="Tipo de Carne:")
        self.tipo_carne_label.grid(row=0, column=2, padx=5, pady=5)

        self.tipo_carne_combobox = ttk.Combobox(self.solicitud_frame, values=list(cortes_carne.keys()))
        self.tipo_carne_combobox.grid(row=0, column=3, padx=5, pady=5)
        self.tipo_carne_combobox.bind("<<ComboboxSelected>>", self.actualizar_cortes_carne)

        self.corte_carne_label = ttk.Label(self.solicitud_frame, text="Corte de Carne:")
        self.corte_carne_label.grid(row=0, column=4, padx=5, pady=5)

        self.corte_carne_combobox = ttk.Combobox(self.solicitud_frame)
        self.corte_carne_combobox.grid(row=0, column=5, padx=5, pady=5)

        self.kilos_carne_label = ttk.Label(self.solicitud_frame, text="Kilos:")
        self.kilos_carne_label.grid(row=0, column=6, padx=5, pady=5)

        self.kilos_carne_entry = ttk.Entry(self.solicitud_frame)
        self.kilos_carne_entry.grid(row=0, column=7, padx=5, pady=5)

        self.agregar_solicitud_button = ttk.Button(self.solicitud_frame, text="Agregar Solicitud", command=self.agregar_solicitud)
        self.agregar_solicitud_button.grid(row=0, column=8, padx=5, pady=5)

        # Remito Frame
        self.remito_frame = ttk.LabelFrame(root, text="Generar Remito")
        self.remito_frame.grid(row=4, column=0, padx=10, pady=10, sticky="ew")

        self.remito_provincia_label = ttk.Label(self.remito_frame, text="Provincia:")
        self.remito_provincia_label.grid(row=0, column=0, padx=5, pady=5)

        self.remito_provincia_combobox = ttk.Combobox(self.remito_frame)
        self.remito_provincia_combobox.grid(row=0, column=1, padx=5, pady=5)
        self.remito_provincia_combobox.bind("<<ComboboxSelected>>", self.actualizar_ciudades_remito)

        self.remito_ciudad_label = ttk.Label(self.remito_frame, text="Ciudad:")
        self.remito_ciudad_label.grid(row=0, column=2, padx=5, pady=5)

        self.remito_ciudad_combobox = ttk.Combobox(self.remito_frame)
        self.remito_ciudad_combobox.grid(row=0, column=3, padx=5, pady=5)

        self.generar_remito_button = ttk.Button(self.remito_frame, text="Generar Remito", command=self.generar_remito)
        self.generar_remito_button.grid(row=0, column=4, padx=5, pady=5)

        self.generar_pdf_button = ttk.Button(self.remito_frame, text="Generar PDF", command=self.generar_pdf)
        self.generar_pdf_button.grid(row=0, column=5, padx=5, pady=5)

        self.remito_text = tk.Text(self.remito_frame, height=15, width=100)
        self.remito_text.grid(row=1, column=0, columnspan=6, padx=5, pady=5)

    def agregar_provincia(self):
        provincia_nombre = self.provincia_nombre_entry.get()
        if provincia_nombre:
            self.provincias[provincia_nombre] = Provincia(provincia_nombre)
            self.provincia_ciudad_combobox['values'] = list(self.provincias.keys())
            self.provincia_cliente_combobox['values'] = list(self.provincias.keys())
            self.remito_provincia_combobox['values'] = list(self.provincias.keys())
            messagebox.showinfo("Éxito", f"Provincia '{provincia_nombre}' agregada.")
        else:
            messagebox.showerror("Error", "Ingrese un nombre válido para la provincia.")
        self.provincia_nombre_entry.delete(0, tk.END)

    def agregar_ciudad(self):
        ciudad_nombre = self.ciudad_nombre_entry.get()
        provincia_nombre = self.provincia_ciudad_combobox.get()
        if ciudad_nombre and provincia_nombre in self.provincias:
            ciudad = Ciudad(ciudad_nombre)
            self.provincias[provincia_nombre].agregar_ciudad(ciudad)
            messagebox.showinfo("Éxito", f"Ciudad '{ciudad_nombre}' agregada a la provincia '{provincia_nombre}'.")
        else:
            messagebox.showerror("Error", "Ingrese un nombre válido para la ciudad y seleccione una provincia.")
        self.ciudad_nombre_entry.delete(0, tk.END)
        self.actualizar_ciudades_cliente(None)

    def agregar_cliente(self):
        cliente_nombre = self.cliente_nombre_entry.get()
        provincia_nombre = self.provincia_cliente_combobox.get()
        ciudad_nombre = self.ciudad_cliente_combobox.get()
        if cliente_nombre and provincia_nombre in self.provincias:
            provincia = self.provincias[provincia_nombre]
            for ciudad in provincia.ciudades:
                if ciudad.nombre == ciudad_nombre:
                    cliente = Cliente(cliente_nombre)
                    ciudad.agregar_cliente(cliente)
                    messagebox.showinfo("Éxito", f"Cliente '{cliente_nombre}' agregado a la ciudad '{ciudad_nombre}' en la provincia '{provincia_nombre}'.")
                    self.cliente_solicitud_combobox['values'] = [cliente.nombre for ciudad in provincia.ciudades for cliente in ciudad.clientes]
                    break
            else:
                messagebox.showerror("Error", "Seleccione una ciudad válida.")
        else:
            messagebox.showerror("Error", "Ingrese un nombre válido para el cliente y seleccione una provincia y una ciudad.")
        self.cliente_nombre_entry.delete(0, tk.END)

    def agregar_solicitud(self):
        cliente_nombre = self.cliente_solicitud_combobox.get()
        tipo_carne = self.tipo_carne_combobox.get()
        corte_carne = self.corte_carne_combobox.get()
        kilos_carne = self.kilos_carne_entry.get()
        provincia_nombre = self.provincia_cliente_combobox.get()
        ciudad_nombre = self.ciudad_cliente_combobox.get()
        if cliente_nombre and tipo_carne and corte_carne and kilos_carne and ciudad_nombre:
            try:
                kilos_carne = float(kilos_carne)
                carne = Carne(tipo_carne, corte_carne, kilos_carne)
                provincia = self.provincias[provincia_nombre]
                for ciudad in provincia.ciudades:
                    if ciudad.nombre == ciudad_nombre:
                        for cliente in ciudad.clientes:
                            if cliente.nombre == cliente_nombre:
                                cliente.solicitar_carne(carne)
                                messagebox.showinfo("Éxito", f"Solicitud de {kilos_carne} kilos de {tipo_carne} ({corte_carne}) agregada al cliente '{cliente_nombre}'.")
                                break
            except ValueError:
                messagebox.showerror("Error", "Ingrese un valor numérico válido para los kilos.")
        else:
            messagebox.showerror("Error", "Ingrese datos válidos para todos los campos.")
        self.kilos_carne_entry.delete(0, tk.END)

    def actualizar_ciudades_cliente(self, event):
        provincia_nombre = self.provincia_cliente_combobox.get()
        if provincia_nombre in self.provincias:
            ciudades = [ciudad.nombre for ciudad in self.provincias[provincia_nombre].ciudades]
            self.ciudad_cliente_combobox['values'] = ciudades
            self.remito_ciudad_combobox['values'] = ciudades

    def actualizar_ciudades_remito(self, event):
        provincia_nombre = self.remito_provincia_combobox.get()
        if provincia_nombre in self.provincias:
            ciudades = [ciudad.nombre for ciudad in self.provincias[provincia_nombre].ciudades]
            self.remito_ciudad_combobox['values'] = ciudades

    def actualizar_cortes_carne(self, event):
        tipo_carne = self.tipo_carne_combobox.get()
        if tipo_carne in cortes_carne:
            self.corte_carne_combobox['values'] = cortes_carne[tipo_carne]

    def generar_remito(self):
        provincia_nombre = self.remito_provincia_combobox.get()
        ciudad_nombre = self.remito_ciudad_combobox.get()
        if provincia_nombre in self.provincias:
            provincia = self.provincias[provincia_nombre]
            remito = crear_remito(provincia)
            self.remito_text.delete(1.0, tk.END)
            self.remito_text.insert(tk.END, f"Kilos para la provincia {remito['provincia']}\n")
            self.remito_text.insert(tk.END, f"Total kilos solicitados: {remito['total_kilos']}\n")
            self.remito_text.insert(tk.END, f"Total kilos bovina: {remito['kilos_bovina']}\n")
            self.remito_text.insert(tk.END, f"Total kilos porcina: {remito['kilos_porcina']}\n")
            self.remito_text.insert(tk.END, "Detalles por ciudad y cliente:\n")
            for ciudad in remito['ciudades']:
                self.remito_text.insert(tk.END, f"\nCiudad: {ciudad['nombre']}\n")
                self.remito_text.insert(tk.END, f"  Total kilos: {ciudad['total_kilos']}\n")
                self.remito_text.insert(tk.END, f"  Kilos bovina: {ciudad['kilos_bovina']}\n")
                self.remito_text.insert(tk.END, f"  Kilos porcina: {ciudad['kilos_porcina']}\n")
                for cliente in ciudad['clientes']:
                    self.remito_text.insert(tk.END, f"  Cliente: {cliente['nombre']}\n")
                    self.remito_text.insert(tk.END, f"    Total kilos: {cliente['total_kilos']}\n")
                    self.remito_text.insert(tk.END, f"    Kilos bovina: {cliente['kilos_bovina']}\n")
                    self.remito_text.insert(tk.END, f"    Kilos porcina: {cliente['kilos_porcina']}\n")
                    self.remito_text.insert(tk.END, "    Detalles:\n")
                    for tipo, corte, peso in cliente['detalles']:
                        self.remito_text.insert(tk.END, f"      {tipo} - {corte}: {peso} kilos\n")
        else:
            messagebox.showerror("Error", "Seleccione una provincia válida.")

    def generar_pdf(self):
        provincia_nombre = self.remito_provincia_combobox.get()
        if provincia_nombre in self.provincias:
            provincia = self.provincias[provincia_nombre]
            remito = crear_remito(provincia)
            pdf_filename = f"Solicitud_{provincia_nombre}.pdf"
            c = canvas.Canvas(pdf_filename, pagesize=letter)
            width, height = letter
            y = height - 40
            c.drawString(30, y, f"Kilos para la provincia {remito['provincia']}")
            y -= 20
            c.drawString(30, y, f"Total kilos solicitados: {remito['total_kilos']}")
            y -= 20
            c.drawString(30, y, f"Total kilos bovina: {remito['kilos_bovina']}")
            y -= 20
            c.drawString(30, y, f"Total kilos porcina: {remito['kilos_porcina']}")
            y -= 20
            c.drawString(30, y, "Detalles por ciudad y cliente:")
            y -= 20
            for ciudad in remito['ciudades']:
                c.drawString(50, y, f"Ciudad: {ciudad['nombre']}")
                y -= 20
                c.drawString(70, y, f"Total kilos: {ciudad['total_kilos']}")
                y -= 20
                c.drawString(70, y, f"Kilos bovina: {ciudad['kilos_bovina']}")
                y -= 20
                c.drawString(70, y, f"Kilos porcina: {ciudad['kilos_porcina']}")
                y -= 20
                for cliente in ciudad['clientes']:
                    c.drawString(90, y, f"Cliente: {cliente['nombre']}")
                    y -= 20
                    c.drawString(110, y, f"Total kilos: {cliente['total_kilos']}")
                    y -= 20
                    c.drawString(110, y, f"Kilos bovina: {cliente['kilos_bovina']}")
                    y -= 20
                    c.drawString(110, y, f"Kilos porcina: {cliente['kilos_porcina']}")
                    y -= 20
                    c.drawString(130, y, "Detalles:")
                    y -= 20
                    for tipo, corte, peso in cliente['detalles']:
                        c.drawString(150, y, f"{tipo} - {corte}: {peso} kilos")
                        y -= 20
            c.save()
            messagebox.showinfo("Éxito", f"PDF generado: {pdf_filename}")
        else:
            messagebox.showerror("Error", "Seleccione una provincia válida.")

if __name__ == "__main__":
    root = tk.Tk()
    app = FrigorificoApp(root)
    root.mainloop()