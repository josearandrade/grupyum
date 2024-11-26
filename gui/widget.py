# This Python file uses the following encoding: utf-8
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from logic.processing import *
#from logic.utils import *
import config.settings as sett
from PyQt6.QtWidgets import QApplication, QWidget, QFileDialog, QListWidgetItem
# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py
from ui_form import Ui_Grupy1
import json
import pandas as pd

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Grupy1()
        self.ui.setupUi(self)

        # Conectar o botão ao método para selecionar imagens
        self.ui.importButton.clicked.connect(self.select_images)

        # Variável para armazenar os caminhos das imagens selecionadas
        self.image_paths = []
        self.file_names = []
        
        # Conectar o botão ao método para carregar as imagens
        self.ui.processButton.clicked.connect(self.full_processing)

        # Exporta em um arquivo json
        self.ui.exportButton.clicked.connect(self.export_to_excel)

        # Botão de reset
        self.ui.resetButton.clicked.connect(self.clear_results)

        # Settings values 
        ## Color Thresholding
        self.ui.brownmarker_LR.setValue(sett.BROWN_MARKER_LR)
        self.ui.brownmarker_LG.setValue(sett.BROWN_MARKER_LG)
        self.ui.brownmarker_LB.setValue(sett.BROWN_MARKER_LB)
        self.ui.brownmarker_UR.setValue(sett.BROWN_MARKER_UR)
        self.ui.brownmarker_UG.setValue(sett.BROWN_MARKER_UG)
        self.ui.brownmarker_UB.setValue(sett.BROWN_MARKER_UB)
        self.ui.bluemarker_LR.setValue(sett.BLUE_MARKER_LR)
        self.ui.bluemarker_LG.setValue(sett.BLUE_MARKER_LG)
        self.ui.bluemarker_LB.setValue(sett.BLUE_MARKER_LB)
        self.ui.bluemarker_UR.setValue(sett.BLUE_MARKER_UR)
        self.ui.bluemarker_UG.setValue(sett.BLUE_MARKER_UG)
        self.ui.bluemarker_UB.setValue(sett.BLUE_MARKER_UB)

        

        ## Perimeter
        self.ui.perimeter_min.setValue(sett.PERIMETER_MIN)
        self.ui.perimeter_max.setValue(sett.PERIMETER_MAX)
        self.ui.min_circularity.setValue(sett.MIN_CIRCULARITY)

    def select_images(self):
        # Abre o QFileDialog para selecionar imagens
        files, _ = QFileDialog.getOpenFileNames(self, "Select images", "", "Images (*.png *.jpg *.jpeg *.bmp *.tif)")

        if files:
            # Salva os caminhos das imagens selecionadas e os nomes dos arquivos
            self.image_paths = files
            self.file_names = [os.path.basename(file) for file in files]  # Lista com os nomes dos arquivos

            # Limpa a lista anterior e adiciona os novos nomes ao QListWidget
            self.ui.list_selected_images.clear()
            for file_name in self.file_names:
                QListWidgetItem(file_name, self.ui.list_selected_images)

    # Função para processar imagens e adicionar itens clicáveis à lista de resultados
    def full_processing(self):

        if self.image_paths:
            self.images = load_image_rgb(self.image_paths)  # Carrega as imagens e retorna a lista de imagens
            

        self.results = []  # Armazena os resultados como dicionários para exportação organizada
        total_images = len(self.images)
        
        for idx, image in enumerate(self.images):
            image_name = self.file_names[idx]
            
            # Atualiza a barra de progresso
            progress = int((idx + 1) / total_images * 100)
            self.ui.progressBar.setValue(progress)

            if sett.GOOD_CONDITION == 1:
                # Processamento das células azuis
                blue_lower_bound, blue_upper_bound = color_thresholding_limits(
                    self.ui.bluemarker_LR.value(), self.ui.bluemarker_LG.value(),
                    self.ui.bluemarker_LB.value(), self.ui.bluemarker_UR.value(),
                    self.ui.bluemarker_UG.value(), self.ui.bluemarker_UB.value()
                )
                masked_image = masks_apply(image, blue_lower_bound, blue_upper_bound)
                blue_results = processing_img(
                    masked_image, 75, 100, self.ui.perimeter_min.value(), 
                    self.ui.perimeter_max.value(), self.ui.min_circularity.value()
                )

                # Processamento das células marrons
                brown_lower_bound, brown_upper_bound = color_thresholding_limits(
                    self.ui.brownmarker_LR.value(), self.ui.brownmarker_LG.value(),
                    self.ui.brownmarker_LB.value(), self.ui.brownmarker_UR.value(),
                    self.ui.brownmarker_UG.value(), self.ui.brownmarker_UB.value()
                )
                masked_image = masks_apply(image, brown_lower_bound, brown_upper_bound)
                brown_results = processing_img(
                    masked_image, 75, 100, self.ui.perimeter_min.value(), 
                    self.ui.perimeter_max.value(), self.ui.min_circularity.value()
                )
                percentage = round(((brown_results/(blue_results + brown_results))*100), 2)
                # Salva cada campo como uma chave-valor no dicionário
                result_entry = {
                    "Image": image_name,
                    "Brown Marker": brown_results,
                    "Blue Marker": blue_results,
                    "Total": blue_results + brown_results,
                    "Percentage +": percentage
                }
                self.results.append(result_entry)
                
                # Exibe o resultado na interface
                result_text = f"Image: {image_name} | Brown: {brown_results} | Blue: {blue_results}  | Total: {blue_results + brown_results} | Percentage +: {percentage}"
                item = QListWidgetItem(result_text)
                self.ui.list_results.addItem(item)

        
    # Função para exportar os resultados para um arquivo JSON (não está sendo usada)
    #def export_to_json(self, filename=None):
    #    filename = filename if isinstance(filename, str) else "results.json"
    #
    #   try:
    #        with open(filename, 'w', encoding='utf-8') as f:
    #            json.dump(self.results, f, ensure_ascii=False, indent=4)
    #        print(f"Resultados exportados para {filename} com sucesso.")
    #    except OSError as e:
    #        print(f"Erro ao exportar para {filename}: {e}")

    def export_to_excel(self):
        # Abre o diálogo para o usuário escolher o local e nome do arquivo
        filename, _ = QFileDialog.getSaveFileName(self, "Salvar arquivo Excel", "", "Excel Files (*.xlsx);;All Files (*)")
        
        # Checa se o usuário forneceu um nome de arquivo válido
        if filename:
            if not filename.endswith(".xlsx"):
                filename += ".xlsx"  # Adiciona a extensão se não estiver presente
                try:
                    data = pd.DataFrame(self.results)
                    data.to_excel(filename, index=False)
                    print(f"Resultados exportados para {filename} com sucesso.")
                except OSError as e:
                    print(f"Erro ao exportar para {filename}: {e}")
            else:
                print("Exportação cancelada pelo usuário.")

    def clear_results(self):
        self.ui.list_results.clear()  # Limpa os itens da QListWidget na interface
        self.results = []  # Reseta a lista de resultados
        self.ui.progressBar.setValue(0)  # Reseta a barra de progresso para 0


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
