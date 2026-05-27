import tkinter as tk
from tkinter import messagebox
import tkinter.font as tkFont

class JuegoAhorcado:
    def __init__(self, master):
        self.master = master
        self.master.title("Juego del Ahorcado - Muñeco Colgado")
        self.master.resizable(False, False)
        self.master.geometry("900x700")

        default_font = tkFont.nametofont("TkDefaultFont")
        default_font.configure(size=14)

        self.intentos_max = 6
        self.palabra = ""
        self.letras_adivinadas = set()
        self.letras_usadas = set()
        self.intentos_fallidos = 0

        self.build_palabra_ingreso_ui()

    def build_palabra_ingreso_ui(self):
        self.frame_ingreso = tk.Frame(self.master, padx=40, pady=40)
        self.frame_ingreso.pack()

        titulo = tk.Label(self.frame_ingreso, text="Ingrese la palabra a adivinar", font=("Helvetica", 24, "bold"))
        titulo.grid(row=0, column=0, columnspan=2, pady=(0, 25))

        etiqueta = tk.Label(self.frame_ingreso, text="Palabra:", font=("Helvetica", 16))
        etiqueta.grid(row=1, column=0, sticky='e')

        # Campo de texto SIN asteriscos
        self.entry_palabra = tk.Entry(self.frame_ingreso, font=("Helvetica", 18), width=20)
        self.entry_palabra.grid(row=1, column=1, sticky='w')
        self.entry_palabra.focus()

        boton_confirmar = tk.Button(self.frame_ingreso, text="Confirmar palabra", command=self.confirmar_palabra, font=("Helvetica", 14))
        boton_confirmar.grid(row=2, column=0, columnspan=2, pady=(25, 0))

    def confirmar_palabra(self):
        palabra = self.entry_palabra.get().strip().upper()
        if not palabra.isalpha():
            messagebox.showwarning("Error", "Por favor, ingrese una palabra válida solo con letras")
            self.entry_palabra.delete(0, tk.END)
            return
        self.palabra = palabra
        self.frame_ingreso.destroy()
        self.inicializar_juego_ui()

    def inicializar_juego_ui(self):
        self.letras_adivinadas = set()
        self.letras_usadas = set()
        self.intentos_fallidos = 0

        self.frame = tk.Frame(self.master, padx=40, pady=40)
        self.frame.pack()

        self.titulo = tk.Label(self.frame, text="Juego del ahorcado - Muñeco Colgado", font=("Helvetica", 26, "bold"))
        self.titulo.grid(row=0, column=0, columnspan=4, pady=(0, 25))

        self.canvas = tk.Canvas(self.frame, width=350, height=500, bg='#f9f9f9')
        self.canvas.grid(row=1, column=0, rowspan=6, padx=(0, 30))

        self.palabra_var = tk.StringVar()
        self.palabra_label = tk.Label(self.frame, textvariable=self.palabra_var, font=("Courier", 36, "bold"))
        self.palabra_label.grid(row=1, column=1, columnspan=3, sticky='w')

        self.info_var = tk.StringVar()
        self.info_label = tk.Label(self.frame, textvariable=self.info_var, font=("Helvetica", 14), fg="gray")
        self.info_label.grid(row=2, column=1, columnspan=3, sticky='w')

        self.letra_label = tk.Label(self.frame, text="Ingrese una letra:", font=("Helvetica", 18))
        self.letra_label.grid(row=3, column=1, sticky='w')

        self.letra_entry = tk.Entry(self.frame, width=5, font=("Helvetica", 18))
        self.letra_entry.grid(row=3, column=2, sticky='w')
        self.letra_entry.bind("<Return>", self.intentar_letra)

        self.intentar_boton = tk.Button(self.frame, text="Intentar", command=self.intentar_letra, width=12, font=("Helvetica", 14))
        self.intentar_boton.grid(row=3, column=3, sticky='w')

        self.letras_usadas_var = tk.StringVar()
        self.letras_usadas_label = tk.Label(self.frame, textvariable=self.letras_usadas_var, font=("Helvetica", 14), fg="blue")
        self.letras_usadas_label.grid(row=4, column=1, columnspan=3, sticky='w', pady=(15, 0))

        self.reiniciar_boton = tk.Button(self.frame, text="Reiniciar Juego (Nueva palabra)", command=self.reiniciar_a_ingreso, width=30, font=("Helvetica", 14))
        self.reiniciar_boton.grid(row=7, column=0, columnspan=4, pady=(25, 0))

        self.actualizar_palabra_display()
        self.info_var.set(f"intentos restantes: {self.intentos_max - self.intentos_fallidos}")
        self.letras_usadas_var.set("Letras usadas: ")
        self.letra_entry.focus()
        self.dibujar_ahorcado()

    def reiniciar_a_ingreso(self):
        self.frame.destroy()
        self.build_palabra_ingreso_ui()

    def actualizar_palabra_display(self):
        display = ' '.join([letra if letra in self.letras_adivinadas else '_' for letra in self.palabra])
        self.palabra_var.set(display)

    def intentar_letra(self, event=None):
        letra = self.letra_entry.get().strip().upper()
        if len(letra) != 1 or not letra.isalpha():
            messagebox.showwarning("Aviso", "Por favor, ingrese solo una letra válida.")
            self.letra_entry.delete(0, tk.END)
            return
        if letra in self.letras_usadas:
            messagebox.showinfo("Aviso", f"La letra '{letra}' ya ha sido usada.")
            self.letra_entry.delete(0, tk.END)
            return

        self.letras_usadas.add(letra)
        if letra in self.palabra:
            self.letras_adivinadas.add(letra)
            self.actualizar_palabra_display()
            if self.gano():
                self.info_var.set("¡Felicidades! ¡Ganaste!")
                messagebox.showinfo("Juego Terminado", f"¡Felicidades! la palabra era '{self.palabra}'. ¡Ganaste!")
                self.deshabilitar_entrada()
        else:
            self.intentos_fallidos += 1
            self.dibujar_ahorcado()
            self.info_var.set(f"intentos restantes: {self.intentos_max - self.intentos_fallidos}")
            if self.perdio():
                self.info_var.set(f"¡Perdiste! La palabra era '{self.palabra}'.")
                messagebox.showinfo("Juego Terminado", f"¡Perdiste! La palabra era '{self.palabra}'.")
                self.actualizar_palabra_display()
                self.deshabilitar_entrada()

        self.letras_usadas_var.set("Letras usadas: " + ", ".join(sorted(self.letras_usadas)))
        self.letra_entry.delete(0, tk.END)
        self.letra_entry.focus()

    def deshabilitar_entrada(self):
        self.letra_entry.config(state="disabled")
        self.intentar_boton.config(state="disabled")

    def gano(self):
        return all(letra in self.letras_adivinadas for letra in self.palabra)

    def perdio(self):
        return self.intentos_fallidos >= self.intentos_max

    def dibujar_ahorcado(self):
        self.canvas.delete("all")

        self.canvas.create_line(40, 300, 260, 300, width=5)
        self.canvas.create_line(60, 300, 60, 40, width=5)
        self.canvas.create_line(60, 40, 200, 40, width=5)
        self.canvas.create_line(200, 40, 200, 80, width=4)

        fallos = self.intentos_fallidos

        if fallos > 0:
            self.canvas.create_oval(180, 80, 220, 120, width=4)
        if fallos > 1:
            self.canvas.create_line(200, 120, 200, 200, width=4)
        if fallos > 2:
            self.canvas.create_line(200, 150, 170, 180, width=4)
        if fallos > 3:
            self.canvas.create_line(200, 150, 230, 180, width=4)
        if fallos > 4:
            self.canvas.create_line(200, 200, 180, 240, width=4)
            self.canvas.create_line(180, 240, 185, 250, width=4)
        if fallos > 5:
            self.canvas.create_line(200, 200, 220, 240, width=4)
            self.canvas.create_line(220, 240, 215, 250, width=4)
        if fallos == self.intentos_max:
            self.canvas.create_line(180, 120, 220, 120, width=3)

if __name__ == "__main__":
    root = tk.Tk()
    juego = JuegoAhorcado(root)
    root.mainloop()