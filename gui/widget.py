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
        self.ui.loadButton.clicked.connect(self.load_images)

        # Inicialmente, esconder a QLabel
        self.ui.load_OK.hide()  # Esconder a QLabel até que o carregamento seja concluído
        
        # Conectar o botão ao método para carregar as imagens
        self.ui.processButton.clicked.connect(self.full_processing)

        # Exporta em um arquivo json
        self.ui.exportButton.clicked.connect(self.export_to_excel)

        # Settings values 
        ## Color Thresholding
        self.ui.browncell_LR.setValue(sett.BROWN_CELL_LR)
        self.ui.browncell_LG.setValue(sett.BROWN_CELL_LG)
        self.ui.browncell_LB.setValue(sett.BROWN_CELL_LB)
        self.ui.browncell_UR.setValue(sett.BROWN_CELL_UR)
        self.ui.browncell_UG.setValue(sett.BROWN_CELL_UG)
        self.ui.browncell_UB.setValue(sett.BROWN_CELL_UB)
        self.ui.bluecell_LR.setValue(sett.BLUE_CELL_LR)
        self.ui.bluecell_LG.setValue(sett.BLUE_CELL_LG)
        self.ui.bluecell_LB.setValue(sett.BLUE_CELL_LB)
        self.ui.bluecell_UR.setValue(sett.BLUE_CELL_UR)
        self.ui.bluecell_UG.setValue(sett.BLUE_CELL_UG)
        self.ui.bluecell_UB.setValue(sett.BLUE_CELL_UB)
        
        ## Edge Canny
        self.ui.edge_canny_lower.setValue(sett.EDGE_CANNY_LOWER)
        self.ui.edge_canny_upper.setValue(sett.EDGE_CANNY_UPPER)

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

    def load_images(self):
        # Verifica se há imagens selecionadas
        if self.image_paths:
            self.images = load_image_rgb(self.image_paths)  # Carrega as imagens e retorna a lista de imagens
            if self.images:  # Verifica se alguma imagem foi carregada
                self.ui.load_OK.setText("Load OK")  # Atualiza o texto da QLabel
                self.ui.load_OK.show()  # Mostra a QLabel
            else:
                self.ui.load_OK.setText("Erro ao carregar as imagens")
                self.ui.load_OK.show()  # Mostra a QLabel

    # Função para processar imagens e adicionar itens clicáveis à lista de resultados
    def full_processing(self):
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
                    self.ui.bluecell_LR.value(), self.ui.bluecell_LG.value(),
                    self.ui.bluecell_LB.value(), self.ui.bluecell_UR.value(),
                    self.ui.bluecell_UG.value(), self.ui.bluecell_UB.value()
                )
                masked_image = masks_apply(image, blue_lower_bound, blue_upper_bound)
                blue_results = processing_img(
                    masked_image, self.ui.edge_canny_lower.value(),
                    self.ui.edge_canny_upper.value(), self.ui.perimeter_min.value(), 
                    self.ui.perimeter_max.value(), self.ui.min_circularity.value()
                )

                # Processamento das células marrons
                brown_lower_bound, brown_upper_bound = color_thresholding_limits(
                    self.ui.browncell_LR.value(), self.ui.browncell_LG.value(),
                    self.ui.browncell_LB.value(), self.ui.browncell_UR.value(),
                    self.ui.browncell_UG.value(), self.ui.browncell_UB.value()
                )
                masked_image = masks_apply(image, brown_lower_bound, brown_upper_bound)
                brown_results = processing_img(
                    masked_image, self.ui.edge_canny_lower.value(), 
                    self.ui.edge_canny_upper.value(), self.ui.perimeter_min.value(), 
                    self.ui.perimeter_max.value(), self.ui.min_circularity.value()
                )
                percentage = round(((brown_results/(blue_results + brown_results))*100), 2)
                # Salva cada campo como uma chave-valor no dicionário
                result_entry = {
                    "Image": image_name,
                    "Brown Cells": brown_results,
                    "Blue Cells": blue_results,
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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
