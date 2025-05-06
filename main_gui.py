import tkinter as tk
from tkinter import ttk, messagebox
from Atividade import Categoria, Desktop, Notebook

# Categorias fixas para seleção
categoria_informatica = Categoria(1, "Informática")
categoria_portateis = Categoria(2, "Portáteis")

def cadastrar():
    tipo = tipo_var.get()
    modelo = entry_modelo.get()
    cor = entry_cor.get()
    preco = float(entry_preco.get())
    extra = entry_extra.get()

    if tipo == "Desktop":
        produto = Desktop(modelo, cor, preco, categoria_informatica, int(extra))
    elif tipo == "Notebook":
        produto = Notebook(modelo, cor, preco, categoria_portateis, int(extra))
    else:
        messagebox.showerror("Erro", "Tipo de produto inválido")
        return

    produto.cadastrar()
    info = produto.getInformacoes()
    messagebox.showinfo("Sucesso", f"{tipo} cadastrado com sucesso:\n\n{info}")

    # Limpar campos
    entry_modelo.delete(0, tk.END)
    entry_cor.delete(0, tk.END)
    entry_preco.delete(0, tk.END)
    entry_extra.delete(0, tk.END)

def atualizar_label_extra(*args):
    if tipo_var.get() == "Desktop":
        label_extra.config(text="Potência da Fonte (W):")
    else:
        label_extra.config(text="Tempo de Bateria (h):")

# Interface
root = tk.Tk()
root.title("Cadastro de Produtos")
root.geometry("400x350")
root.resizable(False, False)

tk.Label(root, text="Tipo de Produto:").pack(pady=5)
tipo_var = tk.StringVar(value="Desktop")
tipo_menu = ttk.Combobox(root, textvariable=tipo_var, values=["Desktop", "Notebook"], state="readonly")
tipo_menu.pack()
tipo_menu.bind("<<ComboboxSelected>>", atualizar_label_extra)

tk.Label(root, text="Modelo:").pack(pady=5)
entry_modelo = tk.Entry(root)
entry_modelo.pack()

tk.Label(root, text="Cor:").pack(pady=5)
entry_cor = tk.Entry(root)
entry_cor.pack()

tk.Label(root, text="Preço:").pack(pady=5)
entry_preco = tk.Entry(root)
entry_preco.pack()

label_extra = tk.Label(root, text="Potência da Fonte (W):")
label_extra.pack(pady=5)
entry_extra = tk.Entry(root)
entry_extra.pack()

tk.Button(root, text="Cadastrar", command=cadastrar).pack(pady=20)

root.mainloop()
