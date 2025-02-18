import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import numpy as np

class StegoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Steganographie - Code in Bild verstecken")
        self.root.geometry("500x350")

        # GUI-Elemente
        tk.Label(root, text="Verstecke Code in einem Bild", font=("Arial", 14)).pack(pady=10)

        self.btn_select_image = tk.Button(root, text="Bild auswählen", command=self.load_image)
        self.btn_select_image.pack(pady=5)

        self.label_info = tk.Label(root, text="Maximale Textlänge: -", fg="blue")
        self.label_info.pack(pady=5)

        self.text_area = tk.Text(root, height=5, width=50)
        self.text_area.pack(pady=5)
        self.text_area.insert(tk.END, "Hier Code eingeben...")

        self.btn_hide = tk.Button(root, text="Code einbetten", command=self.hide_code)
        self.btn_hide.pack(pady=5)

        self.btn_extract = tk.Button(root, text="Code extrahieren", command=self.extract_code)
        self.btn_extract.pack(pady=5)

        self.selected_image = None
        self.image_capacity = 0  # Maximale Textlänge, die im Bild gespeichert werden kann

    def load_image(self):
        """Lädt das Bild für die Verarbeitung und zeigt die maximale Textlänge an."""
        file_path = filedialog.askopenfilename(filetypes=[("Bilder", "*.png;*.jpg;*.bmp")])
        if file_path:
            try:
                img = Image.open(file_path)
                img = img.convert("RGB")
                pixels = np.array(img)
                self.image_capacity = (pixels.shape[0] * pixels.shape[1] * 3) // 8 - 1  # 1 Byte für Endmarkierung
                self.selected_image = file_path
                self.label_info.config(text=f"Maximale Textlänge: {self.image_capacity} Zeichen")
                messagebox.showinfo("Bild geladen", f"Bild erfolgreich geladen: {file_path}")
            except Exception as e:
                messagebox.showerror("Fehler", f"Fehler beim Laden des Bildes: {str(e)}")

    def text_to_binary(self, text):
        """Wandelt Text in eine Binärdarstellung um."""
        return ''.join(format(ord(char), '08b') for char in text)

    def binary_to_text(self, binary):
        """Wandelt Binärdaten zurück in Text."""
        chars = [binary[i:i+8] for i in range(0, len(binary), 8)]
        return ''.join(chr(int(char, 2)) for char in chars if int(char, 2) != 0)

    def hide_code(self):
        """Versteckt den eingegebenen Code in einem Bild."""
        if not self.selected_image:
            messagebox.showerror("Fehler", "Kein Bild ausgewählt!")
            return

        code = self.text_area.get("1.0", tk.END).strip()
        if not code:
            messagebox.showerror("Fehler", "Kein Code eingegeben!")
            return

        if len(code) > self.image_capacity:
            messagebox.showerror("Fehler", f"Der Text ist zu lang! Maximale Länge: {self.image_capacity} Zeichen")
            return

        try:
            img = Image.open(self.selected_image)
            img = img.convert("RGB")
            pixels = np.array(img)

            binary_code = self.text_to_binary(code) + '1111111111111110'  # Endmarkierung
            index = 0

            for row in pixels:
                for pixel in row:
                    for i in range(3):  # RGB-Kanäle
                        if index < len(binary_code):
                            pixel[i] = (pixel[i] & ~1) | int(binary_code[index])  # LSB ersetzen
                            index += 1

            stego_img = Image.fromarray(pixels)
            output_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Images", "*.png")])
            if output_path:
                stego_img.save(output_path)
                messagebox.showinfo("Erfolg", f"Code erfolgreich in {output_path} gespeichert!")
        except Exception as e:
            messagebox.showerror("Fehler", f"Fehler beim Einbetten des Codes: {str(e)}")

    def extract_code(self):
        """Extrahiert versteckten Code aus einem Bild."""
        if not self.selected_image:
            messagebox.showerror("Fehler", "Kein Bild ausgewählt!")
            return

        try:
            img = Image.open(self.selected_image)
            img = img.convert("RGB")
            pixels = np.array(img)

            binary_code = ""
            for row in pixels:
                for pixel in row:
                    for i in range(3):
                        binary_code += str(pixel[i] & 1)  # LSB auslesen

            binary_code = binary_code.split('1111111111111110')[0]  # Endmarkierung finden
            extracted_text = self.binary_to_text(binary_code)

            # Zeigt den extrahierten Code in der Textbox
            self.text_area.delete("1.0", tk.END)
            self.text_area.insert(tk.END, extracted_text)
            messagebox.showinfo("Extrahierter Code", "Code wurde erfolgreich extrahiert!")
        except Exception as e:
            messagebox.showerror("Fehler", f"Fehler beim Extrahieren des Codes: {str(e)}")

# Starte das Programm
if __name__ == "__main__":
    root = tk.Tk()
    app = StegoApp(root)
    root.mainloop()
