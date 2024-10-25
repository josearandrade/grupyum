# This Python file uses the following encoding: utf-8
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from logic.processing import *
from logic.utils import *
import config.settings as sett
from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QListWidgetItem
# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py
from ui_form import Ui_Grupy1

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
            # Salva os caminhos das imagens selecionadas
            self.image_paths = files

            # Limpa a lista anterior, se houver
            self.ui.list_selected_images.clear()

            # Adiciona os nomes das imagens no QListWidget
            for file in files:
                self.file_name = os.path.basename(file)  # Extrai apenas o nome do arquivo
                self.file_names = self.file_name
                QListWidgetItem(self.file_name, self.ui.list_selected_images)

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

    def full_processing(self):
        self.results = []  # Inicializa uma lista para armazenar resultados
        for image in self.images:  # Percorre cada imagem na lista de imagens
            if sett.GOOD_CONDITION == 1:  # Verifica se a condição é boa
                # Blue cells processing
                blue_lower_bound, blue_upper_bound = color_thresholding_limits(
                    self.ui.bluecell_LR.value(),  # Use .value() para obter os valores inteiros
                    self.ui.bluecell_LG.value(),
                    self.ui.bluecell_LB.value(),
                    self.ui.bluecell_UR.value(),
                    self.ui.bluecell_UG.value(),
                    self.ui.bluecell_UB.value()
                )
                
                # Aplica o thresholding à imagem
                masked_image = masks_apply(image, blue_lower_bound, blue_upper_bound)
                
                # Processa a imagem mascarada (supondo que a função `processing_img` está definida)
                blue_results = processing_img(masked_image, self.ui.edge_canny_lower.value(), self.ui.edge_canny_upper.value(), self.ui.perimeter_min.value(), self.ui.perimeter_max.value(), self.ui.min_circularity.value())
                
                # Blue cells processing
                brown_lower_bound, brown_upper_bound = color_thresholding_limits(
                    self.ui.browncell_LR.value(),  # Use .value() para obter os valores inteiros
                    self.ui.browncell_LG.value(),
                    self.ui.browncell_LB.value(),
                    self.ui.browncell_UR.value(),
                    self.ui.browncell_UG.value(),
                    self.ui.browncell_UB.value()
                )
                
                # Aplica o thresholding à imagem
                masked_image = masks_apply(image, brown_lower_bound, brown_upper_bound)

                brown_results = processing_img(masked_image, self.ui.edge_canny_lower.value(), self.ui.edge_canny_upper.value(), self.ui.perimeter_min.value(), self.ui.perimeter_max.value(), self.ui.min_circularity.value())

                # Adiciona o resultado à lista de resultados

                # Formata a string para exibir no QListWidget
                result_text = f"Image: {self.file_names} | Blue: {blue_results} | Brown: {brown_results} | Total: {blue_results+brown_results}"

                # A função QListWidgetItem deve ser usada para adicionar um item à QListWidget
                item = QListWidgetItem(result_text)  # Converte resultados em string, se necessário
                self.ui.list_results.addItem(item)  # Adiciona o item à QListWidget

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
